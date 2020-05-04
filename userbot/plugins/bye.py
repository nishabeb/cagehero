# For @UniBorg
# Courtesy @yasirsiddiqui

"""
.bye
"""
from telethon.tl.functions.channels import LeaveChannelRequest
from userbot.utils import admin_cmd
import time

@borg.on(admin_cmd("bye", outgoing=True))
async def leave(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`jaa rha hu Ye Ganduh Jgha Chord Ke.....!`")
        time.sleep(3)
        if '-' in str(e.chat_id):
            await borg(LeaveChannelRequest(e.chat_id))
        else:
            await e.edit('`Abe Lwde Ye Chat Ni Hai`')
