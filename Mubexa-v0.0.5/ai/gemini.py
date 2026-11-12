import json
import time
import urllib.request

from config import API_KEY, MODELS, MAX_HISTORY
from core.memory import load_memory


history = []


def ask_ai(user_text):

    if not API_KEY:
        return "Gemini API Key সেট করা নেই।"

    memory = load_memory()

    system = (
        "তুমি Mubexa, একটি বাংলা AI সহকারী। "
        "ব্যবহারকারী বাংলা, ইংরেজি বা Banglish-এ কথা বলতে পারে। "
        "Speech-to-text ভুল হলে কাছাকাছি শব্দের অর্থ বুঝে নাও। "
        "যেমন: "
        "Akon somoy koto মানে এখন সময় কত। "
        "Tomar nam ki মানে তোমার নাম কী। "
        "সহজ ও ছোট বাংলায় উত্তর দেবে। "
        "ইমোজি ব্যবহার করবে না। "
        "ব্যবহারকারীর তথ্য: "
        + json.dumps(memory, ensure_ascii=False)
    )

    history.append(
        {
            "role": "user",
            "parts": [
                {
                    "text": user_text
                }
            ]
        }
    )

    body = json.dumps(
        {
            "system_instruction": {
                "parts": [
                    {
                        "text": system
                    }
                ]
            },
            "contents": history[-MAX_HISTORY:]
        }
    ).encode("utf-8")


    for model in MODELS:

        url = (
            "https://generativelanguage.googleapis.com/v1beta/models/"
            + model
            + ":generateContent"
        )

        request = urllib.request.Request(
            url,
            data=body,
            headers={
                "Content-Type": "application/json",
                "x-goog-api-key": API_KEY
            }
        )

        try:
            with urllib.request.urlopen(
                request,
                timeout=20
            ) as response:

                data = json.loads(
                    response.read().decode("utf-8")
                )

            answer = (
                data["candidates"][0]
                ["content"]["parts"][0]
                ["text"]
                .strip()
            )

            history.append(
                {
                    "role": "model",
                    "parts": [
                        {
                            "text": answer
                        }
                    ]
                }
            )

            return answer


        except Exception:
            time.sleep(1)


    return "AI সার্ভারে সমস্যা হয়েছে।"
