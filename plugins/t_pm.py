#sahid malik
from plugins.malik.extra import G_FILTER
from info import PM_MAINTENANCE_MODE, PM_MAINTENANCE_MODE2, LOG_CHANNEL
from pyrogram import Client, filters, enums 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(filters.text & filters.private & filters.incoming)
async def give_text(client, message):
    if PM_MAINTENANCE_MODE:
        content = message.text
        user = message.from_user.mention
        if content.startswith("/") return #
        await message.reply_text(text=(G_FILTER.format(user)), reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⚡️ Backup Channel ⚡️",url="https://t.me/+FAgX05kGByNkZjJl"),]]),parse_mode=enums.ParseMode.HTML)  
        



