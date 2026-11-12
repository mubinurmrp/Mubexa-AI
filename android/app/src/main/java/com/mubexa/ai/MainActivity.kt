package com.mubexa.ai

import android.Manifest
import android.content.pm.PackageManager
import android.os.Bundle
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
import androidx.core.content.ContextCompat
import com.mubexa.ai.core.MemoryManager
import com.mubexa.ai.core.MubexaBrain
import com.mubexa.ai.core.VoiceManager
import com.mubexa.ai.ui.theme.MubexaTheme


class MainActivity : ComponentActivity() {


    private lateinit var voiceManager: VoiceManager


    override fun onCreate(savedInstanceState: Bundle?) {

        super.onCreate(savedInstanceState)


        // Microphone permission

        if (
            ContextCompat.checkSelfPermission(
                this,
                Manifest.permission.RECORD_AUDIO
            ) != PackageManager.PERMISSION_GRANTED
        ) {

            ActivityCompat.requestPermissions(
                this,
                arrayOf(
                    Manifest.permission.RECORD_AUDIO
                ),
                100
            )

        }


        val memory =
            MemoryManager(this)


        val brain =
            MubexaBrain(memory)


        voiceManager =
            VoiceManager(
                this,
                brain
            )


        setContent {

            MubexaTheme {

                MubexaUI(
                    voiceManager
                )

            }

        }

    }

}



@Composable
fun MubexaUI(
    voiceManager: VoiceManager
) {


    var status by remember {

        mutableStateOf(
            "Mubexa অপেক্ষা করছে..."
        )

    }



    val infiniteTransition =
        rememberInfiniteTransition(
            label = "AI Core"
        )


    val pulse by infiniteTransition.animateFloat(

        initialValue = 1f,

        targetValue = 1.15f,

        animationSpec =
            infiniteRepeatable(
                animation =
                    tween(1200),
                repeatMode =
                    RepeatMode.Reverse
            ),

        label = "Pulse"

    )



    Surface(

        modifier =
            Modifier.fillMaxSize(),

        color =
            Color(0xFF050505)

    ) {


        Column(

            modifier =
                Modifier.fillMaxSize(),

            horizontalAlignment =
                Alignment.CenterHorizontally,

            verticalArrangement =
                Arrangement.Center

        ) {


            Text(

                text = "MUBEXA AI",

                color = Color.White,

                fontSize = 32.sp

            )


            Spacer(
                Modifier.height(50.dp)
            )


            Box(

                modifier =
                    Modifier
                        .size(
                            (160 * pulse).dp
                        )
                        .background(
                            Color(0xFF00E5FF),
                            CircleShape
                        ),

                contentAlignment =
                    Alignment.Center

            ) {

                Text(
                    text = "◉",
                    fontSize = 70.sp,
                    color = Color.Black
                )

            }


            Spacer(
                Modifier.height(30.dp)
            )


            Text(

                text = status,

                color = Color.LightGray,

                fontSize = 18.sp

            )


            Spacer(
                Modifier.height(40.dp)
            )


            Button(

                onClick = {

                    status =
                        "🎤 শুনছি..."


                    voiceManager.listen {

                        result ->

                        status =
                            "আপনি: $result"

                    }

                }

            ) {

                Text(
                    "🎤 কথা বলুন"
                )

            }

        }

    }

}
