import asyncio
import logging
from pyrogram import Client, idle
from motor.motor_asyncio import AsyncIOMotorClient
# استيراد البيانات من ملف الإعدادات الخاص بك
from config import API_ID, API_HASH, BOT_TOKEN, MONGO_DB_URI

# إعداد السجلات لمراقبة أداء البوت وتنبيهك في حال وجود أخطاء
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# تعريف كائن البوت وتحديد مسار الإضافات (plugins)
app = Client(
    "SpotiMusicBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins") # هذا السطر هو المسؤول عن تشغيل كل الملفات في مجلد plugins
)

async def start_bot():
    print("🚀 جاري بدء تشغيل محرك SPOTI MUSIC...")
    
    # محاولة الاتصال بقاعدة البيانات MongoDB
    try:
        mongo = AsyncIOMotorClient(MONGO_DB_URI)
        await mongo.admin.command('ping')
        print("✅ تم الاتصال بقاعدة البيانات بنجاح!")
    except Exception as e:
        print(f"❌ فشل الاتصال بقاعدة البيانات: {e}")
        print("⚠️ تنبيه: قد لا تعمل بعض ميزات الإحصائيات بدون قاعدة بيانات.")

    # تشغيل البوت فعلياً
    await app.start()
    
    # جلب يوزرنيم البوت للتأكد من نجاح العملية
    get_me = await app.get_me()
    print("-" * 30)
    print(f"✅ البوت يعمل الآن بنجاح!")
    print(f"🤖 اسم البوت: {get_me.first_name}")
    print(f"🆔 معرف البوت: @{get_me.username}")
    print("-" * 30)
    print("📌 أرسل /start في البوت للتجربة.")

    # إبقاء البوت قيد التشغيل (Idle) حتى يتم إيقافه يدوياً
    await idle()
    
    # إيقاف البوت عند الخروج بشكل آمن
    await app.stop()
    print("🛑 تم إيقاف البوت بنجاح.")

if __name__ == "__main__":
    # تشغيل الحلقة البرمجية الأساسية
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(start_bot())
    except KeyboardInterrupt:
        print("\n🛑 تم إيقاف التشغيل بواسطة المستخدم.")
    except Exception as e:
        logger.error(f"حدث خطأ غير متوقع: {e}")
        
