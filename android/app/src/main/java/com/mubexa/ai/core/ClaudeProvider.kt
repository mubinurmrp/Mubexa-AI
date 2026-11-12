package com.mubexa.ai.core


class ClaudeProvider : AIProvider {


    override fun ask(
        prompt: String
    ): String {


        return "Claude AI: $prompt"

    }


}
