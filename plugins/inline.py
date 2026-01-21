from pyrogram import Client, filters
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent
from yt_dlp import YoutubeDL

@Client.on_inline_query()
async def inline_search(client, query):
    text = query.query.strip().lower()
    if not text:
        return
    
    results = []
    # إعدادات بحث سريعة جداً بدون تحميل
    ydl_opts = {
        "format": "bestaudio/best",
        "quiet": True,
        "no_warnings": True,
        "extract_flat": True, # تسريع البحث بجلب الروابط فقط
    }
    
    try:
        with YoutubeDL(ydl_opts) as ydl:
            # البحث عن أول 10 نتائج
            videos = ydl.extract_info(f"ytsearch10:{text}", download=False)['entries']
            
            for video in videos:
                results.append(
                    InlineQueryResultArticle(
                        title=video.get('title', 'بدون عنوان'),
                        description=f"📺 القناة: {video.get('uploader', 'غير معروف')}\n🔗 اضغط للإرسال والتحميل",
                        thumb_url=video.get('thumbnail'),
                        input_message_content=InputTextMessageContent(
                            f"/play {video.get('url') or video.get('webpage_url')}"
                        )
                    )
                )
        
        await query.answer(results=results, cache_time=300) # كاش لمدة 5 دقائق لتوفير الإنترنت
    except Exception as e:
        print(f"Inline Error: {e}")
            
