import json
import os


PROFILE_FILE = "data/profile.json"



def load_profile():

    if not os.path.exists(PROFILE_FILE):

        return {}


    try:

        with open(
            PROFILE_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except Exception:

        return {}



def save_profile(key, value):

    profile = load_profile()

    profile[key] = value


    os.makedirs(
        "data",
        exist_ok=True
    )


    with open(
        PROFILE_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            profile,
            file,
            ensure_ascii=False,
            indent=4
        )



def get_all_profile():

    return load_profile()
