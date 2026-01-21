from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# استيراد الإعدادات من ملف config
from config import START_VIDEO, SUPPORT_USER, BOT_NAME

@Client.on_message(filters.command("start") & filters.private)
async def start(client, message):
    bot_me = await client.get_me()
    bot_username = bot_me.username
    
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
        [InlineKeyboardButton("➕ أضف البوت لمجموعتك ➕", url=f"https://t.me/{bot_username}?startgroup=true")],
        [InlineKeyboardButton("👑 المطور (𝐃𝐞𝐯)", url=f"https://t.me/{SUPPORT_USER}")],
        [InlineKeyboardButton("📊 الإحصائيات (𝐒𝐭𝐚𝐭𝐬)", callback_data="stats")],
        [InlineKeyboardButton("🎵 قناة السورس", url="https://t.me/C_R_B_X")]
    ])
    
    # محاولة إرسال الفيديو
    try:
        await message.reply_video(
            video=START_VIDEO, # هذا هو السطر المسؤول عن إرسال الفيديو
            caption=text,
            reply_markup=buttons
        )
    except Exception as e:
        # إذا فشل إرسال الفيديو (بسبب الرابط)، سيرسل النص والأزرار فقط
        await message.reply_text(
            text=text,
            reply_markup=buttons
        )
        print(f"خطأ في إرسال الفيديو: {e}")
        
