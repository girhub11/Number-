import asyncio
import os
from aiogram import Bot, Dispatcher
from database import init_db
from admin import admin_router

async def main():
    await init_db()
    bot = Bot(token=os.getenv("BOT_TOKEN"))
    dp = Dispatcher()
    dp.include_router(admin_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(asyncio.run(main()))
  
