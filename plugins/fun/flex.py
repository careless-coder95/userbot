import asyncio
import time
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from helpers import build_output, stylish
from config import DIVIDER, OWNER_TAG

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   Uptime tracker
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

START_TIME = time.time()

# AFK state
afk_state = {"active": False, "reason": "", "time": None}


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   .ᴀʟɪᴠᴇ — Check if userbot is running
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@Client.on_message(filters.me & filters.command("alive", prefixes="."))
async def alive_command(client, message):
    me = await client.get_me()
    uptime_sec = int(time.time() - START_TIME)
    h = uptime_sec // 3600
    m = (uptime_sec % 3600) // 60
    s = uptime_sec % 60

    text = (
        f"❁═════⟬ ꜱᴛᴀʀᴋ ᴜꜱᴇʀʙᴏᴛ ⟭═════❁\n\n"
        f"𝛅 𝛕 ⋏ ᰻⃪᱂ 𐌺 ⋆ ‹𝟹\n\n"
        f"• {stylish('STATUS')}  : Online ✅\n"
        f"• {stylish('USER')}    : [{me.first_name}](tg://user?id={me.id})\n"
        f"• {stylish('UPTIME')}  : `{h}h {m}m {s}s`\n"
        f"• {stylish('VERSION')} : `v1.0 by ᴍɪsᴛᴇʀ sᴛᴀʀᴋ`\n\n"
        f"⍣⃪‌ ᶦ ‌ᵃᵐ⛦⃕‌𝑫𝑬𝑽𝑰𝑳❛𝆺𝅥⤹࿗𓆪ꪾ™\n\n"
        f"{OWNER_TAG}"
    )
    await message.edit(text, disable_web_page_preview=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   .ᴘɪɴɢ — Response time check
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@Client.on_message(filters.me & filters.command("ping", prefixes="."))
async def ping_command(client, message):
    start = time.time()
    await message.edit("🏓 **ᴘɪɴɢɪɴɢ...**")
    ms = round((time.time() - start) * 1000, 2)
    result = (
        f"• {stylish('PING')}   : `{ms} ms` 🏓\n"
        f"• {stylish('STATUS')} : Online ✅"
    )
    await message.edit(build_output("❁═════⟬ ᴘɪɴɢ ⟭═════❁", result))


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   .ᴜᴘᴛɪᴍᴇ — How long running
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@Client.on_message(filters.me & filters.command("uptime", prefixes="."))
async def uptime_command(client, message):
    uptime_sec = int(time.time() - START_TIME)
    h = uptime_sec // 3600
    m = (uptime_sec % 3600) // 60
    s = uptime_sec % 60
    result = (
        f"• {stylish('UPTIME')}   : `{h}h {m}m {s}s` ⏱️\n"
        f"• {stylish('STARTED')}  : `{datetime.fromtimestamp(START_TIME).strftime('%d %b %Y %H:%M:%S')}`"
    )
    await message.edit(build_output("❁═════⟬ ᴜᴘᴛɪᴍᴇ ⟭═════❁", result))


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   .ɪᴅ — Get ID of chat / user
#   Usage: .id  OR  reply + .id
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@Client.on_message(filters.me & filters.command("id", prefixes="."))
async def id_command(client, message):
    chat    = message.chat
    lines   = [f"• {stylish('CHAT ID')} : `{chat.id}`"]

    if message.reply_to_message and message.reply_to_message.from_user:
        u = message.reply_to_message.from_user
        lines.append(f"• {stylish('USER ID')}   : `{u.id}`")
        lines.append(f"• {stylish('NAME')}       : {u.first_name}")
        lines.append(f"• {stylish('USERNAME')}   : @{u.username}" if u.username else f"• {stylish('USERNAME')}   : N/A")

    result = "\n".join(lines)
    await message.edit(build_output("❁═════⟬ ɪᴅ ɪɴꜰᴏ ⟭═════❁", result))


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   .ʙɪᴏ — Change your Telegram bio
#   Usage: .bio {new bio text}
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@Client.on_message(filters.me & filters.command("bio", prefixes="."))
async def bio_command(client, message):
    args = message.text.split(None, 1)
    if len(args) < 2:
        await message.edit("**ᴜꜱᴀɢᴇ:** `.bio {new bio}`")
        return
    new_bio = args[1].strip()
    await client.update_profile(bio=new_bio)
    result = f"• {stylish('BIO')} : {new_bio}\n• {stylish('STATUS')} : Updated ✅"
    await message.edit(build_output("❁═════⟬ ʙɪᴏ ᴜᴘᴅᴀᴛᴇᴅ ⟭═════❁", result))


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   .ᴀꜰᴋ — AFK mode with auto reply
#   Usage: .afk {reason}   to enable
#          .afk            to disable
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@Client.on_message(filters.me & filters.command("afk", prefixes="."))
async def afk_command(client, message):
    args = message.text.split(None, 1)

    if afk_state["active"]:
        afk_state["active"] = False
        afk_state["reason"] = ""
        gone = int(time.time() - afk_state["time"])
        m, s = gone // 60, gone % 60
        await message.edit(
            f"❁═════⟬ ᴀꜰᴋ ᴏꜰꜰ ⟭═════❁\n\n"
            f"• {stylish('WELCOME BACK')}!\n"
            f"• {stylish('GONE FOR')} : `{m}m {s}s`\n\n"
            f"{OWNER_TAG}"
        )
    else:
        reason = args[1].strip() if len(args) > 1 else "AFK 💤"
        afk_state["active"] = True
        afk_state["reason"] = reason
        afk_state["time"]   = time.time()
        await message.edit(
            f"❁═════⟬ ᴀꜰᴋ ᴏɴ ⟭═════❁\n\n"
            f"• {stylish('REASON')} : {reason}\n"
            f"• {stylish('STATUS')} : AFK Mode Active 💤\n\n"
            f"{OWNER_TAG}"
        )


@Client.on_message(~filters.me & (filters.private | filters.mentioned))
async def afk_reply(client, message):
    if not afk_state["active"]:
        return
    if message.from_user and message.from_user.is_self:
        return
    gone = int(time.time() - afk_state["time"])
    m, s = gone // 60, gone % 60
    await message.reply(
        f"🌙 ***ᴍᴀɪ ᴀʙʜɪ ᴀꜰᴋ ʜᴜɴ!***\n\n"
        f"• ***{stylish('REASON')}*** : _{afk_state['reason']}_\n"
        f"• ***{stylish('SINCE')}***  : `{m}m {s}s` pehle se\n\n"
        f"_{OWNER_TAG}_"
    )


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   .ɢʜᴏꜱᴛ — Delete your message after 5 seconds
#   Usage: .ghost {message}
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@Client.on_message(filters.me & filters.command("ghost", prefixes="."))
async def ghost_command(client, message):
    args = message.text.split(None, 1)
    if len(args) < 2:
        await message.edit("**ᴜꜱᴀɢᴇ:** `.ghost {text}` — message 5s baad delete ho jaega")
        return
    text = args[1].strip()
    await message.edit(text)
    await asyncio.sleep(5)
    await message.delete()
