package com.mubexa.ai.core

import android.content.Context
import android.content.Intent
import android.os.Bundle
import android.speech.RecognitionListener
import android.speech.RecognizerIntent
import android.speech.SpeechRecognizer
import android.speech.tts.TextToSpeech
import java.util.Locale


class VoiceManager(
    private val context: Context,
    private val brain: MubexaBrain
) {


    private val speechRecognizer =
        SpeechRecognizer.createSpeechRecognizer(context)


    private lateinit var tts: TextToSpeech


    init {

        tts = TextToSpeech(context) {

            if (it == TextToSpeech.SUCCESS) {

                tts.language =
                    Locale("bn", "BD")

            }

        }

    }



    fun listen(
        onResult: (String) -> Unit
    ) {


        val intent =
            Intent(
                RecognizerIntent.ACTION_RECOGNIZE_SPEECH
            )


        intent.putExtra(
            RecognizerIntent.EXTRA_LANGUAGE_MODEL,
            RecognizerIntent.LANGUAGE_MODEL_FREE_FORM
        )


        intent.putExtra(
            RecognizerIntent.EXTRA_LANGUAGE,
            "bn-BD"
        )


        speechRecognizer.setRecognitionListener(

            object : RecognitionListener {


                override fun onResults(
                    results: Bundle?
                ) {


                    val text =
                        results
                            ?.getStringArrayList(
                                SpeechRecognizer.RESULTS_RECOGNITION
                            )
                            ?.firstOrNull()


                    if(text != null) {


                        onResult(text)


                        val answer =
                            brain.think(text)


                        speak(answer)

                    }

                }


                override fun onError(error: Int) {}

                override fun onReadyForSpeech(params: Bundle?) {}
                override fun onBeginningOfSpeech() {}
                override fun onRmsChanged(rmsdB: Float) {}
                override fun onBufferReceived(buffer: ByteArray?) {}
                override fun onEndOfSpeech() {}
                override fun onPartialResults(partialResults: Bundle?) {}
                override fun onEvent(eventType: Int, params: Bundle?) {}

            }

        )


        speechRecognizer.startListening(intent)

    }



    private fun speak(
        text: String
    ) {

        tts.speak(
            text,
            TextToSpeech.QUEUE_FLUSH,
            null,
            "Mubexa"
        )

    }

}
