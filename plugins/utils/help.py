from pyrogram import Client, filters, enums
from config import DIVIDER, OWNER_TAG
from helpers import stylish

HELP_MENU = {
    "osint": {
        "emoji": "🔍",
        "title": "ᴏꜱɪɴᴛ",
        "commands": [
            (".num {number}",        "Phone number lookup"),
            (".tg {userid/reply}",   "Telegram ID lookup"),
            (".whois {reply/@user}", "User info from Telegram"),
        ]
    },
    "utils": {
        "emoji": "🛠️",
        "title": "ᴜᴛɪʟꜱ",
        "commands": [
            (".qr",                  "Apna QR code bhejo"),
            (".spam {text} {times}", "Message spam karo"),
            (".tr {lang} {text}",    "Text translate karo"),
            (".tts {text/reply}",    "Text to Speech voice"),
            (".calc {expression}",   "Calculator"),
        ]
    },
    "group": {
        "emoji": "👥",
        "title": "ɢʀᴏᴜᴘ ᴛᴏᴏʟꜱ",
        "commands": [
            (".kick {reply/@user}",  "User kick karo"),
            (".ban {reply/@user}",   "User ban karo"),
            (".unban @user",         "User unban karo"),
            (".mute {reply}",        "User mute karo"),
            (".unmute {reply}",      "User unmute karo"),
            (".pin {reply}",         "Message pin karo"),
            (".purge {reply}",       "Messages purge karo"),
            (".promote {reply}",     "User ko admin banao"),
            (".demote {reply}",      "Admin rights hatao"),
        ]
    },
    "fun": {
        "emoji": "😎",
        "title": "ꜰᴜɴ & ꜰʟᴇx",
        "commands": [
            (".alive",               "Userbot alive check"),
            (".afk {reason}",        "AFK mode on/off"),
            (".ghost {text}",        "5s baad delete"),
            (".bio {text}",          "Apni bio change karo"),
            (".tagall {text}",       "Sabko tag karo"),
            (".gmtag",               "Good Morning tag"),
            (".gntag",               "Good Night tag"),
        ]
    },
    "stats": {
        "emoji": "📊",
        "title": "ꜱᴛᴀᴛꜱ",
        "commands": [
            (".ping",   "Response time check"),
            (".uptime", "Kitne time se chal raha"),
            (".id",     "Chat / user ID nikalo"),
        ]
    },
}


def format_category(key):
    cat = HELP_MENU[key]
    lines = [f"{cat['emoji']} {stylish(cat['title'])}"]
    lines.append(DIVIDER)
    for cmd, desc in cat["commands"]:
        lines.append(f"  • {cmd:<28}  {desc}")
    return "\n".join(lines)


@Client.on_message(filters.me & filters.command("help", prefixes="."))
async def help_command(client, message):
    args = message.text.split(None, 1)

    # .help {category}
    if len(args) > 1:
        key = args[1].strip().lower()
        if key not in HELP_MENU:
            cats = " | ".join(HELP_MENU.keys())
            await message.edit(
                f"❌ **Category nahi mili!**\n\nAvailable: `{cats}`",
                parse_mode=enums.ParseMode.MARKDOWN
            )
            return

        body = format_category(key)
        text = (
            f"```\n"
            f"❁═════⟬ ʜᴇʟᴘ : {HELP_MENU[key]['title']} ⟭═════❁\n\n"
            f"{body}\n\n"
            f"{OWNER_TAG}\n"
            f"```"
        )
        await message.edit(text, parse_mode=enums.ParseMode.MARKDOWN)
        return

    # .help — overview
    body_lines = []
    for key, cat in HELP_MENU.items():
        count = len(cat["commands"])
        body_lines.append(f"{cat['emoji']}  {stylish(cat['title']):<20}  {count} commands")
        body_lines.append(f"    .help {key}")
        body_lines.append("")

    body = "\n".join(body_lines).strip()
    header = (
        f"ꜱᴛᴀʀᴋ ᴜꜱᴇʀʙᴏᴛ"
    )
    text = (
        f"```\n"
        f"❁═════⟬ ʜᴇʟᴘ ᴍᴇɴᴜ ⟭═════❁\n\n"
        f"{header}\n\n"
        f"{DIVIDER}\n\n"
        f"{body}\n\n"
        f"{OWNER_TAG}\n"
        f"```"
    )
    await message.edit(text, parse_mode=enums.ParseMode.MARKDOWN)

