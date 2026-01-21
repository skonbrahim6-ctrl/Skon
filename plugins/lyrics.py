from pyrogram import Client, filters
import requests

@Client.on_message(filters.command(["lyrics", "كلمات"]))
async def get_lyrics(client, message):
    if len(message.command) < 2:
        return await message.reply_text("<b>❌ يرجى كتابة اسم الأغنية!</b>\nمثال: <code>/lyrics تملي معاك</code>")
    
    query = " ".join(message.command[1:])
    m = await message.reply_text(f"<b>🔍 جاري البحث عن كلمات:</b> <code>{query}</code>")
    
    try:
        # البحث عن الكلمات باستخدام API
        # ملاحظة: إذا توقف هذا الـ API يمكنك إخباري لتغييره
        url = f"https://api.paxsenix.biz.id/tools/lyrics?text={query}"
        resp = requests.get(url, timeout=10).json()
        
        lyrics = resp.get("lyrics")
        title = resp.get("title", "غير معروف")
        artist = resp.get("artist", "غير معروف")
        
        if not lyrics or resp.get("status") is False:
            return await m.edit("<b>❌ لم يتم العثور على كلمات لهذه الأغنية.</b>\nجرب كتابة اسم الأغنية مع اسم الفنان.")
            
        # تقسيم الرسالة إذا كانت الكلمات طويلة جداً (تجنباً لخطأ تليجرام)
        text = f"<b>🎵 الأغنية:</b> {title}\n<b>🎤 الفنان:</b> {artist}\n\n<code>{lyrics}</code>"
        
        if len(text) > 4096:
            await m.edit(text[:4090] + "...")
        else:
            await m.edit(text)
            
    except Exception as e:
        await m.edit(f"<b>❌ حدث خطأ أثناء الاتصال بالمخدم:</b>\n<code>{str(e)}</code>")
        
