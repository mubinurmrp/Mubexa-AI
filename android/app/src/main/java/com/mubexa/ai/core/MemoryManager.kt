package com.mubexa.ai.core

import android.content.Context

class MemoryManager(context: Context) {

    private val prefs =
        context.getSharedPreferences(
            "mubexa_memory",
            Context.MODE_PRIVATE
        )


    fun save(key: String, value: String) {

        prefs.edit()
            .putString(key, value)
            .apply()

    }


    fun get(key: String): String? {

        return prefs.getString(key, null)

    }


    fun clear() {

        prefs.edit()
            .clear()
            .apply()

    }

}
