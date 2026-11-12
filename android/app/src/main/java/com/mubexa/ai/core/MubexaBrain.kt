package com.mubexa.ai.core

class MubexaBrain(
    private val memory: MemoryManager
) {


    fun think(input: String): String {

        val text = input.lowercase()


        return when {


            text.contains("আমার নাম") -> {

                val name =
                    input.replace(
                        "আমার নাম",
                        ""
                    ).trim()

                memory.save(
                    "name",
                    name
                )

                "ঠিক আছে, আমি মনে রাখলাম আপনার নাম $name"

            }


            text.contains("আমার নাম কি") -> {

                val name =
                    memory.get("name")

                if(name != null)
                    "আপনার নাম $name"
                else
                    "আমি এখনো আপনার নাম জানি না"

            }


            text.contains("তোমার নাম") -> {

                "আমার নাম Mubexa AI"

            }


            text.contains("হ্যালো") ||
            text.contains("হাই") -> {

                "হ্যালো, আমি Mubexa AI"

            }


            else -> {

                "আমি বুঝেছি: $input"

            }

        }

    }

}
