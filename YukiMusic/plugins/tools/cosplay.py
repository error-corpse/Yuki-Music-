import requests
from pyrogram import filters
from pyrogram.types import Message,InlineKeyboardButton,InlineKeyboardMarkup
from pyrogram.enums import ChatAction
from  YukiMusic import app
from config import BOT_USERNAME


@app.on_message(filters.command("cosplay"))
async def cosplay(_,msg):
    img = requests.get("https://waifu-api.vercel.app").json()
    await msg.reply_photo(img, caption=f"Pervert")



@app.on_message(filters.command("ncosplay"))
async def ncosplay(_,msg):
    if msg.chat.type != ChatType.PRIVATE:
      await msg.reply_text(" sᴏʀʀʏ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ɪɴ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ ᴡɪᴛʜ ʙᴏᴛ",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("ɢᴏ ᴘᴍ",url=f"https://t.me/yukki_music_bot?start=True")]
            ]
        ))
    else:
       ncosplay = requests.get("https://waifu-api.vercel.app/items/1").json()


