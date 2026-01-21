import os
import sys
import shutil
from pyrogram import Client, filters
from config import OWNER_ID

@Client.on_message(filters.command("restart") & filters.user(OWNER_ID))
async def restart_bot(client, message):
    await message.reply_text("<b>🔄 جارِ إعادة تشغيل البوت في تيرميكس...</b>\n<i>قد يستغرق الأمر ثوانٍ للعودة للعمل.</i>")
    # إغلاق الجلسة الحالية وإعادة تشغيل الملف الأساسي
    os.execl(sys.executable, sys.executable, *sys.argv)

@Client.on_message(filters.command("clean") & filters.user(OWNER_ID))
async def clean_storage(client, message):
    folder = 'downloads/'
    try:
        if os.path.exists(folder):
            # حذف المجلد بالكامل ثم إعادة إنشائه لضمان حذف كل شيء حتى المجلدات الفرعية
            shutil.rmtree(folder)
            os.makedirs(folder)
            await message.reply_text("<b>🧹 تم تفريغ مجلد التحميلات بالكامل بنجاح!</b>")
        else:
            os.makedirs(folder)
            await message.reply_text("<b>📁 تم إنشاء مجلد التحميلات، لم تكن هناك ملفات لحذفها.</b>")
    except Exception as e:
        await message.reply_text(f"<b>❌ فشل التنظيف:</b>\n<code>{str(e)}</code>")

@Client.on_message(filters.command("leaveall") & filters.user(OWNER_ID))
async def leave_all(client, message):
    # أمر إضافي للمطور لمغادرة كل المجموعات (مفيد في حالات الضغط)
    m = await message.reply_text("<b>🚶 جارِ مغادرة جميع المجموعات...</b>")
    count = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in ["group", "supergroup"]:
            await client.leave_chat(dialog.chat.id)
            count += 1
    await m.edit(f"<b>✅ تمت المغادرة من {count} مجموعة بنجاح.</b>")
    
