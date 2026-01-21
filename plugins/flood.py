import time
from pyrogram import Client, filters
from pyrogram.types import Message

# تخزين بيانات المستخدمين (يتم تصفيرها عند إعادة تشغيل البوت)
user_last_cmd_time = {}

# تحديد المهلة بالثواني (رفعناها لـ 10 ثوانٍ لأن التحميل يستهلك وقتاً)
FLOOD_DELAY = 10 

@Client.on_message(filters.command(["play", "تشغيل", "download", "تحميل", "search"]) & filters.group, group=-1)
async def flood_control(client, message: Message):
    # إذا كان المرسل هو المطور، نتخطى الحماية
    from config import OWNER_ID
    if message.from_user.id == OWNER_ID:
        return

    user_id = message.from_user.id
    current_time = time.time()
    
    if user_id in user_last_cmd_time:
        last_time = user_last_cmd_time[user_id]
        elapsed_time = current_time - last_time
        
        if elapsed_time < FLOOD_DELAY:
            remaining = int(FLOOD_DELAY - elapsed_time)
            await message.reply_text(
                f"<b>⚠️ يرجى الانتظار <code>{remaining}</code> ثانية قبل طلب أغنية أخرى!</b>\n"
                f"<i>نحن نستخدم تيرميكس، ارحم المعالج قليلاً 😊</i>"
            )
            message.stop_propagation() # منع تنفيذ الأوامر (أهم سطر)
            return

    # تحديث وقت آخر أمر للمستخدم
    user_last_cmd_time[user_id] = current_time
    
