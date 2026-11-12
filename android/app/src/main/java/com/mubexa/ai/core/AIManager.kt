package com.mubexa.ai.core

enum class AIModel {

    GEMINI,
    CHATGPT,
    CLAUDE,
    AUTO

}


class AIManager {


    private var currentModel =
        AIModel.AUTO



    fun setModel(
        model: AIModel
    ) {

        currentModel = model

    }



    fun getModel(): AIModel {

        return currentModel

    }



    fun ask(
        prompt: String
    ): String {


        return when(currentModel) {


            AIModel.GEMINI -> {

                "Gemini থেকে উত্তর আসবে: $prompt"

            }


            AIModel.CHATGPT -> {

                "ChatGPT থেকে উত্তর আসবে: $prompt"

            }


            AIModel.CLAUDE -> {

                "Claude থেকে উত্তর আসবে: $prompt"

            }


            AIModel.AUTO -> {

                "Auto mode: সেরা AI নির্বাচন করা হবে"

            }


        }


    }


}

