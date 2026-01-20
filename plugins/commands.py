from pyrogram import Client, filters
from config import BOT_USERNAME

@Client.on_message(filters.command(["play", "تشغيل"]) & filters.group)
async def play_command(client, message):
    await message.reply_text("🎸 جاري البحث عن الأغنية وتشغيلها في المكالمة...")
    # هنا تضاف أكواد البحث والتشغيل لاحقاً

@Client.on_message(filters.command(["stop", "ايقاف"]) & filters.group)
async def stop_command(client, message):
    await message.reply_text("🛑 تم إيقاف التشغيل بواسطة المدير.")

@Client.on_message(filters.command(["skip", "تخطي"]) & filters.group)
async def skip_command(client, message):
    await message.reply_text("⏭ تم تخطي الأغنية الحالية.")
  
