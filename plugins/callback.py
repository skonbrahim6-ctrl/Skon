from pyrogram import Client, filters
from config import BOT_NAME

@Client.on_callback_query()
async def callbacks(client, query):
    data = query.data
    
    if data == "pause":
        # في نظام الملفات، لا يمكننا عمل Pause للملف المرسل، لذا سنخبر المستخدم بذلك
        await query.answer("⚠️ هذا الزر مخصص لنظام المكالمات فقط.", show_alert=True)
        
    elif data == "resume":
        await query.answer("⚠️ هذا الزر مخصص لنظام المكالمات فقط.", show_alert=True)
        
    elif data == "stop":
        # حذف رسالة التحكم
        await query.answer("⏹ تم إغلاق القائمة")
        await query.message.delete()
        
    elif data == "close":
        await query.message.delete()
        await query.answer("❌ تم الإغلاق")
        
