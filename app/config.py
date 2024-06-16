from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from openai import OpenAI
import os

# load_dotenv()  # Load environment variables from .env file

# class Settings(BaseSettings):
#     bot_token: str
#     openai_api_key: str
#     openai_assistant_id: str

#     class Config:
#         env_file = ".env"

# settings = Settings()

# class Reference:
#     def __init__(self) -> None:
#         self.response = ""

# reference = Reference()

# def clear_past():
#     reference.response = ""

#initializing open ai client
bot_token = os.getenv('BOT_TOKEN')
openai_api_key = os.getenv('OPENAI_API_KEY')
openai_assistant_id = os.getenv('OPENAI_ASSISTANT_ID')
openai_client = OpenAI(api_key=openai_api_key)
