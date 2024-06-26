import os
import openai
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

messages = [{"role": "system", "content": "You are an ordinary conversationalist"}]

async def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response.choices[0].message['content']
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hello! I am your personal assistant. You can ask me anything.')

async def handle_message(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text
    response = await CustomChatGPT(user_input)
    await update.message.reply_text(response)

def main() -> None:
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    
    application = Application.builder().token(token).build()

    # command and message handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling() # launch

if __name__ == '__main__':
    main()
