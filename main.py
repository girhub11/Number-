import asyncio
from aiogram import Bot, Dispatcher
from database import init_db
from user_handlers import user_router
from admin_panel import admin_router

async def main():
    await init_db()
    bot = Bot(token="YOUR_BOT_TOKEN_HERE")
    dp = Dispatcher()
    
    dp.include_router(user_router)
    dp.include_router(admin_router)
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
