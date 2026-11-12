package com.mubexa.ai.core

class AIEngine {


    fun generateResponse(
        input: String,
        memory: MemoryManager
    ): String {


        val text = input.lowercase()



        // Memory save

        if (text.contains("আমার নাম")) {

            val name =
                input.replace(
                    "আমার নাম",
                    ""
                ).trim()


            if(name.isNotEmpty()) {

                memory.save(
                    "user_name",
                    name
                )


                return "ঠিক আছে, আমি মনে রাখলাম আপনার নাম $name"

            }

        }



        // Memory recall

        if (
            text.contains("আমার নাম কি") ||
            text.contains("আমার নাম কী")
        ) {


            val name =
                memory.get(
                    "user_name"
                )


            return if(name != null)
                "আপনার নাম $name"
            else
                "আমি এখনো আপনার নাম জানি না"

        }



        // Identity

        if (
            text.contains("তোমার নাম") ||
            text.contains("তুমি কে")
        ) {

            return "আমি Mubexa AI, আপনার ব্যক্তিগত AI assistant"

        }



        // Conversation

        if (
            text.contains("কেমন আছ")
        ) {

            return "আমি ভালো আছি। আপনার সাথে কথা বলতে প্রস্তুত।"

        }


        if (
            text.contains("ভালো নেই") ||
            text.contains("মন খারাপ")
        ) {

            return "আমি শুনছি। কী হয়েছে বলুন।"

        }



        // Knowledge

        if (
            text.contains("বাংলাদেশের রাজধানী")
        ) {

            return "বাংলাদেশের রাজধানী ঢাকা।"

        }



        // Future AI connection point

        return """
        আমি আপনার কথা বুঝেছি:
        $input
        
        আমার উন্নত AI Engine এখনো সংযুক্ত হচ্ছে।
        খুব শীঘ্রই আমি আরও বুদ্ধিমান উত্তর দিতে পারব।
        """.trimIndent()

    }

}
