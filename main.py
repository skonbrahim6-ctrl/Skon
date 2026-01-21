import asyncio
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

# إعداد البوت مع خاصية "الplugins" لقراءة كل الملفات
app = Client(
    "SkonBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins") # هذا السطر هو اللي بيشغل ملف ستارت وباقي الأوامر
)

print("🚀 جاري تشغيل البوت وقراءة جميع الأوامر...")
app.run()
