package com.mubexa.ai.core


class GeminiProvider : AIProvider {


    override fun ask(
        prompt: String
    ): String {


        return "Gemini AI: $prompt"

    }


}
