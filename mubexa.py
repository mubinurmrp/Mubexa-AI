import json
import os
import random

memory_file = "memory.json"

if os.path.exists(memory_file):
    with open(memory_file, "r", encoding="utf-8") as f:
        memory = json.load(f)
else:
    memory = {}

print("Mubexa AI 🤖")
print("আমি বাংলা ভাষায় আপনার সহকারী।")

if "নাম" in memory:
    print(f"স্বাগতম {memory['নাম']} 🤖")

print("বন্ধ করতে 'exit' লিখুন।\n")

responses = {
    "হ্যালো": "হ্যালো! কিভাবে সাহায্য করতে পারি? 😊",
    "হাই": "হাই! আমি Mubexa AI 🤖",
    "কেমন": "আমি ভালো আছি। আপনার সাহায্যের জন্য প্রস্তুত।",
    "ধন্যবাদ": "আপনাকে স্বাগতম। 😊",
    "কি করছো": "আমি আপনার সাথে কথা বলছি এবং শিখছি।"
}

while True:
    user = input("আপনি: ")

    if user.lower() == "exit":
        print("Mubexa: বিদায়! আবার কথা হবে 🤖")
        break

    if "আমার নাম" in user:
        name = user.replace("আমার নাম", "").strip()
        memory["নাম"] = name
        print(f"Mubexa: আপনার নাম {name} মনে রাখলাম।")

    elif "আমার বয়স" in user or "আমার বয়স" in user:
        age = user.replace("আমার বয়স", "").replace("আমার বয়স", "").strip()
        memory["বয়স"] = age
        print(f"Mubexa: আপনার বয়স {age} মনে রাখলাম।")

    elif "আমার পছন্দ" in user:
        like = user.replace("আমার পছন্দ", "").strip()
        memory["পছন্দ"] = like
        print(f"Mubexa: আপনার পছন্দ {like} মনে রাখলাম।")

    elif "আমার সম্পর্কে বলো" in user or "কি মনে আছে" in user:
        print("Mubexa: আপনার সম্পর্কে আমার মনে আছে:")
        for k, v in memory.items():
            print(f"- {k}: {v}")

    else:
        found = False
        for key, value in responses.items():
            if key in user:
                print("Mubexa:", value)
                found = True
                break

        if not found:
            print("Mubexa: আমি এখনো শিখছি। 🤖")

    with open(memory_file, "w", encoding="utf-8") as f:
        json.dump(memory, f, ensure_ascii=False, indent=4)
