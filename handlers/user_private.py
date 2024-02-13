from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
from filters.chat_types import ChatTypeFilter
from Api.api import get_random_duck, get_random_cat, get_random_dog, get_random_clearbit, get_random_photo, get_chatGPT_response
user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(["private"]))
@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Hello, I`m a your personal bot')

@user_private_router.message(Command("menu"))
async def menu_cmd(message: types.Message):
    await message.answer('Menu :\n1. /menu\n2. /help\n3. /echo\n4. /start\n')

@user_private_router.message(Command("help"))
async def help_cmd(message: types.Message):
    await message.answer('Hello! My name is Roman. This is my Chatbot.')

@user_private_router.message(Command("echo"))
async def echo_cmd(message:types.Message):
    await message.answer(message.text)

@user_private_router.message((F.photo) | F.text.contains("кажі") | (F.audio) | (F.sticker))
async def photo_mess(message:types.Message):
    await message.answer("I understand that it`s photo by I can`t explain it")

@user_private_router.message(Command('duck'))
async def duck_cmd(message:types.Message):
    await message.answer_photo(get_random_duck())

@user_private_router.message(Command('cat'))
async def cat_cmd(message:types.Message):
    await message.answer_photo(get_random_cat())

@user_private_router.message(Command('dog'))
async def dog_cmd(message:types.Message):
    await message.answer_photo(get_random_dog())

@user_private_router.message(Command('clearbit'))
async def clearbit_cmd(message:types.Message):
    await message.answer_photo(get_random_clearbit())

@user_private_router.message(Command('photo'))
async def photo_cmd(message:types.Message):
    await message.answer_photo(get_random_photo())

@user_private_router.message(Command('gpt'))
async def gpt_cmd(message:types.Message):
    answer = get_chatGPT_response(message.text[4:])
    await message.answer(message.chat.id, text=answer)

    
