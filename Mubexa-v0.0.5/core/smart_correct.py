from ai.gemini import ask_ai


def smart_correct(text):

    if not text:
        return ""

    prompt = f"""
তুমি একটি Speech Correction System।

নিচের কথাটি Speech-to-text থেকে এসেছে।
ভুল উচ্চারণ, Banglish বা ভুল শব্দ থাকতে পারে।

কাজ:
1. কথাটির আসল অর্থ বুঝো।
2. শুধুমাত্র পরিষ্কার বাংলা বাক্য লিখো।
3. কোনো ব্যাখ্যা দেবে না।

Input:
{text}

Corrected:
"""

    try:
        result = ask_ai(prompt)

        if result:
            return result.strip()

    except Exception:
        pass

    return text
