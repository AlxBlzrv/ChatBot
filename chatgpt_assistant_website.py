import os
import openai
from dotenv import load_dotenv
import gradio as gr

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

messages = [{"role": "system", "content": "You are an ordinary conversationalist"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response.choices[0].message['content']
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gr.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="Hello! I'm your personal assistant, you can ask me anything...")

demo.launch(share=True)
