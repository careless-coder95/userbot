import asyncio
import random
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from config import OWNER_TAG, DIVIDER

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

async def get_members(client, chat_id):
    members = []
    async for m in client.get_chat_members(chat_id):
        if not m.user.is_bot and not m.user.is_deleted:
            members.append(m.user)
    return members

async def send_tags(client, chat_id, members):
    chunk = []
    for user in members:
        mention = f"[{user.first_name}](tg://user?id={user.id})"
        chunk.append(mention)
        if len(chunk) == 5:
            await client.send_message(chat_id, " ".join(chunk), disable_web_page_preview=True)
            chunk = []
            await asyncio.sleep(1)
    if chunk:
        await client.send_message(chat_id, " ".join(chunk), disable_web_page_preview=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   .tagall
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TAG_TEXTS = [
    "⚡ Oye uth ja bhai 😴",
    "🔥 Aaj kuch bada karna hai kya?",
    "😎 Online ho ya so rahe ho?",
    "💀 Reply nahi kiya to fine lagega",
    "🚀 Chal attendance laga de",
    "👀 Dekh raha hu sabko...",
    "😂 Ghost mat ban bhai"
]

@Client.on_message(filters.me & filters.command("tagall", prefixes="."))
async def tagall_command(client, message):
    args = message.text.split(None, 1)
    custom_text = args[1].strip() if len(args) > 1 else None

    await message.delete()

    members = await get_members(client, message.chat.id)
    
    # 👉 random order
    random.shuffle(members)

    header = (
        f"❁═════⟬ 𝐓𝐀𝐆 𝐀𝐋𝐋 ⟭═════❁\n\n"
        f"{OWNER_TAG}"
    )

    await client.send_message(message.chat.id, header)
    await asyncio.sleep(1)

    for user in members:
        mention = f"[{user.first_name}](tg://user?id={user.id})"

        # 👉 agar custom text hai to wahi use hoga
        if custom_text:
            text = custom_text
        else:
            text = random.choice(TAG_TEXTS)

        try:
            await client.send_message(
                message.chat.id,
                f"{mention} {text}",
                disable_web_page_preview=True
            )
            await asyncio.sleep(1)

        except FloodWait as e:
            await asyncio.sleep(e.value)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   .gmtag
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

GM_WISHES = [
    "🌅 ***𝐆𝐨𝐨𝐝 𝐌𝐨𝐫𝐧𝐢𝐧𝐠!*** _ᴀᴀᴊ ᴋᴀ ᴅɪɴ ᴛᴜᴍʜᴀʀᴀ ꜱᴀʙꜱᴇ ᴀᴄʜᴀ ʜᴏ_ ☀️",
    "🌞 ***𝐒𝐮𝐩𝐫𝐚𝐛𝐡𝐚𝐚𝐭!*** _ᴜᴛʜᴏ ᴊᴀɢᴏ ᴀᴜʀ ᴅᴜɴɪʏᴀ ᴊɪᴛᴏ_ 💪",
    "☕ ***𝐆𝐨𝐨𝐝 𝐌𝐨𝐫𝐧𝐢𝐧𝐠!*** _ᴄʜᴀʏ ᴘɪʏᴏ ᴀᴜʀ ᴍᴜꜱᴋᴜʀᴀᴏ_ 😊",
    "🌸 ***𝐍𝐚𝐲𝐚 𝐃𝐢𝐧 𝐍𝐚𝐲𝐢 𝐔𝐦𝐦𝐞𝐞𝐝!*** _ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ʙʜᴀɪ_ 🙌",
    "🔥 ***𝐆𝐨𝐨𝐝 𝐌𝐨𝐫𝐧𝐢𝐧𝐠!*** _ᴀᴀᴊ ᴋᴜᴄʜ ɴᴀʏᴀ ᴋᴀʀᴏ, ᴋᴜᴄʜ ᴀʟᴀɢ ᴋᴀʀᴏ_ 💡",
    "🌻 ***𝐒𝐮𝐛𝐡 𝐊𝐚 𝐍𝐚𝐦𝐚𝐬𝐭𝐞!*** _ʙᴀᴅɪ ᴄʜɪᴢᴇɴ ꜱᴏᴄʜᴏ, ʙᴀᴅᴀ ᴋᴀʀᴏ_ 🚀",
    "🌄 ***𝐔𝐭𝐡𝐨 𝐁𝐡𝐚𝐢!*** _ᴅɪɴ ꜱʜᴜʀᴜ ʜᴏ ɢᴀʏᴀ, ᴀʙ ᴅᴜɴɪʏᴀ ᴊɪᴛɴᴇ ᴋᴀ ᴠᴀᴋᴛ ʜᴀɪ_ 🌟",
]

@Client.on_message(filters.me & filters.command("gmtag", prefixes="."))
async def gmtag_command(client, message):
    await message.delete()
    members = await get_members(client, message.chat.id)
    header = (
        f"🌅 ***𝐆𝐨𝐨𝐝 𝐌𝐨𝐫𝐧𝐢𝐧𝐠 𝐒𝐚𝐛𝐤𝐨!*** 🌸\n\n"
        f"☀️ _ᴜᴛʜᴏ ᴊᴀɢᴏ, ᴅɪɴ ꜱʜᴜʀᴜ ʜᴏ ɢᴀʏᴀ!_\n\n"
        f"{OWNER_TAG}"
    )
    await client.send_message(message.chat.id, header)
    await asyncio.sleep(1)
    for user in members:
        wish    = random.choice(GM_WISHES)
        mention = f"[{user.first_name}](tg://user?id={user.id})"
        try:
            await client.send_message(message.chat.id, f"{mention}\n{wish}", disable_web_page_preview=True)
            await asyncio.sleep(1)
        except FloodWait as e:
            await asyncio.sleep(e.value)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   .gntag
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

GN_WISHES = [
    "🌙 ***𝐆𝐨𝐨𝐝 𝐍𝐢𝐠𝐡𝐭!*** _ᴍɪᴛʜᴇ ꜱᴜɴᴀʜʀᴇ ꜱᴀᴘɴᴇ ᴀᴀʏᴇɴ_ 💤",
    "⭐ ***𝐒𝐨 𝐉𝐚𝐚𝐨 𝐁𝐡𝐚𝐢!*** _ᴋᴀʟ ꜰɪʀ ʟᴀᴅᴇɴɢᴇ_ 😴",
    "🌛 ***𝐀𝐚𝐫𝐚𝐚𝐦 𝐊𝐚𝐫𝐨!*** _ᴅɪɴ ʙʜᴀʀ ᴋᴀꜰɪ ᴋᴀᴍ ᴋɪʏᴀ_ 🙏",
    "🌌 ***𝐆𝐨𝐨𝐝 𝐍𝐢𝐠𝐡𝐭!*** _ᴛᴀᴀʀᴏɴ ᴋɪ ʀᴏꜱʜɴɪ ᴍᴇɪɴ ꜱᴏ ᴊᴀᴀᴏ_ ✨",
    "🛌 ***𝐑𝐚𝐭 𝐊𝐢 𝐍𝐚𝐦𝐚𝐬𝐭𝐞!*** _ᴋᴀʟ ɴᴀʏᴀ ᴅɪɴ ʟᴀʏᴇɢᴀ ɴᴀʏɪ ᴜᴍᴍᴇᴇᴅ_ 💫",
    "🌠 ***𝐆𝐨𝐨𝐝 𝐍𝐢𝐠𝐡𝐭!*** _ꜱᴏɴᴇ ꜱᴇ ᴘᴀʜʟᴇ ᴇᴋ ʙᴀᴀʀ ᴍᴜꜱᴋᴜʀᴀᴏ_ 😊",
    "🌃 ***𝐑𝐚𝐚𝐭 𝐊𝐨 𝐀𝐚𝐫𝐚𝐚𝐦 𝐊𝐚𝐫𝐨!*** _ᴋᴀʟ ᴅᴏʙᴀʀᴀ ᴅᴜɴɪʏᴀ ꜰᴀᴛᴇʜ ᴋᴀʀᴇɴɢᴇ_ 🔥",
]

@Client.on_message(filters.me & filters.command("gntag", prefixes="."))
async def gntag_command(client, message):
    await message.delete()
    members = await get_members(client, message.chat.id)
    header = (
        f"🌙 ***𝐆𝐨𝐨𝐝 𝐍𝐢𝐠𝐡𝐭 𝐒𝐚𝐛𝐤𝐨!*** ⭐\n\n"
        f"🛌 _ᴀᴀʀᴀᴀᴍ ᴋᴀʀᴏ, ᴋᴀʟ ꜰɪʀ ᴍɪʟᴇɴɢᴇ!_\n\n"
        f"{OWNER_TAG}"
    )
    await client.send_message(message.chat.id, header)
    await asyncio.sleep(1)
    for user in members:
        wish    = random.choice(GN_WISHES)
        mention = f"[{user.first_name}](tg://user?id={user.id})"
        try:
            await client.send_message(message.chat.id, f"{mention}\n{wish}", disable_web_page_preview=True)
            await asyncio.sleep(1)
        except FloodWait as e:
            await asyncio.sleep(e.value)
