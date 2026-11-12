import json
import os


MEMORY_FILE = "long_memory.json"



def load_long_memory():

    if not os.path.exists(MEMORY_FILE):

        return []


    try:

        with open(
            MEMORY_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

            # পুরোনো format হলে নতুন format এ নেওয়া
            if data and isinstance(data[0], str):

                data = [
                    {
                        "text": item,
                        "category": "general"
                    }
                    for item in data
                ]

            return data


    except Exception:

        return []



def save_long_memory(data):

    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=4
        )



def add_memory(text, category="general"):

    memories = load_long_memory()


    for memory in memories:

        if memory["text"] == text:

            return False


    item = {
        "text": text,
        "category": category
    }


    memories.append(item)

    save_long_memory(memories)

    return True



def get_memories():

    return load_long_memory()



def delete_memory(text):

    memories = load_long_memory()


    new_memories = []


    for memory in memories:

        saved_text = memory["text"]


        if (
            text in saved_text
            or saved_text in text
        ):

            continue


        new_memories.append(memory)



    save_long_memory(new_memories)

    return True
