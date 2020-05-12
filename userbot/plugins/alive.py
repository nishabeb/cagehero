"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "**No Name set yet.** [AI BY](tg://user?id=898096089)"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("ღღAt Your Service Mam i'm Aliveღღ\n\n"
                     "`Telethon version: 6.9.0\nPython: 3.7.3\nFork by:` @xzendercage\n"
                     "`Bot created by:` ★ 彡𝓝𝓲𝓼𝓱𝓪 𝓙𝓪𝓲𝓼𝔀𝓪𝓵彡★ \n"
                     "`Database Status: Databases functioning Normally!\n\nAlways with you, My Sister!\n`"
                     f"`My peru owner`: ★ 彡𝓝𝓲𝓼𝓱𝓪 𝓙𝓪𝓲𝓼𝔀𝓪𝓵彡★ \n"
                     "[Deploy this userbot Now](https://github.com/xzendercage/cagehero)")
