from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

admin_router = Router()

@admin_router.message(Command("adminpanel"))
async def show_panel(message: Message):
    # Check Admin ID logic here
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🖼 Change Banner", callback_data="set_banner")],
        [InlineKeyboardButton(text="📦 Manage Stock", callback_data="manage_stock")],
        [InlineKeyboardButton(text="✨ Edit Emojis", callback_data="edit_emojis")]
    ])
    await message.answer("🛠 Admin Panel Control:", reply_markup=kb)
  
