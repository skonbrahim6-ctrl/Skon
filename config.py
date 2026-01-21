import os
from dotenv import load_dotenv

# تحميل المتغيرات من ملف .env إذا كان موجوداً
load_dotenv()

# --- إعدادات الحساب الأساسية ---
API_ID = int(os.getenv("API_ID", "24803565"))
API_HASH = os.getenv("API_HASH", "67017684693998f8045f8f9037c80523")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8584176399:AAFXwo50vkJd802-dWBdIJeyPOr_2p3cCdw")

# --- إعدادات قاعدة البيانات ---
MONGO_DB_URI = os.getenv("MONGO_DB_URI", "mongodb+srv://skonbrahim6:skonbrahim6@cluster0.v4a00kd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# --- إعدادات المطور والأسماء ---
OWNER_ID = int(os.getenv("OWNER_ID", "7445763567"))
SUPPORT_USER = "C_R_B_X"      # يوزر المطور بدون @
BOT_NAME = "𝐒𝐏𝐎𝐓𝐈 𝐌𝐔𝐒𝐈𝐂 🎶"  # اسم البوت

# --- ميديا وروابط البوت ---
# رابط فيديو Start (تأكد أنه رابط مباشر ينتهي بـ .mp4)
START_VIDEO = "https://l.top4top.io/m_36723i2xy0.mp4"
SUPPORT_GROUP = "https://t.me/C_R_B_X"

# --- إعدادات إضافية ---
# مسار التحميلات في تيرميكس
DOWNLOAD_DIRECTORY = "downloads/"
if not os.path.exists(DOWNLOAD_DIRECTORY):
    os.makedirs(DOWNLOAD_DIRECTORY)

# وقت تنظيف الملفات المؤقتة (بالثواني)
CLEAN_INTERVAL = 3600 

# ملاحظة:STRING_SESSION غير ضرورية في نظام إرسال ملفات MP3
STRING_SESSION = os.getenv("STRING_SESSION", "")
