from pyrogram import Client, filters
from config import BOT_NAME

@Client.on_callback_query()
async def callbacks(client, query):
    data = query.data
    
    if data == "pause":
        # هنا يتم استدعاء أمر الإيقاف المؤقت من المكتبة
        await query.answer("⏸ تم الإيقاف المؤقت")
        await query.edit_message_caption(caption=f"<b>⏸ تم إيقاف التشغيل مؤقتاً\n💎 بواسطة: {BOT_NAME}</b>")
        
    elif data == "resume":
        await query.answer("▶️ تم الاستئناف")
        await query.edit_message_caption(caption=f"<b>▶️ تم استئناف التشغيل\n💎 بواسطة: {BOT_NAME}</b>")
        
    elif data == "stop":
        await query.answer("⏹ تم الإيقاف")
        await query.message.delete()
        await query.message.reply_text("<b>⏹ تم إنهاء التشغيل ومغادرة المكالمة.</b>")
      
