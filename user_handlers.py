from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

user_router = Router()

@user_router.message(Command("start"))
async def start(message: Message):
    # DB se banner aur welcome message fetch karein
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🛒 Shop", callback_data="shop")],
        [InlineKeyboardButton(text="💬 Support", url="https://t.me/your_support")]
    ])
    await message.answer_photo(photo="https://via.placeholder.com/600x300", 
                               caption="Welcome to our store! Select an option below.", 
                               reply_markup=kb)
  
