import os
import yt_dlp
from pyrogram import Client, filters
from config import DOWNLOAD_DIRECTORY

# التأكد من وجود المجلد
if not os.path.exists(DOWNLOAD_DIRECTORY):
    os.makedirs(DOWNLOAD_DIRECTORY)

@Client.on_message(filters.command(["download", "video"]) & filters.private)
async def download_video(client, message):
    if len(message.command) < 2:
        return await message.reply_text("<b>❌ أرسل رابط الفيديو بعد الأمر، مثال:</b>\n`/video https://youtu.be/...`")

    url = message.text.split(None, 1)[1]
    msg = await message.reply_text("<b>⏳ جاري معالجة الرابط وتحميل الفيديو...</b>")

    try:
        # إعدادات التحميل
        ydl_opts = {
            'format': 'best',
            'outtmpl': f'{DOWNLOAD_DIRECTORY}%(title)s.%(ext)s',
            'noplaylist': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info)
            title = info.get('title', 'video')

        await msg.edit("<b>✅ اكتمل التحميل.. جاري الرفع إلى تيليجرام 🚀</b>")

        # إرسال الفيديو للمستخدم
        await message.reply_video(
            video=file_path,
            caption=f"<b>🎬 تم التحميل بنجاح:</b>\n`{title}`"
        )

        # مسح الملف من تيرميكس لتوفير المساحة
        if os.path.exists(file_path):
            os.remove(file_path)
            
        await msg.delete()

    except Exception as e:
        await msg.edit(f"<b>❌ حدث خطأ أثناء التحميل:</b>\n`{str(e)}`")
    
