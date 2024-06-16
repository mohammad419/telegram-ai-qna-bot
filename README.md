
# RAG Powered Telegram Bot

This project contains the implementation of a Telegram bot that uses the OpenAI Assistant API to generate responses to user messages. The bot is built using `aiogram` for Telegram bot functionality and `openai` for generating responses.

## Features

- Responds to user messages using OpenAI Assistant's GPT-3.5-turbo model.
- Handles commands like `/start`, `/clear`, and `/help`.
- Modular design with handlers separated into different files for easy maintenance.
- Uses OpenAI Assistant RAG (Retrieval-Augmented Generation) for Document QnA.

## Prerequisites

- Python 3.8+
- A Telegram bot token from [BotFather](https://t.me/BotFather).
- An OpenAI API key from [OpenAI](https://openai.com/).

## Project Structure

```
rag_telegram_bot/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── bot/
│   │   ├── __init__.py
│   │   ├── bot.py
│   │   ├── handlers/
│   │   │   ├── __init__.py
│   │   │   ├── start.py
│   │   │   ├── clear.py
│   │   │   ├── help.py
│   │   │   ├── chatgpt.py
│   └── services/
│       ├── __init__.py
│       ├── rag_service.py
│       └── response_generator.py
├── requirements.txt
├── .env
└── README.md
```

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/rag_telegram_bot.git
cd rag_telegram_bot
```

2. **Create a virtual environment and activate it:**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install the required packages:**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables:**

Create a `.env` file in the root directory and add the following:

```env
OPENAI_API_KEY=your-openai-api-key
BOT_TOKEN=your-telegram-bot-token
```

## Usage

Run the bot:

```bash
python -m app.main
```

## Handlers

The bot has several handlers to manage different commands and messages:

- **Start Handler (`start.py`):** Welcomes the user and clears past conversation context.
- **Clear Handler (`clear.py`):** Clears the previous conversation and context.
- **Help Handler (`help.py`):** Provides a help menu with available commands.
- **RAG QnA Handler (`chatgpt.py`):** Processes the user's input and generates a response using OpenAI Assistant RAG (Retrieval-Augmented Generation) for Document QnA.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [aiogram](https://github.com/aiogram/aiogram) for Telegram bot functionality.
- [OpenAI Assistant]([https://openai.com/](https://platform.openai.com/docs/assistants/overview)) for the RAG Application for Document QnA.

## Contact

Author: Mohammad Arif
