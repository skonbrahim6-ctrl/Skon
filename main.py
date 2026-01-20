import asyncio
import os
from pyrogram import Client, idle, filters
from pytgcalls import PyTgCalls
from pytgcalls.types import AudioPiped
from motor.motor_asyncio import AsyncIOMotorClient
import config
from utils.queue import get_queue, clear_queue

# --- إنشاء المجلدات الضرورية تلقائياً ---
for folder in ["downloads", "cache"]:
    if not os.path.exists(folder):
        os.mkdir(folder)

# --- إعداد قاعدة البيانات ---
mongodb = AsyncIOMotorClient(config.MONGO_DB_URI)
db = mongodb.SpotiMusic

# --- تعريف البوت والمساعد ---
app = Client(
    "SpotiMusicBot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    plugins=dict(root="plugins")
)

assistant = Client(
    "SpotiAssistant",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    session_string=config.STRING_SESSION
)

call_py = PyTgCalls(assistant)

# --- [جديد] الترحيب عند دخول المجموعة ---
@app.on_message(filters.new_chat_members)
async def welcome_to_group(client, message):
    for member in message.new_chat_members:
        if member.id == (await client.get_me()).id:
            await message.reply_text(
                f"<b>✅ شكراً لإضافتي إلى {message.chat.title}!\n\n"
                f"🎸 أنا بوت {config.BOT_NAME} المطور.\n"
                f"استخدم أمر /play + اسم الأغنية للبدء.\n"
                f"للمساعدة أرسل /help</b>"
            )

# --- نظام التشغيل التلقائي (عند انتهاء الأغنية) ---
@call_py.on_stream_end()
async def stream_end_handler(client, update):
    chat_id = update.chat_id
    queue = get_queue(chat_id)
    if queue:
        queue.pop(0) # حذف اللي خلصت
        if queue:
            next_song = queue[0]
            await call_py.play(chat_id, AudioPiped(next_song['url']))
            await app.send_message(
                chat_id, 
                f"<b>⏭ تشغيل التالي تلقائياً:</b>\n<code>{next_song['title']}</code>"
            )
        else:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
    else:
        await call_py.leave_group_call(chat_id)

# --- [جديد] وظيفة التنظيف التلقائي للملفات ---
async def auto_cleaner():
    while True:
        await asyncio.sleep(3600) # تنظيف كل ساعة
        for folder in ["downloads", "cache"]:
            for file in os.listdir(folder):
                file_path = os.path.join(folder, file)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                except Exception as e:
                    print(f"Error cleaning {file_path}: {e}")

async def start_services():
    print("💎 جارِ بدء تشغيل 𝐒𝐏𝐎𝐓𝐈 𝐌𝐔𝐒𝐈𝐂...")
    await app.start()
    await assistant.start()
    await call_py.start()
    
    # تشغيل منظف الملفات في الخلفية
    asyncio.create_task(auto_cleaner())
    
    print("✅ كل الأنظمة تعمل بنجاح!")
    await idle()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(start_services())
    
