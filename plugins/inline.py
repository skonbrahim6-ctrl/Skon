from pyrogram import Client, filters
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent
from yt_dlp import YoutubeDL

@Client.on_inline_query()
async def inline_search(client, query):
    string = query.query.lower()
    if string == "":
        return
    
    results = []
    with YoutubeDL({"format": "bestaudio/best", "quiet": True}) as ydl:
        videos = ydl.extract_info(f"ytsearch10:{string}", download=False)['entries']
        
        for video in videos:
            results.append(
                InlineQueryResultArticle(
                    title=video['title'],
                    input_message_content=InputTextMessageContent(f"/play {video['webpage_url']}"),
                    description=f"قناة: {video['uploader']}\nمدة: {video['duration_string']}",
                    thumb_url=video['thumbnail']
                )
            )
            
    await query.answer(results=results, cache_time=1)
  
