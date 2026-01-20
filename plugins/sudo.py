from pyrogram import Client, filters
from config import OWNER_ID
import os, sys

@Client.on_message(filters.command("restart") & filters.user(OWNER_ID))
async def restart_bot(client, message):
    await message.reply_text("<b>🔄 جارِ إعادة تشغيل البوت وتحديث الملفات...</b>")
    os.execl(sys.executable, sys.executable, *sys.argv)

@Client.on_message(filters.command("clean") & filters.user(OWNER_ID))
async def clean_storage(client, message):
    # تنظيف مجلد التحميلات والملفات المؤقتة
    folder = 'downloads/'
    if os.path.exists(folder):
        for file in os.listdir(folder):
            os.remove(os.path.join(folder, file))
        await message.reply_text("<b>🧹 تم تنظيف التخزين المؤقت بنجاح!</b>")
    else:
        await message.reply_text("<b>📁 المجلد نظيف بالفعل.</b>")
      
