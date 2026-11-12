package com.mubexa.ai

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
import com.mubexa.ai.ui.theme.MubexaTheme


class MainActivity : ComponentActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContent {

            MubexaTheme {

                MubexaUI()

            }

        }
    }
}


@Composable
fun MubexaUI() {

    var status by remember {

        mutableStateOf("Mubexa অপেক্ষা করছে...")

    }


    val infiniteTransition = rememberInfiniteTransition(
        label = "AI Core"
    )


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

                modifier = Modifier

                    .size((160 * pulse).dp)

                    .background(

                        color = Color(0xFF00E5FF),

                        shape = CircleShape

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

                }

            ) {


                Text(

                    text = "🎤 কথা বলুন"

                )

            }

        }

    }

}
