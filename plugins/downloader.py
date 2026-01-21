import os
import asyncio
from pyrogram import Client, filters
from yt_dlp import YoutubeDL

# إعدادات متقدمة لتحميل أسرع في تيرميكس
YDL_OPTIONS = {
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

@Client.on_message(filters.command(["download", "تحميل"]))
async def download_song(client, message):
    if len(message.command) < 2:
        return await message.reply_text("<b>❌ يرجى كتابة اسم الأغنية أو رابط اليوتيوب!</b>")
    
    query = " ".join(message.command[1:])
    m = await message.reply_text(f"<b>📥 جاري معالجة طلبك:</b> <code>{query}</code>")
    
    try:
        with YoutubeDL(YDL_OPTIONS) as ydl:
            # استخراج المعلومات والتحميل
            info = ydl.extract_info(f"ytsearch:{query}" if not query.startswith("http") else query, download=True)
            if 'entries' in info:
                info = info['entries'][0]
            
            # تحديد المسار الصحيح للملف بعد التحويل لـ MP3
            file_path = ydl.prepare_filename(info).rsplit(".", 1)[0] + ".mp3"
            title = info.get('title', 'Unknown')
            uploader = info.get('uploader', 'Unknown')
            duration = info.get('duration', 0)

        await m.edit("<b>📤 جاري الرفع إلى تليجرام...</b>")
        
        await message.reply_audio(
            audio=file_path, 
            title=title, 
            performer=uploader,
            duration=int(duration),
            caption=f"<b>✅ تم التحميل بنجاح</b>\n<b>🎵 العنوان:</b> <code>{title}</code>"
        )
        
        await m.delete()
        
        # التأكد من حذف الملف بعد الإرسال لتوفير مساحة الهاتف
        if os.path.exists(file_path):
            os.remove(file_path)
            
    except Exception as e:
        await m.edit(f"<b>❌ حدث خطأ غير متوقع:</b>\n<code>{str(e)}</code>")
            
