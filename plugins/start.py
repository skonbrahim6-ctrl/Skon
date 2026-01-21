from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import START_VIDEO, SUPPORT_USER, BOT_NAME

@Client.on_message(filters.command("start") & filters.private)
async def start(client, message):
    # جلب يوزر البوت تلقائياً لضمان عمل رابط الإضافة
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

    # هنا جعلنا كل زر في قائمة مستقلة [ ] لكي يظهر تحت الآخر
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ أضف البوت لمجموعتك ➕", url=f"https://t.me/{bot_username}?startgroup=true")],
        [InlineKeyboardButton("👑 المطور (𝐃𝐞𝐯)", url=f"https://t.me/{SUPPORT_USER}")],
        [InlineKeyboardButton("📊 الإحصائيات (𝐒𝐭𝐚𝐭𝐬)", callback_data="stats")],
        [InlineKeyboardButton("🎵 قناة السورس", url="https://t.me/C_R_B_X")]
    ])
    
    try:
        # إرسال الفيديو مع النص والأزرار تحت بعضها
        await message.reply_video(
            video=START_VIDEO,
            caption=text,
            reply_markup=buttons
        )
    except Exception as e:
        # حل احتياطي إذا فشل الفيديو
        await message.reply_text(
            text=text,
            reply_markup=buttons
        )
        print(f"Error: {e}")
        
