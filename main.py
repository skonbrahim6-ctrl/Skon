import asyncio
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types import Update
from config import API_ID, API_HASH, BOT_TOKEN, STRING_SESSION

# إعداد بوت التليجرام
app = Client(
    "SkonBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")
)

# إعداد حساب المساعد للمكالمات (Client Assistant)
assistant = Client(
    "SkonAssistant",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION
)

# إعداد محرك المكالمات الجديد (الإصدار 2.x.x)
call_py = PyTgCalls(assistant)

@app.on_message(filters.command("start"))
async def start_handler(client, message):
    await message.reply_text("✅ أهلاً بك! البوت يعمل بنجاح بأحدث المكتبات.")

async def start_bot():
    print("[!] جاري تشغيل البوت والمساعد...")
    await app.start()
    await assistant.start()
    await call_py.start()
    print("[+] ✅ كل الأنظمة تعمل بنجاح! البوت الآن جاهز.")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(start_bot())
    
