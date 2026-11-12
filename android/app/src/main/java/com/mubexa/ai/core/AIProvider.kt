package com.mubexa.ai.core

interface AIProvider {

    fun ask(
        prompt: String
    ): String

}
