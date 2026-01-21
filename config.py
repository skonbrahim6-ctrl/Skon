import os
from dotenv import load_dotenv

# تحميل المتغيرات من ملف .env (تأكد أن الملف موجود في مجلد البوت)
load_dotenv()

# --- إعدادات الحساب الأساسية ---
# قمت بوضع بياناتك كقيم افتراضية لضمان عمل البوت في تيرميكس مباشرة
API_ID = int(os.getenv("API_ID", "24803565"))
API_HASH = os.getenv("API_HASH", "67017684693998f8045f8f9037c80523")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8584176399:AAFXwo50vkJd802-dWBdIJeyPOr_2p3cCdw")

# --- إعدادات قاعدة البيانات والجلسة ---
MONGO_DB_URI = os.getenv("MONGO_DB_URI", "mongodb+srv://skonbrahim6:skonbrahim6@cluster0.v4a00kd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# ملاحظة: في نظام الـ MP3 الذي برمجناه لتيرميكس، قد لا تحتاج لـ STRING_SESSION 
# لأن البوت هو من سيرسل الملفات، ولكن نتركها احتياطاً
STRING_SESSION = os.getenv("STRING_SESSION", "")

# --- إعدادات المطور ---
OWNER_ID = int(os.getenv("OWNER_ID", "7445763567"))
SUPPORT_USER = "C_R_B_X"
BOT_NAME = "𝐒𝐏𝐎𝐓𝐈 𝐌𝐔𝐒𝐈𝐂 🎶"

# --- ميديا وروابط البوت ---
# ملاحظة: في تيرميكس قد يكون إرسال الروابط أسرع من الفيديوهات الكبيرة
START_VIDEO = "https://l.top4top.io/m_36723i2xy0.mp4"
SUPPORT_GROUP = "https://t.me/C_R_B_X"

# --- إعدادات إضافية ---
CLEAN_INTERVAL = 3600
# تأكد أن هذا المسار موجود في هاتفك
DOWNLOAD_DIRECTORY = "downloads/"
