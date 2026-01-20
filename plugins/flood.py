import time
from pyrogram import Client, filters
from pyrogram.types import Message

# تخزين بيانات المستخدمين مؤقتاً
user_last_cmd_time = {}

@Client.on_message(filters.command(["play", "download", "lyrics", "search"]) & filters.group, group=-1)
async def flood_control(client, message: Message):
    user_id = message.from_user.id
    current_time = time.time()
    
    # تحديد المهلة (مثلاً 3 ثوانٍ بين كل أمر)
    delay = 3
    
    if user_id in user_last_cmd_time:
        last_time = user_last_cmd_time[user_id]
        if current_time - last_time < delay:
            await message.reply_text("<b>⚠️ يرجى الانتظار قليلًا قبل إرسال أمر آخر!</b>")
            message.stop_propagation() # منع تنفيذ الأوامر الأخرى
            return

    user_last_cmd_time[user_id] = current_time
  
