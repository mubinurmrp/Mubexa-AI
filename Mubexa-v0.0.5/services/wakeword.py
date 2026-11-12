from config import WAKE_WORDS
from core.speech import listen


def detect_wake_word(text):

    if not text:
        return False

    text = text.lower()

    for word in WAKE_WORDS:
        if word.lower() in text:
            return True

    return False


def wait_for_wake_word():

    while True:

        text = listen()

        if detect_wake_word(text):
            return True
