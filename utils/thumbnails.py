import os
import aiohttp
import aiofiles

async def gen_thumb(videoid, title):
    url = f"https://img.youtube.com/vi/{videoid}/maxresdefault.jpg"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                f = await aiofiles.open(f"thumb{videoid}.jpg", mode="wb")
                await f.write(await resp.read())
                await f.close()
    return f"thumb{videoid}.jpg"
  
