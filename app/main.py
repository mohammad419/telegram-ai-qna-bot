from config import settings
import asyncio
import logging
import sys
from os import getenv
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from service.rag_response_generator import generate_rag_response

dp = Dispatcher()

@dp.message(CommandStart())
async def welcome(message: Message):
    await message.answer("Hello! \nI'm AI Powered Telegram bot created by Mohammad!\nHow may I help you with your queries related to BERT paper?")

@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        response = generate_rag_response(message.text)
        await message.answer(response)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")

async def main() -> None:
    # # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=settings.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # # Include all routers
    # dp.include_router(start.router)
    # dp.include_router(clear.router)
    # dp.include_router(help.router)
    # dp.include_router(rag_response.router)

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
