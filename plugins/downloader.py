from pyrogram import Client, filters
import os
from yt_dlp import YoutubeDL

@Client.on_message(filters.command(["download", "تحميل"]))
async def download_song(client, message):
    if len(message.command) < 2:
        return await message.reply_text("<b>❌ أرسل اسم الأغنية لتحميلها!</b>")
    
    m = await message.reply_text("<b>📥 جاري معالجة التحميل (قد يستغرق لحظات)...</b>")
    query = message.text.split(None, 1)[1]
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '192',}],
    }
    
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch:{query}", download=True)['entries'][0]
            file_path = ydl.prepare_filename(info).replace('.webm', '.mp3').replace('.m4a', '.mp3').replace('.opus', '.mp3')
        
        await message.reply_audio(
            audio=file_path, 
            title=info.get('title'), 
            performer=info.get('uploader'),
            caption=f"<b>✅ تم التحميل بواسطة: {client.me.mention}</b>"
        )
        await m.delete()
        if os.path.exists(file_path): os.remove(file_path)
    except Exception as e:
        await m.edit(f"<b>❌ فشل التحميل: {e}</b>")
        
