
# Chat-Bot Project

This project consists of two different implementations of a Chat-Bot using OpenAI's GPT-3.5-turbo model. One implementation is a web-based chat interface using Gradio, and the other is a Telegram bot.

## Project Files

- **chatgpt_assistant_website.py**: A web-based chat interface using Gradio.
- **tg_chatbot.py**: A Telegram bot for chatting.
- **LICENSE**: MIT License.
- **screenshots**: A directory containing screenshots of examples of the bots in action.

## chatgpt_assistant_website.py

This script creates a web-based chat interface using Gradio, which allows users to interact with the Chat-GPT model.

### Requirements

- `os`
- `openai`
- `dotenv`
- `gradio`

### Setup

1. Install the required packages:
    ```bash
    pip install openai python-dotenv gradio
    ```
2. Set up your OpenAI API key in a `.env` file:
    ```plaintext
    OPENAI_API_KEY=your_openai_api_key_here
    ```

### Usage

Run the script:
```bash
python chatgpt_assistant_website.py
```

This will launch a Gradio interface that you can use to chat with the bot.

## tg_chatbot.py

This script sets up a Telegram bot that interacts with the Chat-GPT model.

### Requirements

- `os`
- `openai`
- `dotenv`
- `python-telegram-bot`

### Setup

1. Install the required packages:
    ```bash
    pip install openai python-dotenv python-telegram-bot
    ```
2. Set up your OpenAI API key and Telegram Bot Token in a `.env` file:
    ```plaintext
    OPENAI_API_KEY=your_openai_api_key_here
    TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
    ```

### Usage

Run the script:
```bash
python tg_chatbot.py
```

This will launch the Telegram bot, which you can interact with by sending messages to your bot on Telegram.

## Screenshots

- **chatbot_website.png**: Screenshot of the web-based chat interface.
- **telegram_chatbot.png**: Screenshot of the Telegram bot interface.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
