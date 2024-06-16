from aiogram import Bot, Dispatcher
from app.config import settings
from app.bot.handlers import start, clear, help, rag_response

# Initialize bot and dispatcher
bot = Bot(token=settings.bot_token)
dp = Dispatcher(bot)

# Include all routers
dp.include_router(start.router)
dp.include_router(clear.router)
dp.include_router(help.router)
dp.include_router(rag_response.router)

class Reference:
    def __init__(self) -> None:
        self.response = ""

reference = Reference()

def clear_past():
    reference.response = ""