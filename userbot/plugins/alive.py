"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba, check pinned in @deadpool_army"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**At Your Service Sir !! I'm Alive**\n\n"
                     "`Telethon version: 6.9.0\nPython: 3.7.3\nRepo by:` @xzendercage\n"
                     "`Bot created by:`Xzender Cage\n"
                     "`Database Status: Databases functioning normally!\n\nAlways with you, My Master!\n`"
                     f"`My peru owner`: Xzender Cage\n"
                     "[Deploy this userbot Now](https://github.com/xzendercage/cagehero)")
