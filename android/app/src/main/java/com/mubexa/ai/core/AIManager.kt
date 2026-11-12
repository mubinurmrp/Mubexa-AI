package com.mubexa.ai.core


class AIManager {


    private val router =
        AIRouter()



    private val providers:
            Map<AIModel, AIProvider> =
        mapOf(

            AIModel.GEMINI to GeminiProvider(),

            AIModel.CHATGPT to OpenAIProvider(),

            AIModel.CLAUDE to ClaudeProvider(),

            AIModel.GROK to GrokProvider()

        )



    fun ask(
        prompt: String
    ): String {


        val selectedAI =
            router.selectAI(prompt)



        val finalAI =
            if(selectedAI == AIModel.AUTO) {

                AIModel.GEMINI

            } else {

                selectedAI

            }



        val provider =
            providers[finalAI]



        return if(provider != null) {

            provider.ask(prompt)

        } else {

            "কোন AI provider পাওয়া যায়নি"

        }

    }


}
