from pyrogram import Client, filters

@Client.on_message(filters.regex("^(بوت|البوت)$") & filters.group)
async def bot_reply(client, message):
    await message.reply_text("<b>عيوني للبوت، أمرني وش محتاج تشغل؟ 🎶</b>")

@Client.on_message(filters.regex("^(سورس|السورس)$") & filters.group)
async def source_reply(client, message):
    await message.reply_text("<b>سورس 𝐒𝐏𝐎𝐓𝐈 𝐌𝐔𝐒𝐈𝐂 الفخم، تابع التحديثات هنا: @C_R_B_X</b>")
  
