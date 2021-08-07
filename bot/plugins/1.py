#import logging
#logger = logging.getLogger(__name__)

import datetime
from bot import UPDATE_CHANNEL, BOT_USERNAME
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant, ChatAdminRequired, UsernameNotOccupied


@Client.on_message(filters.private & filters.incoming)
async def force_sub(c, m):
    if UPDATE_CHANNEL:
        try:
            chat = await c.get_chat_member(UPDATE_CHANNEL, m.from_user.id)
            if chat.status=='kicked':
                return await m.reply_text('Hai you are kicked from my updates channel. So, you are not able to use me',  quote=True)

        except UserNotParticipant:
            button = [[
                InlineKeyboardButton('join Updates channel', url=f'https://t.me/{UPDATE_CHANNEL}')
                ],[
                InlineKeyboardButton('🔄 Refresh 🔄', url=f'https://t.me/{BOT_USERNAME}?start')
            ]]
            markup = InlineKeyboardMarkup(button)
            return await m.reply_text(text="Hey join in my updates channel to use me.", parse_mode='markdown', reply_markup=markup, quote=True)

        except ChatAdminRequired:
            logger.warning(f"Make me admin in @{UPDATE_CHANNEL}")
            if m.from_user.id in Config.AUTH_USERS:
                return await m.reply_text(f"Make me admin in @{UPDATE_CHANNEL}")

    await m.continue_propagation()
