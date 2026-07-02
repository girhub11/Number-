import aiosqlite

async def init_db():
    async with aiosqlite.connect("bot_data.db") as db:
        await db.execute("CREATE TABLE IF NOT EXISTS stock (id INTEGER PRIMARY KEY, platform TEXT, category TEXT, data TEXT, status TEXT)")
        await db.commit()

async def add_stock_db(platform, category, data):
    async with aiosqlite.connect("bot_data.db") as db:
        await db.execute("INSERT INTO stock (platform, category, data, status) VALUES (?, ?, ?, 'Ready')", (platform, category, data))
        await db.commit()
      
