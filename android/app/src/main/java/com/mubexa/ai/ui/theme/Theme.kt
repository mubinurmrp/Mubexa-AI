package com.mubexa.ai.ui.theme

import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.darkColorScheme
import androidx.compose.runtime.Composable


private val MubexaDarkColors = darkColorScheme()


@Composable
fun MubexaTheme(
    content: @Composable () -> Unit
) {

    MaterialTheme(
        colorScheme = MubexaDarkColors,
        content = content
    )

}
