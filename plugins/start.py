from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import START_VIDEO, SUPPORT_USER, BOT_USERNAME, BOT_NAME

@Client.on_message(filters.command("start") & filters.private)
async def start(client, message):
    text = f"""
<b>─── • ◈ • ───</b>
<b>🎸 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 {BOT_NAME} 🎸</b>
<b>─── • ◈ • ───</b>

<b>أهلاً بك يا {message.from_user.mention} في أقوى بوت ميوزك على التيليجرام ✨</b>

<b>🚀 مميزات البوت:</b>
<b>• تشغيل فوري بجودة 320kbps 🔊</b>
<b>• دعم كامل للمجموعات والقنوات 🛡</b>
<b>• نظام بحث ذكي من يوتيوب وسبوتيفاي 🔍</b>
<b>• حماية كاملة وتشغيل مستمر 24/7 💎</b>

<b>اسـتخدم الأزرار بالأسفل لاستكشاف البوت 👇</b>
"""
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("➕ أضف البوت لمجموعتك ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
            InlineKeyboardButton("👑 𝐃𝐞𝐯", url=f"https://t.me/{SUPPORT_USER}"),
            InlineKeyboardButton("📊 𝐒𝐭𝐚𝐭𝐬", callback_data="stats")
        ],
        [
            InlineKeyboardButton("🎵 قناة السورس", url="https://t.me/C_R_B_X")
        ]
    ])
    
    await message.reply_video(
        video=START_VIDEO,
        caption=text,
        reply_markup=buttons
    )
    
