from aiogram import types, Router
from app.config import settings
from app.service.rag_response_generator import generate_rag_response

router = Router()

class Reference:
    def __init__(self) -> None:
        self.response = ""

reference = Reference()

@dp.message()
async def chatgpt(message: types.Message):
    print(f">» USER: \n{message.text}")
    response = generate_rag_response(message.text)
    reference.response = response
    print(f">» chatGPT: \n{reference.response}")
    await message.answer(reference.response)
