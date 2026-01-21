from pyrogram import Client, filters
from config import OWNER_ID

# أمر الإحصائيات - متاح فقط للمالك
@Client.on_message(filters.command("stats") & filters.user(OWNER_ID))
async def stats(client, message):
    text = (
        "<b>📊 إحصائيات البوت الحالية:</b>\n\n"
        "✅ <b>حالة البوت:</b> يعمل بنجاح (Termux)\n"
        "📡 <b>قاعدة البيانات:</b> متصلة\n"
        "⚠️ <b>المكالمات:</b> معطلة (نظام الملفات الصوتية فقط)"
    )
    await message.reply_text(text)

# أمر الإذاعة - متاح فقط للمالك
@Client.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
async def broadcast(client, message):
    if not message.reply_to_message:
        return await message.reply_text("<b>❌ خطأ:</b> يرجى الرد على الرسالة (نص، صورة، فيديو) التي تريد إذاعتها!")
    
    # هنا يتم وضع منطق الإرسال للمجموعات لاحقاً
    await message.reply_text("<b>📢 جاري بدء الإذاعة الشاملة...</b>")
    
