import asyncio
from aiogram.client.default import DefaultBotProperties
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from app.config import *
from app.service.rag_response_generator import generate_rag_response

# Initialize the Dispatcher
dp = Dispatcher()

# Command handler for '/start'
@dp.message(CommandStart())
async def welcome(message: Message):
    await message.answer("Hello! \nI'm an AI-powered Telegram bot created by Mohammad!\nHow may I help you with your queries related to the BERT paper?")

# Default message handler
@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Handler to generate a response using RAG (Retrieval-Augmented Generation).
    """
    try:
        # # Generate response based on user input
        response = generate_rag_response(message.text)
        await message.answer(response)
    except TypeError:
        # Handle unsupported message types
        await message.answer("Sorry, I can't process that request.")

async def main() -> None:
    # Initialize the Bot instance with default bot properties
    bot = Bot(token=bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # Start polling for incoming messages
    await dp.start_polling(bot)

# Entry point for Vercel
handler = dp 

if __name__ == "__main__":
    # Run the main coroutine
    asyncio.run(main())
