import asyncio
from pyrogram import Client
from pytgcalls import PyTgCalls
from pytgcalls.types import Update
# استدعاء المتغيرات من ملفك
from config import API_ID, API_HASH, BOT_TOKEN, STRING_SESSION

# إعداد المساعد (الحساب الذي سيدخل المكالمة)
assistant = Client("SkonAssistant", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION)
# إعداد محرك المكالمات الحديث
call_py = PyTgCalls(assistant)

async def main():
    print("[!] جاري تشغيل المساعد...")
    await assistant.start()
    await call_py.start()
    print("✅ البوت يعمل الآن في تيرميكس! اذهب لتجربته.")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
    
