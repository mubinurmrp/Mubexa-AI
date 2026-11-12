package com.mubexa.ai.core


class OpenAIProvider : AIProvider {


    override fun ask(
        prompt: String
    ): String {


        return "ChatGPT AI: $prompt"

    }


}
