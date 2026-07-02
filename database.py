import aiosqlite
async def init_db():
    async with aiosqlite.connect("store.db") as db:
        await db.execute("CREATE TABLE IF NOT EXISTS stocks (id INTEGER PRIMARY KEY, category TEXT, data TEXT, status TEXT)")
        await db.execute("CREATE TABLE IF NOT EXISTS settings (key TEXT PRIMARY KEY, value TEXT)")
        await db.commit()
        
