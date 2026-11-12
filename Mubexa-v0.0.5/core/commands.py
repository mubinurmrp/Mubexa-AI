import datetime

from core.intent import detect_intent

from core.memory import (
    remember,
    recall,
    set_state,
    get_state,
    clear_state
)

from core.profile import (
    get_all_profile,
    save_profile
)

from core.long_memory import (
    get_memories,
    delete_memory
)

from core.memory_manager import (
    process_memory
)


def run_command(text):

    if not text:
        return None


    text = text.strip()



    # Memory ভুলে যাও
    if "ভুলে যাও" in text:

        memory_text = (
            text
            .replace("ভুলে যাও", "")
            .replace("এই তথ্যটা", "")
            .strip()
        )


        if memory_text:

            delete_memory(memory_text)

            return (
                f"ঠিক আছে, আমি {memory_text} ভুলে গেছি।"
            )


        return "কোন তথ্য ভুলে যেতে হবে বলুন।"



    # Memory দেখা
    if any(word in text for word in [
        "আমার মেমোরি",
        "আমার মনে রাখা তথ্য",
        "কি কি মনে আছে",
        "কী কী মনে আছে"
    ]):

        memories = get_memories()

        if memories:

            result = "আমি মনে রেখেছি: "

            for memory in memories:

                result += (
                    f"{memory['text']} "
                    f"({memory['category']}), "
                )

            return result


        return "এখনো কোনো তথ্য মনে রাখা নেই।"



    # Profile দেখা
    if any(word in text for word in [
        "আমার সম্পর্কে",
        "আমাকে সম্পর্কে",
        "আমার তথ্য",
        "আমার ব্যাপারে"
    ]):

        profile = get_all_profile()

        if profile:

            result = "আমি আপনার সম্পর্কে জানি: "

            for key, value in profile.items():

                result += f"{key} {value}, "

            return result


        return "আমি এখনো আপনার সম্পর্কে কোনো তথ্য জানি না।"



    # Smart Memory
    process_memory(text)



    # Waiting state
    state = get_state("waiting")


    if state:

        value = text.strip()

        if value:

            save_profile(
                state,
                value
            )

            clear_state("waiting")

            return (
                f"ঠিক আছে, আমি মনে রাখলাম। {value}"
            )



    # বয়স
    if "আমার বয়স" in text or "আমার বয়স" in text:

        value = (
            text
            .replace("আমার বয়স", "")
            .replace("আমার বয়স", "")
            .strip()
        )


        if value:

            save_profile(
                "age",
                value
            )

            return (
                f"ঠিক আছে, আমি আপনার বয়স {value} মনে রাখলাম।"
            )


        set_state(
            "waiting",
            "age"
        )

        return "আপনার বয়স কত?"



    # পছন্দ
    if "আমার পছন্দ" in text:

        value = text.replace(
            "আমার পছন্দ",
            ""
        ).strip()


        if value:

            save_profile(
                "like",
                value
            )

            return (
                f"ঠিক আছে, আমি আপনার পছন্দ {value} মনে রাখলাম।"
            )


        set_state(
            "waiting",
            "like"
        )

        return "আপনার পছন্দ কী?"



    # নাম
    if text.startswith("আমার নাম"):

        name = text.replace(
            "আমার নাম",
            ""
        ).strip()


        if name:

            remember(
                "name",
                name
            )

            save_profile(
                "name",
                name
            )

            return (
                f"ঠিক আছে, আমি মনে রাখলাম। "
                f"আপনার নাম {name}।"
            )


        set_state(
            "waiting",
            "name"
        )

        return "আপনার নাম কী?"



    intent = detect_intent(text)



    if intent == "ASK_NAME":

        name = recall("name")

        if name:

            return f"আপনার নাম {name}।"

        return "আমি এখনো আপনার নাম জানি না।"



    if intent == "ASK_TIME":

        now = datetime.datetime.now()

        return (
            f"এখন সময় {now.strftime('%I:%M %p')}"
        )



    return None
