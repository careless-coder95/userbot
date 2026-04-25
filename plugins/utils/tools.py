import asyncio
import os
from pyrogram import Client, filters
from config import QR_IMAGE_PATH, OWNER_TAG, DIVIDER
from helpers import stylish

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   .ǫʀ — Send Your QR Code
#   Usage: .qr
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@Client.on_message(filters.me & filters.command("qr", prefixes="."))
async def qr_command(client, message):
    if not os.path.exists(QR_IMAGE_PATH):
        await message.edit("❌ **QR image nahi mili!** `assets/qr.jpg` mein rakhna.")
        return

    await message.delete()
    await client.send_photo(
        chat_id=message.chat.id,
        photo=QR_IMAGE_PATH,
        caption=(
            f"❁═⟬ ᴍʏ ǫʀ ᴄᴏᴅᴇ ⟭═❁\n"
            f"❁═⟬ ᴍɪsᴛᴇʀ sᴛᴀʀᴋ ⟭═❁"
        )
    )


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   .ꜱᴘᴀᴍ — Spam a message N times
#   Usage: .spam {text} {times}
#   Example: .spam Hello bro 5
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@Client.on_message(filters.me & filters.command("spam", prefixes="."))
async def spam_command(client, message):
    args = message.text.split(None, 1)

    if len(args) < 2:
        await message.edit("**ᴜꜱᴀɢᴇ:** `.spam {text} {times}`\n**ᴇxᴀᴍᴘʟᴇ:** `.spam Hello bro 5`")
        return

    parts = args[1].rsplit(None, 1)
    if len(parts) < 2 or not parts[1].isdigit():
        await message.edit("❌ **Aakhir mein number likhna!**\n**ᴇxᴀᴍᴘʟᴇ:** `.spam Hello bro 5`")
        return

    text  = parts[0].strip()
    times = int(parts[1])

    if times > 50:
        await message.edit("❌ **Max 50 times allowed hai!**")
        return

    await message.delete()
    for _ in range(times):
        await client.send_message(message.chat.id, text)
        await asyncio.sleep(0.5)
