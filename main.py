import asyncio
from pyrogram import Client, idle
from pytgcalls import PyTgCalls
from pytgcalls.types import AudioPiped
from motor.motor_asyncio import AsyncIOMotorClient
import config
from utils.queue import get_queue, clear_queue

# 1. إعداد قاعدة البيانات
mongodb = AsyncIOMotorClient(config.MONGO_DB_URI)
db = mongodb.SpotiMusic

# 2. تعريف البوت والمساعد
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

# 3. نظام التشغيل التلقائي (عند انتهاء الأغنية)
@call_py.on_stream_end()
async def stream_end_handler(client, update):
    chat_id = update.chat_id
    queue = get_queue(chat_id)
    if queue:
        # حذف الأغنية التي انتهت وسحب التالية
        queue.pop(0)
        if queue:
            next_song = queue[0]
            await call_py.play(chat_id, AudioPiped(next_song['url']))
            await app.send_message(
                chat_id, 
                f"<b>⏭ جاري تشغيل الأغنية التالية تلقائياً:</b>\n<code>{next_song['title']}</code>"
            )
        else:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
    else:
        await call_py.leave_group_call(chat_id)

async def start_services():
    print("💎 جارِ بدء تشغيل 𝐒𝐏𝐎𝐓𝐈 𝐌𝐔𝐒𝐈𝐂...")
    await app.start()
    await assistant.start()
    await call_py.start()
    print("✅ كل الأنظمة تعمل بنجاح!")
    await idle()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(start_services())
            
