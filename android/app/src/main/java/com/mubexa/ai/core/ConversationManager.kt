package com.mubexa.ai.core

class ConversationManager {


    private val history =
        mutableListOf<String>()



    fun addUserMessage(
        message: String
    ) {

        history.add(
            "User: $message"
        )

    }



    fun addMubexaMessage(
        message: String
    ) {

        history.add(
            "Mubexa: $message"
        )

    }



    fun getHistory(): List<String> {

        return history

    }



    fun getLastMessage(): String? {

        return history.lastOrNull()

    }



    fun clear() {

        history.clear()

    }


}
