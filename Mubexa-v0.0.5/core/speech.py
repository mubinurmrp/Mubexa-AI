import subprocess
from config import VOICE_LANG

from core.correction import correct_text
from core.smart_correct import smart_correct


def speak(text):

    if not text:
        return

    print("Mubexa:", text)

    try:
        subprocess.run(
            [
                "termux-tts-speak",
                "-l",
                VOICE_LANG,
                text
            ],
            timeout=30
        )

    except Exception:
        pass



def listen():

    print("🎤 শুনছি...")

    try:

        result = subprocess.run(
            [
                "termux-speech-to-text"
            ],
            capture_output=True,
            text=True,
            timeout=30
        )


        text = result.stdout.strip()


        if text:

            text = correct_text(text)

            text = smart_correct(text)

            print(
                "আপনি বলেছেন:",
                text
            )


        return text


    except Exception:

        return ""



def wake_listen():

    return listen()

