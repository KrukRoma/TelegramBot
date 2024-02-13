from aiogram import Router, types, F 
from aiogram.filters import Command
from filters.chat_types import ChatTypeFilter
from string import punctuation

user_group_router = Router()
user_group_router.message.filter(ChatTypeFilter(["group", 'supergroup']))

bad_words = {'bad', 'word', 'badword', 'bad_words'}

def clean_words(text:str):
    return text.translate(str.maketrans('', '', punctuation)).lower()

@user_group_router.edited_message()
@user_group_router.message()
async def check_words(message:types.Message):
    await message.reply(message.text)

@user_group_router.edited_message()
@user_group_router.message()
async def check_words(message:types.Message):
    if bad_words.intersection(message.text.lower().split()):
        await message.answer(f"{message.from_user.full_name} you are using bad words")
        await message.delete()