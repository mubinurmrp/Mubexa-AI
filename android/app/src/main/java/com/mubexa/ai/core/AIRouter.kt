package com.mubexa.ai.core


class AIRouter {


    fun selectAI(
        question: String
    ): AIModel {


        val text =
            question.lowercase()



        // Coding related questions
        if (
            text.contains("code") ||
            text.contains("kotlin") ||
            text.contains("java") ||
            text.contains("python") ||
            text.contains("program")
        ) {

            return AIModel.CHATGPT

        }



        // Image / vision related questions
        if (
            text.contains("image") ||
            text.contains("photo") ||
            text.contains("picture") ||
            text.contains("ছবি")
        ) {

            return AIModel.GEMINI

        }



        // Long analysis / documents
        if (
            question.length > 1000 ||
            text.contains("analyze") ||
            text.contains("বিশ্লেষণ")
        ) {

            return AIModel.CLAUDE

        }



        // General conversation
        return AIModel.AUTO


    }


}
