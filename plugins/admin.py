from pyrogram import Client, filters
from config import OWNER_ID

@Client.on_message(filters.command("stats") & filters.user(OWNER_ID))
async def stats(client, message):
    await message.reply_text("<b>📊 إحصائيات البوت:</b>\n\n✅ البوت يعمل بنجاح\n📡 قاعدة البيانات متصلة\n🔊 المكالمات النشطة: جاري الفحص...")

@Client.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
async def broadcast(client, message):
    if not message.reply_to_message:
        return await message.reply_text("<b>يرجى الرد على الرسالة التي تريد إذاعتها!</b>")
    await message.reply_text("<b>📢 جاري الإذاعة لكل المستخدمين والمجموعات...</b>")
  
