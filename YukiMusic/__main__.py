import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from YukiMusic import app, userbot
from YukiMusic.core.call import Anony
from YukiMusic.misc import sudo
from YukiMusic.plugins import ALL_MODULES
from YukiMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS
from .logging import LOGGER


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error(" Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("YukiMusic.plugins" + all_module)
    LOGGER("YukiMusic.plugins").info("✦ Successfully Imported Modules...")
    await userbot.start()
    await Anony.start()
    try:
        await Anony.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("YukiMusic").error(
            "✦ Please turn on the videochat of your log group\channel.\n\n✦ Stopping Bot...💣"
        )
        exit()
    except:
        pass
    await Anony.decorators()
    LOGGER("YukiMusic").info(
        "🄿🄰🅁🄰🄳🄾🅇"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("YukiMusic").info("❖ Stopping Makima Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
