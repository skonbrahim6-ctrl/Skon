import os
import yt_dlp
from pyrogram import Client, filters
from config import DOWNLOAD_DIRECTORY

@Client.on_message(filters.command(["يوت", "تحميل", "play"]) & filters.private)
async def fast_download(client, message):
    if len(message.command) < 2:
        return await message.reply_text("<b>❌ أرسل (يوت + اسم الأغنية) أو (تحميل + الرابط)</b>")

    query = message.text.split(None, 1)[1]
    msg = await message.reply_text("<b>⏳ جاري البحث والتحميل بسرعة الصاروخ... 🚀</b>")

    # إعدادات السرعة والجودة المتوسطة (عشان يرفع بسرعة في تيرميكس)
    ydl_opts = {
        'format': 'best[ext=mp4]/best', # اختيار أفضل صيغة مباشرة
        'outtmpl': f'{DOWNLOAD_DIRECTORY}%(title)s.%(ext)s',
        'noplaylist': True,
        'quiet': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # إذا كان المدخل ليس رابطاً، سيبحث في يوتيوب تلقائياً
            info = ydl.extract_info(f"ytsearch:{query}", download=True)['entries'][0]
            file_path = ydl.prepare_filename(info)
            title = info.get('title', 'Video')

        await msg.edit("<b>✅ اكتمل التحميل.. جاري الإرسال الآن ⚡</b>")

        # إرسال الملف
        await message.reply_video(
            video=file_path,
            caption=f"<b>🎬 تم التحميل بنجاح:</b>\n`{title}`"
        )

        # حذف الملف فوراً لتوفير مساحة تيرميكس
        if os.path.exists(file_path):
            os.remove(file_path)
        await msg.delete()

    except Exception as e:
        await msg.edit(f"<b>❌ حدث خطأ:</b> `{str(e)}` \n تأكد من تثبيت ffmpeg")
        
