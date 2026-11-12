def correct_text(text):

    if not text:
        return ""

    text = text.lower().strip()


    corrections = {

        # Time
        "akon": "এখন",
        "akhn": "এখন",
        "ekhon": "এখন",
        "somo": "সময়",
        "samay": "সময়",
        "somoy": "সময়",
        "time": "সময়",
        "koto": "কত",

        # Question
        "ki": "কি",
        "kee": "কি",
        "koi": "কোথায়",
        "kaun": "কোন",
        "kon": "কোন",

        # Personal
        "amar": "আমার",
        "tomar": "তোমার",
        "tumar": "তোমার",
        "nam": "নাম",

        # Noise words from speech
        "show my": "",
        "account from my": "",
        "account for my": "",
        "phone": "",
        "photo": "",

        # Mubexa
        "mubexa": "mubexa",
        "mubesha": "mubexa",
        "mubiksa": "mubexa"
    }


    for wrong, correct in corrections.items():
        text = text.replace(
            wrong,
            correct
        )


    return text.strip()
