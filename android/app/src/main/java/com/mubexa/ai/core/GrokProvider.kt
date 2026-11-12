package com.mubexa.ai.core

class GrokProvider : AIProvider {


    override fun ask(
        prompt: String
    ): String {


        // এখানে পরে Grok API যুক্ত হবে

        return "Grok থেকে উত্তর আসবে: $prompt"

    }

}
