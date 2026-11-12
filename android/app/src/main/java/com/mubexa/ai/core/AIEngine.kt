package com.mubexa.ai.core

class AIEngine {


    fun generateResponse(
        input: String,
        memory: MemoryManager
    ): String {


        val text = input.lowercase()



        // User memory
        if (
            text.contains("আমার নাম")
        ) {

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



        // Ask user name
        if (
            text.contains("আমার নাম কি") ||
            text.contains("আমার নাম কী")
        ) {


            val name =
                memory.get(
                    "user_name"
                )


            return if(name != null) {

                "আপনার নাম $name"

            } else {

                "আমি এখনো আপনার নাম জানি না"

            }

        }



        // Mubexa identity
        if (
            text.contains("তোমার নাম") ||
            text.contains("তুমি কে")
        ) {

            return "আমি Mubexa AI, আপনার ব্যক্তিগত AI assistant"

        }



        // Greetings
        if (
            text.contains("হ্যালো") ||
            text.contains("হাই") ||
            text.contains("hello")
        ) {

            return "হ্যালো! আমি Mubexa AI। কিভাবে সাহায্য করতে পারি?"

        }



        // Feelings conversation
        if (
            text.contains("ভালো নেই") ||
            text.contains("মন খারাপ")
        ) {

            return "আমি দুঃখিত। কী হয়েছে বলুন, আমি শুনছি।"

        }



        // Simple knowledge
        if (
            text.contains("বাংলাদেশের রাজধানী")
        ) {

            return "বাংলাদেশের রাজধানী ঢাকা।"

        }



        // Default response

        return "আমি বুঝেছি আপনি বলেছেন: $input। আরো ভালো উত্তর দেওয়ার জন্য আমার AI Engine উন্নত করা হচ্ছে।"

    }

}
