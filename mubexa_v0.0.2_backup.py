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

