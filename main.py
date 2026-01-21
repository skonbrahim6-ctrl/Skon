import asyncio
from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN

# تشغيل البوت فقط بدون محرك المكالمات
app = Client(
    "SkonBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("✅ تم إلغاء نظام الأغاني مؤقتاً.. البوت يعمل الآن كبوت رسائل عادي في تيرميكس!")

print("🚀 جاري تشغيل البوت بدون نظام المكالمات...")
app.run()
