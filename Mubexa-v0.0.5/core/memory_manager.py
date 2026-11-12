from core.long_memory import add_memory


def get_category(text):

    if any(word in text for word in [
        "AI",
        "Mubexa",
        "প্রজেক্ট",
        "বানাচ্ছি"
    ]):

        return "project"



    if any(word in text for word in [
        "কাজ",
        "চাকরি",
        "Food",
        "Production"
    ]):

        return "work"



    if any(word in text for word in [
        "শিখছি",
        "শিখতে",
        "পছন্দ"
    ]):

        return "interest"



    return "general"



def should_remember(text):

    keywords = [
        "আমি বানাচ্ছি",
        "আমি কাজ করি",
        "আমি পড়ি",
        "আমার লক্ষ্য",
        "আমার পরিকল্পনা",
        "আমি শিখছি",
        "আমি ব্যবহার করি"
    ]


    for word in keywords:

        if word in text:

            return True


    return False



def process_memory(text):

    if should_remember(text):

        category = get_category(text)

        return add_memory(
            text,
            category
        )


    return False
