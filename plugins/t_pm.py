#sahid malik
from plugins.malik.extra import G_FILTER
from info import PM_MAINTENANCE_MODE, AUTH_USERS
from pyrogram import Client, filters, enums 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton




@Client.on_message(filters.text & filters.private & filters.incoming)
async def give_filter(client, message):
    if PM_MAINTENANCE_MODE:
        content = message.text
        user = message.from_user.first_name
        user_id = message.from_user.id
        if content.startswith("/") or content.startswith("#"): return #
        await message.reply_text(text=(G_FILTER.format(message.from_user.mention)), reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⚡️ Backup Channel ⚡️",url="https://t.me/+FAgX05kGByNkZjJl"),]]),parse_mode=enums.ParseMode.HTML)#"You are now verified for next 24 hours. Continue asking movies")      


