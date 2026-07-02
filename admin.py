from aiogram import Router, F
from aiogram.types import Message
from database import add_stock_db
import os

admin_router = Router()

@admin_router.message(F.text == "/panel")
async def admin_panel(message: Message):
    if str(message.from_user.id) == os.getenv("ADMIN_ID"):
        await message.answer("Admin Panel\nOptions: \n1. /add_stock [platform] [cat] [data]")
    else:
        await message.answer("Access Denied!")

@admin_router.message(F.text.startswith("/add_stock"))
async def add_stock_cmd(message: Message):
    # Format: /add_stock Telegram 2014 user:pass
    parts = message.text.split(" ", 3)
    await add_stock_db(parts[1], parts[2], parts[3])
    await message.answer(f"Added {parts[3]} to {parts[1]} {parts[2]}")
                      
