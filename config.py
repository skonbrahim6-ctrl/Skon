import os
from dotenv import load_dotenv

# تحميل البيانات من ملف .env
load_dotenv()

# استدعاء البيانات
API_ID = int(os.getenv("API_ID", "24803565"))
API_HASH = os.getenv("API_HASH", "67017684693998f8045f8f9037c80523")
BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_DB_URI = os.getenv("MONGO_DB_URI")
STRING_SESSION = os.getenv("STRING_SESSION")
OWNER_ID = int(os.getenv("OWNER_ID", "7445763567"))

# إعدادات البوت الثابتة
BOT_NAME = "𝐒𝐏𝐎𝐓𝐈 𝐌𝐔𝐒𝐈𝐂 🎶"
SUPPORT_USER = "C_R_B_X"
START_VIDEO = "https://l.top4top.io/m_36723i2xy0.mp4"
