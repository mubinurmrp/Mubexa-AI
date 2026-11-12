import ast
import json
import operator
import os
import re
import subproces
from config import *
import time
import urllib.request
from datetime import datetime

history = []
speaker = None

BN_DIGITS = str.maketrans("০১২৩৪৫৬৭৮৯", "0123456789")
DAYS = ["সোমবার", "মঙ্গলবার", "বুধবার", "বৃহস্পতিবার",
        "শুক্রবার", "শনিবার", "রবিবার"]


def speak(text):
    global speaker
    text = re.sub(r"[\U0001F300-\U0001FAFF\u2600-\u27BF\uFE0F]", "", text).strip()
    if not text:
        return
    try:
        if speaker and speaker.poll() is None:
            speaker.terminate()
        speaker = subprocess.Popen(["termux-tts-speak", "-l", "bn", text])
    except OSError:
        pass


def say(text):
    print("Mubexa:", text)
    speak(text)


def listen():
    print("🎤 বলুন...")
    try:
        out = subprocess.run(["termux-speech-to-text"],
                             capture_output=True, text=True, timeout=30)
        return out.stdout.strip()
    except (OSError, subprocess.TimeoutExpired):
        return ""


def save_memory():
    with open(memory_file, "w", encoding="utf-8") as f:
        json.dump(memory, f, ensure_ascii=False, indent=4)


# ---------- অফলাইন কমান্ড ----------

OPS = {
    ast.Add: operator.add, ast.Sub: operator.sub,
    ast.Mult: operator.mul, ast.Div: operator.truediv,
    ast.USub: operator.neg,
}


def safe_eval(node):
    if isinstance(node, ast.Expression):
        return safe_eval(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in OPS:
        return OPS[type(node.op)](safe_eval(node.left), safe_eval(node.right))
    if isinstance(node, ast.UnaryOp) and type(node.op) in OPS:
        return OPS[type(node.op)](safe_eval(node.operand))
    raise ValueError("unsafe")


def calculate(text):
    t = text.lower().translate(BN_DIGITS)
    for word, sym in (("বিয়োগ", "-"), ("minus", "-"), ("যোগ", "+"), ("plus", "+"),
                      ("গুণ", "*"), ("times", "*"), ("into", "*"), ("×", "*"),
                      ("ভাগ", "/"), ("divided by", "/"), ("÷", "/")):
        t = t.replace(word, sym)
    t = t.replace(" x ", "*")
    expr = re.sub(r"[^0-9+\-*/().\s]", "", t).strip()
    if not re.search(r"\d\s*[-+*/]\s*\d", expr):
        return None
    try:
        result = safe_eval(ast.parse(expr, mode="eval"))
    except Exception:
        return None
    if isinstance(result, float) and result.is_integer():
        result = int(result)
    elif isinstance(result, float):
        result = round(result, 4)
    return f"উত্তর {result}"


def run(cmd):
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=15)
    except (OSError, subprocess.TimeoutExpired):
        return None


def open_intent(args):
    r = run(["am", "start"] + args)
    return r is not None and r.returncode == 0


APPS = [
    (("ইউটিউব", "youtube"), "ইউটিউব",
     ["-a", "android.intent.action.VIEW", "-d", "https://www.youtube.com"]),
    (("গুগল", "google"), "গুগল",
     ["-a", "android.intent.action.VIEW", "-d", "https://www.google.com"]),
    (("হোয়াটসঅ্যাপ", "whatsapp"), "হোয়াটসঅ্যাপ",
     ["-a", "android.intent.action.VIEW", "-d", "https://wa.me"]),
    (("ফেসবুক", "facebook"), "ফেসবুক",
     ["-a", "android.intent.action.VIEW", "-d", "https://www.facebook.com"]),
    (("ক্যামেরা", "camera"), "ক্যামেরা",
     ["-a", "android.media.action.IMAGE_CAPTURE"]),
    (("সেটিংস", "settings"), "সেটিংস",
     ["-a", "android.settings.SETTINGS"]),
    (("ডায়াল", "dialer"), "ডায়ালার",
     ["-a", "android.intent.action.DIAL"]),
]


def is_time_question(t):
    if "সময়" in t:
        return True
    if ("কয়টা" in t or "কটা" in t) and "বাজ" in t:
        return True
    if re.search(r"\b(time|somoy|samay)\b", t):
        return True
    if re.search(r"\b(koyta|kota|kyta)\b", t) and re.search(r"\b(baje|bajche|baj)\b", t):
        return True
    return False


def is_date_question(t):
    if "তারিখ" in t or "কি বার" in t or "কী বার" in t:
        return True
    if re.search(r"\b(date|tarikh|tarik|today)\b", t):
        return True
    return False


def offline_command(text):
    t = text.lower()

    # ক্যালকুলেটর
    calc = calculate(text)
    if calc:
        return calc

    # সময়
    if is_time_question(t):
        return "এখন সময় " + datetime.now().strftime("%I:%M %p")

    # তারিখ
    if is_date_question(t):
        now = datetime.now()
        return f"আজ {DAYS[now.weekday()]}, " + now.strftime("%d-%m-%Y")

    # ব্যাটারি
    if "ব্যাটারি" in t or "battery" in t or "চার্জ" in t or "batari" in t:
        r = run(["termux-battery-status"])
        if r and r.stdout.strip():
            try:
                d = json.loads(r.stdout)
                charging = "চার্জ হচ্ছে" if d.get("status") == "CHARGING" else "চার্জ হচ্ছে না"
                return f"ব্যাটারি {d.get('percentage')} শতাংশ, {charging}"
            except ValueError:
                pass
        return "ব্যাটারির তথ্য পেলাম না। Termux:API অ্যাপ চেক করুন।"

    # টর্চ
    if "টর্চ" in t or "torch" in t or "flashlight" in t:
        off = any(w in t for w in ("নেভা", "বন্ধ", "off", "nevao", "bondho"))
        r = run(["termux-torch", "off" if off else "on"])
        if r is None or r.returncode != 0:
            return "টর্চ চালাতে পারলাম না।"
        return "টর্চ বন্ধ করলাম।" if off else "টর্চ জ্বালালাম।"

    # ভলিউম
    if "ভলিউম" in t or "volume" in t:
        up = any(w in t for w in ("বাড়া", "বেশি", "up", "increase", "barao"))
        down = any(w in t for w in ("কমা", "কম", "down", "decrease", "komao"))
        if up or down:
            r = run(["termux-volume", "music", "12" if up else "4"])
            if r and r.returncode == 0:
                return "ভলিউম বাড়ালাম।" if up else "ভলিউম কমালাম।"
        return None

    # অ্যাপ খোলা
    if any(w in t for w in ("খোল", "চালু", "open", "kholo", "khulo")):
        for keys, name, args in APPS:
            if any(k in t for k in keys):
                if open_intent(args):
                    return f"{name} খুলছি।"
                return f"{name} খুলতে পারলাম না।"

    return None


# ---------- AI ----------

def ask_ai(user_text):
    system = (
        "তুমি Mubexa, একটি বাংলা AI সহকারী। ব্যবহারকারী বাংলা, ইংরেজি বা বাংলিশে "
        "লিখলেও বুঝে সহজ বাংলায় ছোট উত্তর দাও। ইমোজি ব্যবহার করবে না। "
        "ব্যবহারকারী সম্পর্কে যা জানা আছে: "
        + json.dumps(memory, ensure_ascii=False)
        + " এখনকার সঠিক সময়: "
        + datetime.now().strftime("%d-%m-%Y %I:%M %p")
        + "। সময় বা তারিখ জিজ্ঞেস করলে শুধু এটা বলো, নিজে অনুমান করো না।"
    )
    history.append({"role": "user", "parts": [{"text": user_text}]})
    body = json.dumps({
        "system_instruction": {"parts": [{"text": system}]},
        "contents": history[-20:],
    }).encode("utf-8")

    last_error = None
    for model in MODELS:
        url = ("https://generativelanguage.googleapis.com/v1beta/models/"
               + model + ":generateContent")
        for attempt in range(2):
            req = urllib.request.Request(
                url, data=body,
                headers={"Content-Type": "application/json",
                         "x-goog-api-key": API_KEY},
            )
            try:
                with urllib.request.urlopen(req, timeout=15) as r:
                    data = json.loads(r.read().decode("utf-8"))
                answer = data["candidates"][0]["content"]["parts"][0]["text"].strip()
                history.append({"role": "model", "parts": [{"text": answer}]})
                return answer
            except Exception as e:
                last_error = e
                time.sleep(1)

    history.pop()
    print("(এরর:", last_error, ")")
    return None


if not API_KEY:
    print("সতর্কতা: GEMINI_API_KEY সেট নেই, শুধু অফলাইন কমান্ড চলবে।")

memory = {}
if os.path.exists(memory_file):
    try:
        with open(memory_file, "r", encoding="utf-8") as f:
            memory = json.load(f)
    except (json.JSONDecodeError, OSError):
        memory = {}

print("Mubexa AI 🤖")
print("ভয়েসের জন্য 'v' লিখুন, বন্ধ করতে 'exit' লিখুন।\n")

if "নাম" in memory:
    say(f"স্বাগতম {memory['নাম']}")

while True:
    raw = input("আপনি: ").strip()

    if raw.lower() == "v":
        user = listen()
        if not user:
            say("বুঝতে পারিনি, আবার বলুন।")
            continue
        print("আপনি বলেছেন:", user)
    else:
        user = raw

    if not user:
        continue

    if user.lower() in ("exit", "বিদায়", "বন্ধ করো"):
        say("বিদায়! আবার কথা হবে।")
        if speaker:
            speaker.wait()
        break

    if "আমার নাম" in user or "my name is" in user.lower():
        name = re.split(r"আমার নাম|my name is", user, flags=re.I)[-1]
        name = name.replace("হলো", "").replace("হল", "").strip(" :-")
        if name:
            memory["নাম"] = name
            save_memory()

    # আগে অফলাইন কমান্ড, না মিললে AI
    reply = offline_command(user)
    if reply:
        say(reply)
        continue

    answer = ask_ai(user) if API_KEY else None
    if answer:
        say(answer)
    else:
        say("এখন ইন্টারনেট বা API-তে সমস্যা, পরে চেষ্টা করুন।")

