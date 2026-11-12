package com.mubexa.ai;

import android.app.Activity;
import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;
import android.view.View;


public class MainActivity extends Activity {


    TextView status;
    TextView aiCore;
    Button voiceButton;


    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_main);


        status = findViewById(R.id.status);

        aiCore = findViewById(R.id.ai_core);

        voiceButton = findViewById(R.id.voice_button);



        voiceButton.setOnClickListener(
            new View.OnClickListener() {

                @Override
                public void onClick(View v) {

                    status.setText(
                        "🎤 শুনছি..."
                    );


                    aiCore.setText(
                        "◉"
                    );

                }

            }
        );


    }

}
