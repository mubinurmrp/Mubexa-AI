import json
import os


MEMORY_FILE = "memory.json"


def load_memory():

    if not os.path.exists(MEMORY_FILE):
        return {}

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except Exception:
        return {}



def save_memory(data):

    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=4
        )



def remember(key, value):

    data = load_memory()

    data[key] = value

    save_memory(data)



def recall(key):

    data = load_memory()

    return data.get(key)
def set_state(key, value):

    data = load_memory()

    data["_state_" + key] = value

    save_memory(data)



def get_state(key):

    data = load_memory()

    return data.get("_state_" + key)



def clear_state(key):

    data = load_memory()

    if "_state_" + key in data:
        del data["_state_" + key]

    save_memory(data)
