from core.speech import speak, listen
from core.commands import run_command
from core.offline import offline_command
from core.memory import remember
from ai.gemini import ask_ai
from services.wakeword import wait_for_wake_word



def process(user):

    # Command Router
    command_reply = run_command(user)

    if command_reply:
        return command_reply


    # নাম মনে রাখা
    if "আমার নাম" in user:

        name = user.split("আমার নাম")[-1].strip()

        if name:
            remember("নাম", name)

            return (
                f"ঠিক আছে, আমি মনে রাখলাম আপনার নাম {name}"
            )


    # Offline command
    reply = offline_command(user)

    if reply:
        return reply


    # AI
    return ask_ai(user)




def main():

    speak("Mubexa চালু হয়েছে।")


    while True:

        print("\nMubexa অপেক্ষা করছে...")


        wait_for_wake_word()


        speak("জ্বি, বলুন।")


        user = listen()


        if not user:
            continue


        print("আপনি বলেছেন:", user)


        answer = process(user)


        speak(answer)



if __name__ == "__main__":
    main()

