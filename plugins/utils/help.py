from pyrogram import Client, filters
from config import DIVIDER, OWNER_TAG
from helpers import stylish

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   HELP MENU DATA
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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
            (".kick {reply/@user}",   "User kick karo"),
            (".ban {reply/@user}",    "User ban karo"),
            (".unban @user",          "User unban karo"),
            (".mute {reply}",         "User mute karo"),
            (".unmute {reply}",       "User unmute karo"),
            (".pin {reply}",          "Message pin karo"),
            (".purge {reply}",        "Messages purge karo"),
            (".promote {reply}",      "User ko admin banao"),
            (".demote {reply}",       "Admin rights hatao"),
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
            (".ping",    "Response time check"),
            (".uptime",  "Kitne time se chal raha"),
            (".id",      "Chat / user ID nikalo"),
        ]
    },
}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def format_category(key):
    cat = HELP_MENU[key]
    lines = [f"{cat['emoji']} {stylish(cat['title'])}"]
    lines.append(DIVIDER)
    for cmd, desc in cat["commands"]:
        lines.append(f"  • `{cmd}`\n    ↳ _{desc}_")
    return "\n".join(lines)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   .ʜᴇʟᴘ — Show all commands
#   Usage: .help              → all categories overview
#          .help {category}   → detailed commands
#   Categories: osint, utils, group, fun, stats
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@Client.on_message(filters.me & filters.command("help", prefixes="."))
async def help_command(client, message):
    args = message.text.split(None, 1)

    # .help {category}
    if len(args) > 1:
        key = args[1].strip().lower()
        if key not in HELP_MENU:
            cats = " | ".join(HELP_MENU.keys())
            await message.edit(f"❌ **Category nahi mili!**\n\n**Available:** `{cats}`")
            return

        text = (
            f"❁═════⟬ ʜᴇʟᴘ : {HELP_MENU[key]['title']} ⟭═════❁\n\n"
            f"{format_category(key)}\n\n"
            f"{DIVIDER}\n\n"
            f"{OWNER_TAG}"
        )
        await message.edit(text)
        return

    # .help — overview of all categories
    lines = [
        f"❁═════⟬ ꜱᴛᴀʀᴋ ᴜꜱᴇʀʙᴏᴛ ʜᴇʟᴘ ⟭═════❁\n",
        f"𝛅 𝛕 ⋏ ᰻⃪᱂ 𐌺 ⋆ ‹𝟹  ***ʙʏ ᴍɪsᴛᴇʀ sᴛᴀʀᴋ***\n",
        f"{DIVIDER}\n",
    ]

    for key, cat in HELP_MENU.items():
        count = len(cat["commands"])
        lines.append(f"{cat['emoji']} ***{stylish(cat['title'])}*** — `{count} commands`")
        lines.append(f"   ↳ `.help {key}` for details\n")

    lines.append(DIVIDER)
    lines.append(f"\n{OWNER_TAG}")

    await message.edit("\n".join(lines))
