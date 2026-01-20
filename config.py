import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID", "24803565"))
API_HASH = os.getenv("API_HASH", "67017684693998f8045f8f9037c80523")
BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_DB_URI = os.getenv("MONGO_DB_URI")
STRING_SESSION = os.getenv("STRING_SESSION")
OWNER_ID = int(os.getenv("OWNER_ID", "7445763567"))
