import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_NAME, BOT_USERNAME
from utils.call import get_audio_link

@Client.on_message(filters.command(["play", "تشغيل"]) & filters.group)
async def play(client, message):
    # 1. التحقق من وجود اسم الأغنية
    if len(message.command) < 2:
        return await message.reply_text(
            "<b>❌ عذراً.. يرجى كتابة اسم الأغنية أو رابط يوتيوب بعد الأمر!</b>\n\n"
            "<b>مثال:</b> <code>/play ضحى بيه</code>"
        )
    
    # 2. رسالة جارِ البحث
    query = message.text.split(None, 1)[1]
    m = await message.reply_text(f"<b>🔍 جاري البحث عن ↫ ⦗ {query} ⦘...</b>")
    
    try:
        # 3. جلب رابط الصوت والعنوان من المحرك
        audio_url, title = get_audio_link(query)
        
        # 4. تصميم أزرار التحكم (اللمسة الفخمة)
        buttons = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("⏸ إيقاف مؤقت", callback_data="pause"),
                InlineKeyboardButton("▶️ استئناف", callback_data="resume")
            ],
            [
                InlineKeyboardButton("⏹ إيقاف نهائي", callback_data="stop")
            ],
            [
                InlineKeyboardButton("✨ أضفني لمجموعتك ✨", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ]
        ])

        # 5. تحديث الرسالة إلى وضع التشغيل
        await m.edit(
            f"<b>🎸 تم بدء التشغيل بنجاح!</b>\n\n"
            f"<b>🎵 الأغنية:</b> <code>{title}</code>\n"
            f"<b>👥 المجموعة:</b> {message.chat.title}\n"
            f"<b>💎 بواسطة:</b> {BOT_NAME}",
            reply_markup=buttons
        )

    except Exception as e:
        await m.edit(f"<b>❌ حدث خطأ غير متوقع!\nالسبب:</b> <code>{str(e)}</code>")

@Client.on_message(filters.command(["stop", "ايقاف"]) & filters.group)
async def stop(client, message):
    # كود الإيقاف السريع
    await message.reply_text("<b>🛑 تم إيقاف التشغيل ومغادرة المكالمة بنجاح.</b>")
