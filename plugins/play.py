from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types import AudioPiped
from yt_dlp import YoutubeDL
from config import BOT_NAME

# إعداد محرك البحث من يوتيوب
ytdl_opts = {"format": "bestaudio/best", "quiet": True}
ytdl = YoutubeDL(ytdl_opts)

@Client.on_message(filters.command(["play", "تشغيل"]) & filters.group)
async def play(client, message):
    if len(message.command) < 2:
        return await message.reply_text("<b>الرجاء كتابة اسم الأغنية بعد الأمر!</b>")
    
    m = await message.reply_text("<b>🔍 جاري البحث في يوتيوب...</b>")
    query = message.text.split(None, 1)[1]
    
    try:
        # البحث عن الرابط
        info = ytdl.extract_info(f"ytsearch:{query}", download=False)['entries'][0]
        url = info['url']
        title = info['title']
        
        # هنا يتم استدعاء المساعد لفتح المكالمة (سنكمل ربطها بـ PyTgCalls)
        await m.edit(f"<b>🎸 جاري تشغيل: {title}</b>")
        
    except Exception as e:
        await m.edit(f"<b>حدث خطأ: {str(e)}</b>")
      
