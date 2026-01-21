import os
import aiohttp
import aiofiles

async def gen_thumb(videoid, title):
    # رابط الصورة المصغرة لليوتيوب
    url = f"https://img.youtube.com/vi/{videoid}/maxresdefault.jpg"
    thumb_path = f"downloads/thumb{videoid}.jpg"
    
    # التأكد من وجود مجلد downloads
    if not os.path.exists("downloads"):
        os.makedirs("downloads")

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                # إذا لم تتوفر الجودة العالية، نجرب الجودة العادية
                url = f"https://img.youtube.com/vi/{videoid}/0.jpg"
                async with session.get(url) as resp_alt:
                    if resp_alt.status == 200:
                        f = await aiofiles.open(thumb_path, mode="wb")
                        await f.write(await resp_alt.read())
                        await f.close()
                    else:
                        return None # فشل جلب الصورة
            else:
                f = await aiofiles.open(thumb_path, mode="wb")
                await f.write(await resp.read())
                await f.close()
                
    return thumb_path
    
