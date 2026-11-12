def detect_intent(text):

    if not text:
        return None


    text = text.lower()


    # নাম জানতে চাওয়া
    if any(word in text for word in [
        "তোমার নাম",
        "তুমি কে",
        "নাম কী",
        "নাম বল",
        "পরিচয়"
    ]):
        return "ASK_NAME"


    # সময় জানতে চাওয়া
    if any(word in text for word in [
        "সময়",
        "কয়টা বাজে",
        "কয়টা বাজে",
        "time"
    ]):
        return "ASK_TIME"


    # বয়স জানতে চাওয়া
    if any(word in text for word in [
        "বয়স",
        "বয়স",
        "age"
    ]):
        return "ASK_AGE"


    return None

