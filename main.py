import asyncio
from pyrogram import Client
from pytgcalls import PyTgCalls
from config import API_ID, API_HASH, BOT_TOKEN, SESSION

# تشغيل البوت مع خاصية المجلدات (Plugins)
app = Client(
    "SpotiMusic",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins") # هذا هو السر في فصل الملفات
)

# حساب المساعد (لفتح المايك)
assistant = Client("SpotiAssistant", API_ID, API_HASH, session_string=SESSION)
call_py = PyTgCalls(assistant)

async def start_bot():
    print("💎 SPYOTI MUSIC: جارِ التحميل...")
    await app.start()
    await assistant.start()
    await call_py.start()
    print("✅ البوت الفخم يعمل الآن!")
    await asyncio.idle()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(start_bot())
    
