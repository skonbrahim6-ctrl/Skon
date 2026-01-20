from pytgcalls import PyTgCalls
from pytgcalls.types import AudioPiped
from yt_dlp import YoutubeDL

# إعدادات استخراج الصوت من يوتيوب
ytdl_opts = {"format": "bestaudio/best", "quiet": True, "no_warnings": True}
ytdl = YoutubeDL(ytdl_opts)

def get_audio_link(query):
    info = ytdl.extract_info(f"ytsearch:{query}", download=False)['entries'][0]
    return info['url'], info['title']
  
