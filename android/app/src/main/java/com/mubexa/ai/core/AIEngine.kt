package com.mubexa.ai.core


class AIEngine {


    private val aiManager =
        AIManager()



    fun generateResponse(
        input: String,
        memory: MemoryManager
    ): String {


        val text =
            input.lowercase()



        // নাম মনে রাখা

        if(text.contains("আমার নাম")) {


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



        // নাম জিজ্ঞেস করা

        if(
            text.contains("আমার নাম কি") ||
            text.contains("আমার নাম কী")
        ) {


            val name =
                memory.get(
                    "user_name"
                )


            if(name != null){

                return "আপনার নাম $name"

            }

        }



        // Basic identity

        if(
            text.contains("তোমার নাম") ||
            text.contains("তুমি কে")
        ){

            return "আমি Mubexa AI, আপনার ব্যক্তিগত AI assistant"

        }



        // অন্য সব প্রশ্ন AI Manager এ যাবে

        return aiManager.ask(
            input
        )


    }


}
