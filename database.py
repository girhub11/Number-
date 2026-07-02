import aiosqlite

async def init_db():
    async with aiosqlite.connect("store.db") as db:
        await db.execute("CREATE TABLE IF NOT EXISTS stocks (id INTEGER PRIMARY KEY, category TEXT, name TEXT, price REAL, stock INTEGER)")
        await db.execute("CREATE TABLE IF NOT EXISTS settings (key TEXT PRIMARY KEY, value TEXT)")
        # Default settings
        await db.execute("INSERT OR IGNORE INTO settings VALUES ('banner', 'https://via.placeholder.com/600x300')")
        await db.execute("INSERT OR IGNORE INTO settings VALUES ('welcome_msg', 'Welcome to the Store!')")
        await db.commit()
        
