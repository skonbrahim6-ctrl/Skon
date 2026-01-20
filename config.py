import os
from dotenv import load_dotenv

# تحميل المتغيرات من ملف .env إذا كان موجوداً محلياً
load_dotenv()

# --- إعدادات الحساب الأساسية ---
# يتم جلبها من Environment Variables في Render
API_ID = int(os.getenv("API_ID", "24803565"))
API_HASH = os.getenv("API_HASH", "67017684693998f8045f8f9037c80523")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8584176399:AAFXwo50vkJd802-dWBdIJeyPOr_2p3cCdw")

# --- إعدادات قاعدة البيانات والجلسة ---
# الرابط الذي أعطيتك إياه (يفضل وضعه في Render للأمان)
MONGO_DB_URI = os.getenv("MONGO_DB_URI", "mongodb+srv://skonbrahim6:skonbrahim6@cluster0.v4a00kd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
STRING_SESSION = os.getenv("STRING_SESSION", "") # كود الجلسة الخاص بحساب المساعد

# --- إعدادات المطور ---
OWNER_ID = int(os.getenv("OWNER_ID", "7445763567"))
SUPPORT_USER = "C_R_B_X"
BOT_NAME = "𝐒𝐏𝐎𝐓𝐈 𝐌𝐔𝐒𝐈𝐂 🎶"

# --- ميديا وروابط البوت ---
START_VIDEO = "https://l.top4top.io/m_36723i2xy0.mp4"
SUPPORT_GROUP = "https://t.me/C_R_B_X"

# --- إعدادات إضافية ---
# مدة تنظيف الذاكرة التلقائي (بالثواني) - ساعة واحدة
CLEAN_INTERVAL = 3600 
