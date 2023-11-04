import streamlit as st
import openai


openai.api_key = "************************"


functions = [
    {
        "name": "get_current_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city and state, e.g. San Francisco, CA",
                },
                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
            },
            "required": ["location"],
        },
    }
]

messages = []

# Streamlit app
st.title("OpenAI Chatbot")

user_input = st.text_input("You:", "")
if user_input:
    messages.append({"role": "user", "content": user_input})
    st.text("Chatbot is typing...")
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        functions=functions,
        function_call="auto",
    )
    bot_response = completion["choices"][0]["message"]["content"]
    st.text("Chatbot: " + bot_response)
