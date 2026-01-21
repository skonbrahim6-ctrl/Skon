import asyncio
from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN, MONGO_DB_URI
from motor.motor_asyncio import AsyncIOMotorClient
import logging

# إعداد السجلات (Logging) لمراقبة الأخطاء
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# تعريف البوت
app = Client(
    "SpotiMusic",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins") # هذا السطر يقوم بتحميل كل الملفات داخل مجلد plugins تلقائياً
)

async def start_bot():
    print("🚀 جاري بدء تشغيل البوت...")
    
    # الاتصال بقاعدة البيانات (MongoDB)
    try:
        mongo = AsyncIOMotorClient(MONGO_DB_URI)
        await mongo.admin.command('ping')
        print("✅ تم الاتصال بقاعدة البيانات بنجاح!")
    except Exception as e:
        print(f"❌ خطأ في الاتصال بقاعدة البيانات: {e}")

    # تشغيل البوت
    await app.start()
    
    # جلب معلومات البوت
    get_me = await app.get_me()
    print(f"✅ تم تشغيل البوت بنجاح باسم: @{get_me.username}")
    
    # البقاء في وضع التشغيل (Idle)
    await idle()
    
    # إغلاق البوت عند التوقف
    await app.stop()
    print("🛑 تم إيقاف البوت.")

if __name__ == "__main__":
    try:
        asyncio.get_event_loop().run_until_complete(start_bot())
    except KeyboardInterrupt:
        pass
        
