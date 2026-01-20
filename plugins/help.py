from pyrogram import Client, filters
from config import BOT_NAME

@Client.on_message(filters.command(["help", "اوامر", "أوامر"]))
async def help_cmds(client, message):
    help_text = f"""
<b>📊 قائمة أوامر بوت {BOT_NAME}:</b>

<b>🎸 أوامر التشغيل:</b>
• <code>/play</code> + [اسم الأغنية] : للتشغيل بالمكالمة.
• <code>/stop</code> : لإيقاف التشغيل نهائياً.
• <code>/pause</code> : إيقاف مؤقت.
• <code>/resume</code> : استئناف التشغيل.

<b>📥 أوامر التحميل:</b>
• <code>/download</code> + [اسم الأغنية] : تحميل ملف صوتي.
• <code>/lyrics</code> + [اسم الأغنية] : جلب كلمات الأغنية.

<b>🔍 البحث:</b>
• يمكنك البحث مباشرة عبر كتابة يوزر البوت في أي محادثة.
"""
    await message.reply_text(help_text)
  
