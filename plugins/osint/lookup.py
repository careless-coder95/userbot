from pyrogram import Client, filters, enums
from config import NUM_API_URL, TG_API_URL, TG_API_KEY, OWNER_TAG, DIVIDER
from helpers import call_api, remove_branding, format_response, stylish


def code_block(title, body):
    return (
        f"```\n"
        f"{title}\n\n"
        f"{body}\n\n"
        f"{OWNER_TAG}\n"
        f"```"
    )

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   .num — Phone Number Lookup
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@Client.on_message(filters.me & filters.command("num", prefixes="."))
async def num_command(client, message):
    args = message.text.split(None, 1)
    if len(args) < 2 or not args[1].strip():
        await message.edit(
            "**ᴜꜱᴀɢᴇ:** `.num {number}`",
            parse_mode=enums.ParseMode.MARKDOWN
        )
        return

    number = args[1].strip()
    await message.edit(f"🔎 **ꜱᴇᴀʀᴄʜɪɴɢ...** `{number}`", parse_mode=enums.ParseMode.MARKDOWN)

    data = await call_api(f"{NUM_API_URL}{number}")
    if not data:
        await message.edit("❌ **ɴᴏ ʀᴇꜱᴜʟᴛ ꜰᴏᴜɴᴅ**", parse_mode=enums.ParseMode.MARKDOWN)
        return

    body = format_response(remove_branding(data))
    text = code_block("❁═════⟬ ɴᴜᴍʙᴇʀ ɪɴꜰᴏ ⟭═════❁", body)
    await message.edit(text, parse_mode=enums.ParseMode.MARKDOWN)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   .tg — Telegram ID Lookup
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
            await message.edit(
                "**ᴜꜱᴀɢᴇ:** `.tg {userid}` ʏᴀ ʀᴇᴘʟʏ ᴋᴀʀᴋᴇ `.tg`",
                parse_mode=enums.ParseMode.MARKDOWN
            )
            return
        user_id = args[1].strip()

    await message.edit(f"🔎 **ꜱᴇᴀʀᴄʜɪɴɢ...** `{user_id}`", parse_mode=enums.ParseMode.MARKDOWN)

    data = await call_api(f"{TG_API_URL}{user_id}&key={TG_API_KEY}")
    if not data:
        await message.edit("❌ **ɴᴏ ʀᴇꜱᴜʟᴛ ꜰᴏᴜɴᴅ**", parse_mode=enums.ParseMode.MARKDOWN)
        return

    body = format_response(remove_branding(data))
    text = code_block("❁═════⟬ ᴛᴇʟᴇɢʀᴀᴍ ɪɴꜰᴏ ⟭═════❁", body)
    await message.edit(text, parse_mode=enums.ParseMode.MARKDOWN)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   .whois — User Info from Telegram
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
                await message.edit("❌ **ᴜꜱᴇʀ ɴᴏᴛ ꜰᴏᴜɴᴅ**", parse_mode=enums.ParseMode.MARKDOWN)
                return
        else:
            await message.edit(
                "**ᴜꜱᴀɢᴇ:** ʀᴇᴘʟʏ ᴋᴀʀᴋᴇ `.whois` ʏᴀ `.whois @username`",
                parse_mode=enums.ParseMode.MARKDOWN
            )
            return

    uid       = target.id
    fname     = target.first_name or "N/A"
    lname     = target.last_name or ""
    full_name = f"{fname} {lname}".strip()
    username  = f"@{target.username}" if target.username else "N/A"
    is_bot    = "Yes" if target.is_bot else "No"
    is_fake   = "Yes" if target.is_fake else "No"
    is_scam   = "Yes" if target.is_scam else "No"
    dc        = target.dc_id if target.dc_id else "N/A"

    body = (
        f"• {stylish('USER ID')}   : {uid}\n"
        f"• {stylish('NAME')}      : {full_name}\n"
        f"• {stylish('USERNAME')}  : {username}\n"
        f"• {stylish('DC')}        : {dc}\n"
        f"• {stylish('BOT')}       : {is_bot}\n"
        f"• {stylish('FAKE')}      : {is_fake}\n"
        f"• {stylish('SCAM')}      : {is_scam}"
    )
    text = code_block("❁═════⟬ ᴡʜᴏɪꜱ ɪɴꜰᴏ ⟭═════❁", body)
    await message.edit(text, parse_mode=enums.ParseMode.MARKDOWN, disable_web_page_preview=True)
