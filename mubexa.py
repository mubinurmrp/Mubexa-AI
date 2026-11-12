import json
import os

memory_file = "memory.json"

# Memory load
if os.path.exists(memory_file):
    with open(memory_file, "r", encoding="utf-8") as f:
        memory = json.load(f)
else:
    memory = {}

print("Mubexa AI 🤖")
print("আমি বাংলা ভাষায় আপনার সহকারী।")

if "name" in memory:
    print(f"স্বাগতম {memory['name']} 🤖")

print("বন্ধ করতে 'exit' লিখুন।\n")

while True:
    user = input("আপনি: ")

    if user.lower() == "exit":
        print("Mubexa: বিদায়! আবার কথা হবে 🤖")
        break

    if "আমার নাম" in user:
        name = user.replace("আমার নাম", "").strip()

        if name:
            memory["name"] = name

            with open(memory_file, "w", encoding="utf-8") as f:
                json.dump(memory, f, ensure_ascii=False, indent=4)

            print(f"Mubexa: ঠিক আছে, আমি মনে রাখলাম আপনার নাম {name}।")

    elif "তোমার নাম" in user:
        print("Mubexa: আমার নাম Mubexa AI 🤖")

    elif "কেমন" in user:
        print("Mubexa: আমি ভালো আছি। আপনার সাহায্য করার জন্য প্রস্তুত।")

    elif "কি মনে আছে" in user:
        if memory:
            print("Mubexa: আমার মনে আছে:")
            print(memory)
        else:
            print("Mubexa: এখনো কিছু মনে রাখা নেই।")

    else:
        print("Mubexa: আমি এখনো শিখছি। ধীরে ধীরে আরও বুদ্ধিমান হব।")
print("Mubexa AI 🤖")
print("আমি বাংলা ভাষায় আপনার সহকারী।")
print("বন্ধ করতে 'exit' লিখুন।\n")

while True:
    user = input("আপনি: ")

    if user.lower() == "exit":
        print("Mubexa: বিদায়! আবার কথা হবে 🤖")
        break

    if "নাম" in user:
        print("Mubexa: আমার নাম Mubexa AI 🤖")

    elif "কেমন" in user:
        print("Mubexa: আমি ভালো আছি। আপনার সাহায্য করার জন্য প্রস্তুত।")

    elif "হ্যালো" in user or "হাই" in user:
        print("Mubexa: হ্যালো! কিভাবে সাহায্য করতে পারি?")

    else:
        print("Mubexa: আমি এখনো শিখছি। ধীরে ধীরে আরও বুদ্ধিমান হব।")

