from pyrogram import Client, filters
from config import BOT_NAME

@Client.on_message(filters.command(["play", "تشغيل"]) & filters.group)
async def play(client, message):
    await message.reply_text(f"<b>🎸 {BOT_NAME} | جاري معالجة الطلب...</b>")

@Client.on_message(filters.command(["stop", "ايقاف"]) & filters.group)
async def stop(client, message):
    await message.reply_text("<b>🛑 تم إيقاف التشغيل وإنهاء المكالمة.</b>")
  
