import asyncio
import os
from aiogram import Bot, Dispatcher
from database import init_db
from user_handlers import user_router
from admin_panel import admin_router

# Environment Variables (Railway mein ye set hona chahiye)
TOKEN = os.getenv("BOT_TOKEN")

async def main():
    if not TOKEN:
        print("❌ Error: BOT_TOKEN is missing!")
        return
    
    await init_db()
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    
    dp.include_router(user_router)
    dp.include_router(admin_router)
    
    print("🚀 Bot is running successfully...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"❌ Critical Error: {e}")
        
