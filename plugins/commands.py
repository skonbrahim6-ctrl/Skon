import os
import asyncio
from pyrogram import Client, filters
from yt_dlp import YoutubeDL

# إعدادات التحميل من اليوتيوب
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
async def play_command(client, message):
    if len(message.command) < 2:
        return await message.reply_text("<b>❌ يرجى كتابة اسم الأغنية بعد الأمر!</b>\nمثال: <code>/play عمرو دياب</code>")
    
    query = " ".join(message.command[1:])
    m = await message.reply_text(f"<b>🔍 جاري البحث عن:</b> <code>{query}</code>")
    
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(f"ytsearch:{query}", download=True)['entries'][0]
            audio_file = ydl.prepare_filename(info_dict).rsplit(".", 1)[0] + ".mp3"
            title = info_dict.get('title', 'Audio')
            duration = info_dict.get('duration', 0)
            thumbnail = info_dict.get('thumbnail', None)

        await m.edit("<b>📤 جاري رفع الملف الصوتي...</b>")
        
        await message.reply_audio(
            audio=audio_file,
            caption=f"<b>🎵 تم التحميل بنجاح:</b>\n<code>{title}</code>\n\n💎 <b>بواسطة:</b> تيرميكس",
            duration=int(duration),
            title=title
        )
        
        await m.delete()
        
        # حذف الملف من الهاتف بعد الإرسال لتوفير المساحة
        if os.path.exists(audio_file):
            os.remove(audio_file)
            
    except Exception as e:
        await m.edit(f"<b>❌ حدث خطأ أثناء البحث:</b>\n<code>{str(e)}</code>")

@Client.on_message(filters.command(["stop", "ايقاف"]) & filters.group)
async def stop_command(client, message):
    await message.reply_text("<b>🛑 هذا الأمر يعمل فقط في نظام المكالمات.</b>\nلحذف الرسائل الصوتية، يمكنك حذفها يدوياً.")

@Client.on_message(filters.command(["skip", "تخطي"]) & filters.group)
async def skip_command(client, message):
    await message.reply_text("<b>⏭ نظام التخطي غير مفعل في وضع الملفات الصوتية.</b>")
    
