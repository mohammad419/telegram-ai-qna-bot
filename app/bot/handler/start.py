from aiogram.types import Message
from aiogram.filters import CommandStart

@dp.message(CommandStart())
async def welcome(message: Message):
    await message.answer("Hello! \nI'm AI Powered Telegram bot created by Mohammad!\nHow may I help you with your queries related to BERT paper?")
