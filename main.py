import asyncio
from pyrogram import Client, idle
from pytgcalls import PyTgCalls
from motor.motor_asyncio import AsyncIOMotorClient
import config # استيراد الإعدادات من ملفك

# 1. إعداد قاعدة بيانات MongoDB
mongodb = AsyncIOMotorClient(config.MONGO_DB_URI)
db = mongodb.SpotiMusic # إنشاء قاعدة بيانات باسم البوت

# 2. تعريف العميل (البوت الأساسي)
app = Client(
    "SpotiMusicBot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    plugins=dict(root="plugins") # تفعيل المجلدات المنفصلة
)

# 3. تعريف الحساب المساعد (UserBot)
assistant = Client(
    "SpotiAssistant",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    session_string=config.STRING_SESSION
)

# 4. تعريف محرك المكالمات الصوتية
call_py = PyTgCalls(assistant)

async def start_services():
    print("-----------------------------------")
    print("💎 جارِ تشغيل بوت 𝐒𝐏𝐎𝐓𝐈 𝐌𝐔𝐒𝐈𝐂...")
    print("-----------------------------------")
    
    # تشغيل البوت
    await app.start()
    print("✅ تم تشغيل البوت الأساسي بنجاح.")
    
    # تشغيل الحساب المساعد
    await assistant.start()
    print("✅ تم تشغيل الحساب المساعد بنجاح.")
    
    # تشغيل محرك المكالمات
    await call_py.start()
    print("✅ تم ربط محرك المكالمات الصوتية.")
    
    # فحص الاتصال بقاعدة البيانات
    try:
        await mongodb.server_info()
        print("✅ تم الاتصال بقاعدة بيانات MongoDB بنجاح.")
    except Exception as e:
        print(f"❌ خطأ في الاتصال بقاعدة البيانات: {e}")

    print("-----------------------------------")
    print("🚀 البوت الآن جاهز للعمل في المجموعات!")
    print("-----------------------------------")
    
    await idle() # إبقاء البوت يعمل

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(start_services())
    
