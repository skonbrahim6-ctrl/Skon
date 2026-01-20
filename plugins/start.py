from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import START_VIDEO, SUPPORT_USER, BOT_USERNAME

@Client.on_message(filters.command("start") & filters.private)
async def start(client, message):
    text = f"""
<b>✧━━━━━━━━━━━━━━✧</b>
<b> 𝐒𝐏𝐎𝐓𝐈 𝐌𝐔𝐒𝐈𝐂 🎶 </b>
<b>✧━━━━━━━━━━━━━━✧</b>

<b>أهلاً بك يا {message.from_user.mention} في عالم الموسيقى الفخم..</b>

<b>أنـا بوت {BOT_USERNAME}.. أقوى وأسرع مشغل موسيقى في التيليجرام ⚡️</b>

<b>• أستطيع تشغيل الأغاني والڤيديوهات بجودة عالية 🔊</b>
<b>• أدعم القنوات والمجموعات بدون انقطاع 🛡</b>
<b>• تم تطويري بأحدث التقنيات البرمجية لتجربة استماع لا مثيل لها 💎</b>

<b>اسـتمر في اكتشاف الفخامة عبر الأزرار أدناه 👇</b>
"""
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("ضيف البوت لمجموعتك ✨", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
            InlineKeyboardButton("𝐃𝐞𝐯 👑", url=f"https://t.me/C_R_B_X")
        ]
    ])
    
    await message.reply_video(
        video=START_VIDEO,
        caption=text,
        reply_markup=buttons
    )
  
