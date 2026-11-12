package com.mubexa.ai.core


class GeminiClient : AIProvider {


    override fun ask(
        prompt: String
    ): String {


        // এখানে পরে Gemini API যুক্ত হবে


        return "AI উত্তর প্রস্তুত হচ্ছে: $prompt"

    }


}
