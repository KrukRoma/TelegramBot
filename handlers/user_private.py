from aiogram import types, Router
from aiogram.filters import CommandStart, Command
import random

user_private_router = Router()

@user_private_router.message(CommandStart())
async def start_cmd(message:types.Message):
    await message.answer('Hello, I`m a your personal bot')

@user_private_router.message(Command("menu"))
async def menu_cmd(message:types.Message):
    await message.answer('Menu :\n1. /menu\n 2. /help\n 3. /echo\n 4. /start\n')

@user_private_router.message(Command("help"))
async def help_cmd(message:types.Message):
    await message.answer('Hello! My name is Roman. This is my Chatbot.')

@user_private_router.message(Command("echo"))
async def echo_cmd(message:types.Message):
    user_text = message.text
    await message.answer(user_text)

    
