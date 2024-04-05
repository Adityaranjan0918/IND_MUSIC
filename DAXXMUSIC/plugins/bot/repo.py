from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DAXXMUSIC import app
from config import BOT_USERNAME

start_txt = """
Phir tu repo lene agaya repo k jagah me tera rape kar duga chal bhag

sun jate jate mera group join karle @THE_IND_CODERS

or channel bhi join karle na bhag na mat @THE_IND_CODER.

chal ab ja bhag bdk. """




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [
          InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/the_ind_coders"),
          InlineKeyboardButton("ʀᴇᴘᴏ", url="https://t.me/itz_aditya_the_king"),
          ],
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/33bc093c89898dcc318ae.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
