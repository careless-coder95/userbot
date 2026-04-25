from pyrogram import Client, filters
from config import NUM_API_URL, TG_API_URL, TG_API_KEY
from helpers import call_api, remove_branding, format_response, build_output

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   .ɴᴜᴍ — Phone Number Lookup
#   Usage: .num 9876543210
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@Client.on_message(filters.me & filters.command("num", prefixes="."))
async def num_command(client, message):
    args = message.text.split(None, 1)
    if len(args) < 2 or not args[1].strip():
        await message.edit("**ᴜꜱᴀɢᴇ:** `.num {number}`")
        return

    number = args[1].strip()
    await message.edit(f"🔎 **ꜱᴇᴀʀᴄʜɪɴɢ...** `{number}`")

    data = await call_api(f"{NUM_API_URL}{number}")
    if not data:
        await message.edit("❌ **ɴᴏ ʀᴇꜱᴜʟᴛ ꜰᴏᴜɴᴅ**")
        return

    result = format_response(remove_branding(data))
    await message.edit(build_output("❁═════⟬ ɴᴜᴍʙᴇʀ ɪɴꜰᴏ ⟭═════❁", result))


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   .ᴛɢ — Telegram ID Lookup
#   Usage: .tg {userid}  OR  reply + .tg
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@Client.on_message(filters.me & filters.command("tg", prefixes="."))
async def tg_command(client, message):
    user_id = None

    if message.reply_to_message:
        replied = message.reply_to_message
        if replied.from_user:
            user_id = replied.from_user.id
        elif replied.sender_chat:
            user_id = replied.sender_chat.id
    else:
        args = message.text.split(None, 1)
        if len(args) < 2 or not args[1].strip():
            await message.edit("**ᴜꜱᴀɢᴇ:** `.tg {userid}` ʏᴀ ʀᴇᴘʟʏ ᴋᴀʀᴋᴇ `.tg`")
            return
        user_id = args[1].strip()

    await message.edit(f"🔎 **ꜱᴇᴀʀᴄʜɪɴɢ...** `{user_id}`")

    data = await call_api(f"{TG_API_URL}{user_id}&key={TG_API_KEY}")
    if not data:
        await message.edit("❌ **ɴᴏ ʀᴇꜱᴜʟᴛ ꜰᴏᴜɴᴅ**")
        return

    result = format_response(remove_branding(data))
    await message.edit(build_output("❁═════⟬ ᴛᴇʟᴇɢʀᴀᴍ ɪɴꜰᴏ ⟭═════❁", result))


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   .ᴡʜᴏɪꜱ — User Info from Telegram itself
#   Usage: reply + .whois
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@Client.on_message(filters.me & filters.command("whois", prefixes="."))
async def whois_command(client, message):
    target = None

    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user
    else:
        args = message.text.split(None, 1)
        if len(args) > 1:
            try:
                target = await client.get_users(args[1].strip())
            except Exception:
                await message.edit("❌ **ᴜꜱᴇʀ ɴᴏᴛ ꜰᴏᴜɴᴅ**")
                return
        else:
            await message.edit("**ᴜꜱᴀɢᴇ:** ʀᴇᴘʟʏ ᴋᴀʀᴋᴇ `.whois` ʏᴀ `.whois @username`")
            return

    from helpers import stylish, DIVIDER
    from config import OWNER_TAG

    uid       = target.id
    fname     = target.first_name or "N/A"
    lname     = target.last_name or ""
    full_name = f"{fname} {lname}".strip()
    username  = f"@{target.username}" if target.username else "N/A"
    is_bot    = "✅ Yes" if target.is_bot else "❌ No"
    is_fake   = "⚠️ Yes" if target.is_fake else "❌ No"
    is_scam   = "⚠️ Yes" if target.is_scam else "❌ No"
    dc        = target.dc_id if target.dc_id else "N/A"
    mention   = f"[{full_name}](tg://user?id={uid})"

    lines = [
        f"• {stylish('USER ID')} : `{uid}`",
        f"• {stylish('NAME')} : {full_name}",
        f"• {stylish('USERNAME')} : {username}",
        f"• {stylish('MENTION')} : {mention}",
        f"• {stylish('DC')} : {dc}",
        f"• {stylish('BOT')} : {is_bot}",
        f"• {stylish('FAKE')} : {is_fake}",
        f"• {stylish('SCAM')} : {is_scam}",
    ]

    result = "\n".join(lines)
    text = (
        f"❁═════⟬ ᴡʜᴏɪꜱ ɪɴꜰᴏ ⟭═════❁\n"
        f"{DIVIDER}\n"
        f"{result}\n"
        f"{DIVIDER}\n\n"
        f"{OWNER_TAG}"
    )
    await message.edit(text, disable_web_page_preview=True)
