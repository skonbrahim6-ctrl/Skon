from pyrogram import Client, filters
from config import BOT_NAME

# الرد عند كتابة "بوت" أو "البوت"
@Client.on_message(filters.regex("^(بوت|البوت)$") & filters.group)
async def bot_reply(client, message):
    await message.reply_text(
        f"<b>لبيه! أنا {BOT_NAME} معك 🎶</b>\n"
        "تبغى تشغل شيء؟ أرسل <code>/play</code> وبعده اسم الأغنية."
    )

# الرد عند كتابة "سورس" أو "السورس"
@Client.on_message(filters.regex("^(سورس|السورس)$") & filters.group)
async def source_reply(client, message):
    await message.reply_text(
        "<b>💎 سورس 𝐒𝐏𝐎𝐓𝐈 𝐌𝐔𝐒𝐈𝐂 الفخم</b>\n"
        "📡 يعمل حالياً بنظام الملفات على تيرميكس.\n"
        "📢 تابعنا هنا: @C_R_B_X"
    )

# إضافة رد ترحيبي بسيط عند دخول عضو جديد (اختياري)
@Client.on_message(filters.new_chat_members)
async def welcome(client, message):
    for member in message.new_chat_members:
        if member.id == (await client.get_me()).id:
            await message.reply_text(f"<b>✅ شكراً لإضافتي في المجموعة!\nللمساعدة أرسل <code>/help</code></b>")
            
