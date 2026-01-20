from yt_dlp import YoutubeDL

ytdl_opts = {
    "format": "bestaudio/best",
    "quiet": True,
    "no_warnings": True,
    "default_search": "auto",
    "source_address": "0.0.0.0",
}

ytdl = YoutubeDL(ytdl_opts)

def get_audio_link(query):
    search_query = f"ytsearch:{query}"
    info = ytdl.extract_info(search_query, download=False)['entries'][0]
    return info['url'], info['title'], info['duration'], info['id']
    
