package com.example.yemenionyx

import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity // Ensure this import is correct
import android.util.Log

class MainActivity : AppCompatActivity() {
    private external fun checkInput(input: String): Boolean

    override fun onCreate(savedInstanceState: Bundle?) {
        setTheme(R.style.Theme_YemeniOnyx)
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val editText: EditText = findViewById(R.id.editText)
        val button: Button = findViewById(R.id.button)
        val textView: TextView = findViewById(R.id.textView)

        button.setOnClickListener { v: View? ->
            try {
                val userInput = editText.text.toString()
                val result = checkInput(userInput)
                textView.text = if (result) "Password is correct!" else "Password is incorrect."
            } catch (e: Exception) {
                textView.text = "An error occurred: ${e.message}"
            }
        }
    }


    companion object {
        init {
            System.loadLibrary("yemenionyx") // Load the .so file
        }
    }
}
