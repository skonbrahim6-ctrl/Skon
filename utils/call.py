from yt_dlp import YoutubeDL

# إعدادات البحث والتحميل
ytdl_opts = {
    "format": "bestaudio/best",
    "quiet": True,
    "no_warnings": True,
    "default_search": "auto",
    "source_address": "0.0.0.0",
}

ytdl = YoutubeDL(ytdl_opts)

def get_audio_info(query):
    """
    وظيفة لجلب معلومات الفيديو والرابط المباشر
    """
    try:
        search_query = f"ytsearch:{query}"
        # نستخدم download=False لجلب المعلومات فقط دون تحميل في هذه المرحلة
        info = ytdl.extract_info(search_query, download=False)
        
        if 'entries' in info and len(info['entries']) > 0:
            entry = info['entries'][0]
            return {
                "link": entry.get('url'),
                "title": entry.get('title'),
                "duration": entry.get('duration'),
                "id": entry.get('id'),
                "thumbnail": entry.get('thumbnail'),
                "uploader": entry.get('uploader')
            }
        return None
    except Exception as e:
        print(f"Error in get_audio_info: {e}")
        return None

# وظيفة قديمة للتوافق مع الملفات الأخرى إذا استدعتها بنفس الاسم
def get_audio_link(query):
    data = get_audio_info(query)
    if data:
        return data['link'], data['title'], data['duration'], data['id']
    return None, None, None, None
    
