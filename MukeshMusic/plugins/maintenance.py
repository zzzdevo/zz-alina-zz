from pyrogram import filters
from pyrogram.types import Message

from strings import get_command, get_string
from MukeshMusic import app
from MukeshMusic.misc import SUDOERS
from MukeshMusic.utils.database import (get_lang, is_maintenance,
                                       maintenance_off,
                                       maintenance_on)
from MukeshMusic.utils.decorators.language import language

# Commands
MAINTENANCE_COMMAND = get_command("MAINTENANCE_COMMAND")
from config import OWNER_ID

@app.on_message(filters.command(MAINTENANCE_COMMAND) & filters.user(OWNER_ID))
async def maintenance(client, message: Message):
    try:
        language = await get_lang(message.chat.id)
        _ = get_string(language)
    except:
        _ = get_string("en")
    usage = _["maint_1"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    message.chat.id
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        if await is_maintenance() is False:
            await message.reply_text(
                "ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ ᴍᴏᴅᴇ ɪs ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ."
            )
        else:
            await maintenance_on()
            await message.reply_text(_["maint_2"])
    elif state == "disable":
        if await is_maintenance() is False:
            await maintenance_off()
            await message.reply_text(_["maint_3"])
        else:
            await message.reply_text(
                "ɪ ᴅᴏɴ'ᴛ ʀᴇᴍᴇᴍʙᴇʀ ᴛʜᴀᴛ ʏᴏᴜ ᴇɴᴀʙʟᴇᴅ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ ᴍᴏᴅᴇ."
            )
    else:
        await message.reply_text(usage)
