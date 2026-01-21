import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_NAME, BOT_USERNAME
from yt_dlp import YoutubeDL

# إعدادات التحميل الاحترافية
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'downloads/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'quiet': True,
    'no_warnings': True,
}

@Client.on_message(filters.command(["play", "تشغيل"]) & filters.group)
async def play(client, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "<b>❌ عذراً.. يرجى كتابة اسم الأغنية أو رابط يوتيوب بعد الأمر!</b>\n\n"
            "<b>مثال:</b> <code>/play ضحى بيه</code>"
        )
    
    query = message.text.split(None, 1)[1]
    m = await message.reply_text(f"<b>🔍 جاري البحث عن ↫ ⦗ {query} ⦘...</b>")
    
    try:
        # البحث والتحميل باستخدام yt-dlp المتوافقة مع تيرميكس
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(f"ytsearch:{query}", download=True)['entries'][0]
            audio_file = ydl.prepare_filename(info_dict).rsplit(".", 1)[0] + ".mp3"
            title = info_dict.get('title', 'Audio')
            duration = info_dict.get('duration', 0)

        # تصميم أزرار التحكم (اللمسة الفخمة)
        buttons = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("⏹ إغلاق القائمة", callback_data="stop")
            ],
            [
                InlineKeyboardButton("✨ أضفني لمجموعتك ✨", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ]
        ])

        await m.edit("<b>📤 جاري رفع الملف الصوتي للمجموعة...</b>")

        # إرسال الملف الصوتي بدلاً من فتح مكالمة
        await message.reply_audio(
            audio=audio_file,
            caption=f"<b>🎸 تم التحميل والتشغيل بنجاح!</b>\n\n"
                    f"<b>🎵 الأغنية:</b> <code>{title}</code>\n"
                    f"<b>💎 بواسطة:</b> {BOT_NAME}",
            duration=int(duration),
            title=title,
            reply_markup=buttons
        )
        
        await m.delete()

        # تنظيف مساحة الهاتف فوراً
        if os.path.exists(audio_file):
            os.remove(audio_file)

    except Exception as e:
        await m.edit(f"<b>❌ حدث خطأ غير متوقع!\nالسبب:</b> <code>{str(e)}</code>")

@Client.on_message(filters.command(["stop", "ايقاف"]) & filters.group)
async def stop(client, message):
    await message.reply_text("<b>🛑 تم إيقاف التشغيل.</b>\n<i>(ملاحظة: يمكنك حذف الملف الصوتي من المجموعة يدوياً)</i>")
            
