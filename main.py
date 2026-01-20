import asyncio
from pyrogram import Client
from pytgcalls import PyTgCalls
from config import API_ID, API_HASH, BOT_TOKEN, SESSION

# تعريف البوت وحساب المساعد
app = Client(
    "SpotiMusic",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins") # هذا السطر يربط مجلد الأوامر تلقائياً
)

assistant = Client("SpotiAssistant", API_ID, API_HASH, session_string=SESSION)
call_py = PyTgCalls(assistant)

async def start_bot():
    print("💎 جارِ تشغيل بوت سبوتي ميوزك الفخم...")
    await app.start()
    await assistant.start()
    await call_py.start()
    print("✅ البوت يعمل الآن بنجاح!")
    await asyncio.idle()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(start_bot())
