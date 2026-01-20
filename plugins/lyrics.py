from pyrogram import Client, filters
import requests

@Client.on_message(filters.command(["lyrics", "كلمات"]))
async def get_lyrics(client, message):
    if len(message.command) < 2:
        return await message.reply_text("<b>❌ أرسل اسم الأغنية مع الأمر!</b>")
    
    m = await message.reply_text("<b>🔍 جاري البحث عن الكلمات...</b>")
    query = message.text.split(None, 1)[1]
    
    try:
        # استخدام API خارجي لجلب الكلمات
        resp = requests.get(f"https://api.paxsenix.biz.id/tools/lyrics?text={query}").json()
        lyrics = resp.get("lyrics")
        title = resp.get("title")
        artist = resp.get("artist")
        
        if not lyrics:
            return await m.edit("<b>❌ لم يتم العثور على كلمات لهذه الأغنية.</b>")
            
        await m.edit(f"<b>🎵 الأغنية: {title}\n🎤 الفنان: {artist}</b>\n\n<code>{lyrics}</code>")
    except Exception as e:
        await m.edit(f"<b>❌ حدث خطأ أثناء جلب الكلمات: {e}</b>")
      
