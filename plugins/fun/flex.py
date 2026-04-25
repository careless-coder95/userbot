import asyncio
import time
from datetime import datetime
from pyrogram import Client, filters, enums
from helpers import build_output, stylish
from config import DIVIDER, OWNER_TAG

START_TIME = time.time()
afk_state  = {"active": False, "reason": "", "time": None}


def code_block(title, body):
    return (
        f"{title}\n"
        f"```\n"
        f"{body}\n"
        f"```\n"
        f"{OWNER_TAG}"
    )


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   .alive
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@Client.on_message(filters.me & filters.command("alive", prefixes="."))
async def alive_command(client, message):
    me = await client.get_me()
    sec = int(time.time() - START_TIME)
    h, m, s = sec // 3600, (sec % 3600) // 60, sec % 60

    text = (
        f"```\n"
        f"❁═════⟬ ꜱᴛᴀʀᴋ ᴜꜱᴇʀʙᴏᴛ ⟭═════❁\n\n"
        f"{DIVIDER}\n\n"
        f"• {stylish('STATUS')}  : Online\n"
        f"• {stylish('USER')}    : {me.first_name}\n"
        f"• {stylish('UPTIME')}  : {h}h {m}m {s}s\n"
        f"• {stylish('VERSION')} : v1.0 by MISTER STARK\n\n"
        f"{OWNER_TAG}\n"
        f"```"
    )

    await message.edit(text, parse_mode=enums.ParseMode.MARKDOWN)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   .ping
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@Client.on_message(filters.me & filters.command("ping", prefixes="."))
async def ping_command(client, message):
    start = time.time()
    await message.edit("🏓 **ᴘɪɴɢɪɴɢ...**", parse_mode=enums.ParseMode.MARKDOWN)
    ms = round((time.time() - start) * 1000, 2)

    text = (
        f"```\n"
        f"❁═════⟬ ᴘɪɴɢ ⟭═════❁\n\n"
        f"• {stylish('PING')}   : {ms} ms\n"
        f"• {stylish('STATUS')} : Online\n\n"
        f"{OWNER_TAG}\n"
        f"```"
    )

    await message.edit(text, parse_mode=enums.ParseMode.MARKDOWN)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   .uptime
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@Client.on_message(filters.me & filters.command("uptime", prefixes="."))
async def uptime_command(client, message):
    sec = int(time.time() - START_TIME)
    h, m, s = sec // 3600, (sec % 3600) // 60, sec % 60

    text = (
        f"```\n"
        f"❁═════⟬ ᴜᴘᴛɪᴍᴇ ⟭═════❁\n\n"
        f"• {stylish('UPTIME')}  : {h}h {m}m {s}s\n"
        f"• {stylish('STARTED')} : {datetime.fromtimestamp(START_TIME).strftime('%d %b %Y %H:%M:%S')}\n\n"
        f"{OWNER_TAG}\n"
        f"```"
    )

    await message.edit(text, parse_mode=enums.ParseMode.MARKDOWN)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   .id
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@Client.on_message(filters.me & filters.command("id", prefixes="."))
async def id_command(client, message):
    chat = message.chat

    lines = [f"• {stylish('CHAT ID')} : {chat.id}"]

    if message.reply_to_message and message.reply_to_message.from_user:
        u = message.reply_to_message.from_user
        lines.append(f"• {stylish('USER ID')}  : {u.id}")
        lines.append(f"• {stylish('NAME')}     : {u.first_name}")
        lines.append(
            f"• {stylish('USERNAME')} : @{u.username}" 
            if u.username else 
            f"• {stylish('USERNAME')} : N/A"
        )

    body = "\n".join(lines)

    text = (
        f"```\n"
        f"❁═════⟬ ɪᴅ ɪɴꜰᴏ ⟭═════❁\n\n"
        f"{body}\n\n"
        f"{OWNER_TAG}\n"
        f"```"
    )

    await message.edit(text, parse_mode=enums.ParseMode.MARKDOWN)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   .bio
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@Client.on_message(filters.me & filters.command("bio", prefixes="."))
async def bio_command(client, message):
    args = message.text.split(None, 1)
    if len(args) < 2:
        await message.edit("**ᴜꜱᴀɢᴇ:** `.bio {new bio}`", parse_mode=enums.ParseMode.MARKDOWN)
        return

    new_bio = args[1].strip()
    await client.update_profile(bio=new_bio)

    text = (
        f"```\n"
        f"❁═════⟬ ʙɪᴏ ᴜᴘᴅᴀᴛᴇᴅ ⟭═════❁\n\n"
        f"• {stylish('BIO')}    : {new_bio}\n"
        f"• {stylish('STATUS')} : Updated\n\n"
        f"{OWNER_TAG}\n"
        f"```"
    )

    await message.edit(text, parse_mode=enums.ParseMode.MARKDOWN)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   .afk
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@Client.on_message(filters.me & filters.command("afk", prefixes="."))
async def afk_command(client, message):
    args = message.text.split(None, 1)

    if afk_state["active"]:
        afk_state["active"] = False
        gone = int(time.time() - afk_state["time"])
        gm, gs = gone // 60, gone % 60

        text = (
            f"```\n"
            f"❁═════⟬ ᴀꜰᴋ ᴏꜰꜰ ⟭═════❁\n\n"
            f"• {stylish('STATUS')}   : Back Online\n"
            f"• {stylish('GONE FOR')} : {gm}m {gs}s\n\n"
            f"{OWNER_TAG}\n"
            f"```"
        )

    else:
        reason = args[1].strip() if len(args) > 1 else "AFK"
        afk_state["active"] = True
        afk_state["reason"] = reason
        afk_state["time"]   = time.time()

        text = (
            f"```\n"
            f"❁═════⟬ ᴀꜰᴋ ᴏɴ ⟭═════❁\n\n"
            f"• {stylish('STATUS')} : AFK Mode Active\n"
            f"• {stylish('REASON')} : {reason}\n\n"
            f"{OWNER_TAG}\n"
            f"```"
        )

    await message.edit(text, parse_mode=enums.ParseMode.MARKDOWN)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# AFK AUTO REPLY
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@Client.on_message(~filters.me & (filters.private | filters.mentioned))
async def afk_reply(client, message):
    if not afk_state["active"]:
        return
    if message.from_user and message.from_user.is_self:
        return

    gone = int(time.time() - afk_state["time"])
    gm, gs = gone // 60, gone % 60

    text = (
        f"```\n"
        f"❁═════⟬ ᴀꜰᴋ ⟭═════❁\n\n"
        f"• {stylish('STATUS')} : AFK\n"
        f"• {stylish('REASON')} : {afk_state['reason']}\n"
        f"• {stylish('SINCE')}  : {gm}m {gs}s pehle se\n\n"
        f"{OWNER_TAG}\n"
        f"```"
    )

    await message.reply(text, parse_mode=enums.ParseMode.MARKDOWN)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   .ghost
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@Client.on_message(filters.me & filters.command("ghost", prefixes="."))
async def ghost_command(client, message):
    args = message.text.split(None, 1)
    if len(args) < 2:
        await message.edit(
            "**ᴜꜱᴀɢᴇ:** `.ghost {text}` — message 5s baad delete ho jaega",
            parse_mode=enums.ParseMode.MARKDOWN
        )
        return

    text = (
        f"```\n"
        f"{args[1].strip()}\n"
        f"```"
    )

    await message.edit(text, parse_mode=enums.ParseMode.MARKDOWN)
    await asyncio.sleep(5)
    await message.delete()

