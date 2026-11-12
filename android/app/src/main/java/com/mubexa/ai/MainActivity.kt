package com.mubexa.ai

import android.Manifest
import android.content.Intent
import android.os.Bundle
import android.speech.RecognitionListener
import android.speech.RecognizerIntent
import android.speech.SpeechRecognizer
import android.speech.tts.TextToSpeech
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.animation.core.*
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.core.app.ActivityCompat
import com.mubexa.ai.ui.theme.MubexaTheme
import java.util.Locale

class MainActivity : ComponentActivity() {

    private lateinit var speechRecognizer: SpeechRecognizer
    private lateinit var textToSpeech: TextToSpeech

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        ActivityCompat.requestPermissions(
            this,
            arrayOf(Manifest.permission.RECORD_AUDIO),
            1
        )

        textToSpeech = TextToSpeech(this) {
            textToSpeech.language = Locale("bn", "BD")
        }

        speechRecognizer = SpeechRecognizer.createSpeechRecognizer(this)

        setContent {

            MubexaTheme {
                MubexaUI(
                    startListening = {
                        listen()
                    }
                )
            }

        }
    }


    private fun listen() {

        val intent = Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH)

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

                override fun onResults(results: Bundle?) {

                    val text =
                        results?.getStringArrayList(
                            SpeechRecognizer.RESULTS_RECOGNITION
                        )?.get(0)

                    speak("আপনি বলেছেন $text")
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


    private fun speak(text: String) {

        textToSpeech.speak(
            text,
            TextToSpeech.QUEUE_FLUSH,
            null,
            "Mubexa"
        )
    }


    override fun onDestroy() {

        speechRecognizer.destroy()
        textToSpeech.shutdown()

        super.onDestroy()
    }

}



@Composable
fun MubexaUI(
    startListening: () -> Unit
) {

    var status by remember {
        mutableStateOf("Mubexa অপেক্ষা করছে...")
    }


    val infiniteTransition =
        rememberInfiniteTransition(label = "AI Core")


    val pulse by infiniteTransition.animateFloat(
        initialValue = 1f,
        targetValue = 1.15f,
        animationSpec = infiniteRepeatable(
            animation = tween(1200),
            repeatMode = RepeatMode.Reverse
        ),
        label = "Pulse"
    )


    Surface(
        modifier = Modifier.fillMaxSize(),
        color = Color(0xFF050505)
    ) {


        Column(
            modifier = Modifier.fillMaxSize(),
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.Center
        ) {


            Text(
                text = "MUBEXA AI",
                color = Color.White,
                fontSize = 32.sp
            )


            Spacer(
                modifier = Modifier.height(50.dp)
            )


            Box(
                modifier =
                Modifier
                    .size((160 * pulse).dp)
                    .background(
                        Color(0xFF00E5FF),
                        CircleShape
                    ),
                contentAlignment = Alignment.Center
            ) {

                Text(
                    text = "◉",
                    fontSize = 70.sp,
                    color = Color.Black
                )

            }


            Spacer(
                modifier = Modifier.height(30.dp)
            )


            Text(
                text = status,
                color = Color.LightGray,
                fontSize = 18.sp
            )


            Spacer(
                modifier = Modifier.height(40.dp)
            )


            Button(
                onClick = {

                    status = "🎤 শুনছি..."

                    startListening()

                }
            ) {

                Text(
                    text = "🎤 কথা বলুন"
                )

            }

        }

    }

}
