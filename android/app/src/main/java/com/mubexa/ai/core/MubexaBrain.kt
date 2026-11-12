package com.mubexa.ai.core

class MubexaBrain(
    private val memory: MemoryManager
) {


    private val aiEngine =
        AIEngine()


    private val conversation =
        ConversationManager()



    fun think(
        input: String
    ): String {


        // Save user message

        conversation.addUserMessage(
            input
        )



        // Generate answer

        val reply =
            aiEngine.generateResponse(
                input,
                memory
            )



        // Save Mubexa reply

        conversation.addMubexaMessage(
            reply
        )


        return reply

    }



    fun getConversation():
            List<String> {

        return conversation.getHistory()

    }


}
