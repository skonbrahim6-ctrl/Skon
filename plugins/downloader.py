from pyrogram import Client, filters
import os
from yt_dlp import YoutubeDL

@Client.on_message(filters.command(["download", "تحميل"]))
async def download_song(client, message):
    if len(message.command) < 2:
        return await message.reply_text("<b>❌ أرسل اسم الأغنية لتحميلها!</b>")
    
    m = await message.reply_text("<b>📥 جاري معالجة التحميل...</b>")
    query = message.text.split(None, 1)[1]
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'downloads/%(title)s.%(ext)s',
        'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '192',}],
    }
    
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch:{query}", download=True)['entries'][0]
            file_path = ydl.prepare_filename(info).replace('.webm', '.mp3').replace('.m4a', '.mp3')
        
        await message.reply_audio(audio=file_path, title=info['title'], caption=f"<b>🎵 تم التحميل بواسطة: @{client.me.username}</b>")
        await m.delete()
        os.remove(file_path) # حذف الملف بعد الإرسال لتوفير المساحة
    except Exception as e:
        await m.edit(f"<b>❌ فشل التحميل: {e}</b>")
      
