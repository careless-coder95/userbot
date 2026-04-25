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
    " **𝐎𝐲𝐞 𝐁𝐫𝐨 𝐊𝐚𝐡𝐚 𝐆𝐚𝐲𝐚 𝐓𝐮😏** ",
    " **𝐒𝐚𝐛 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐚𝐨 𝐁𝐚𝐭 𝐊𝐚𝐫𝐭𝐞 𝐇𝐚𝐢𝐧😎** ",
    " **𝐀𝐛𝐞 𝐆𝐫𝐨𝐮𝐩 𝐌𝐞 𝐊𝐮𝐜𝐡 𝐓𝐨 𝐁𝐨𝐥 𝐃𝐞😤** ",
    " **𝐎𝐲𝐞 𝐂𝐡𝐮𝐩 𝐊𝐲𝐮 𝐁𝐚𝐢𝐭𝐡𝐚 𝐇𝐚𝐢 𝐁𝐫𝐨🤨** ",
    " **𝐊𝐲𝐚 𝐇𝐚𝐥 𝐂𝐡𝐚𝐥 𝐇𝐚𝐢 𝐌𝐞𝐫𝐞 𝐁𝐡𝐚𝐢😎** ",
    " **𝐒𝐚𝐛 𝐋𝐨𝐠 𝐀𝐜𝐭𝐢𝐯𝐞 𝐇𝐨 𝐉𝐚𝐨 𝐉𝐥𝐝𝐢🔥** ",
    " **𝐆𝐫𝐨𝐮𝐩 𝐌𝐞 𝐂𝐡𝐚𝐭 𝐊𝐲𝐮 𝐍𝐡𝐢 𝐂𝐡𝐚𝐥 𝐑𝐡𝐢🤔** ",
    " **𝐎𝐲𝐞 𝐆𝐚𝐦𝐞 𝐊𝐡𝐞𝐥𝐧𝐞 𝐂𝐡𝐚𝐥𝐨 𝐊𝐨𝐧 𝐊𝐨𝐧 𝐇𝐚𝐢🎮** ",
    " **𝐀𝐛𝐞 𝐊𝐨𝐢 𝐌𝐞𝐦𝐞 𝐓𝐨 𝐃𝐚𝐥𝐨 𝐘𝐚𝐫😂** ",
    " **𝐒𝐚𝐛 𝐒𝐨 𝐆𝐚𝐲𝐞 𝐊𝐲𝐚 𝐘𝐚𝐫😴** ",
    " **𝐁𝐫𝐨 𝐀𝐚𝐣 𝐊𝐲𝐚 𝐏𝐥𝐚𝐧 𝐇𝐚𝐢🤟** ",
    " **𝐎𝐲𝐞 𝐊𝐨𝐢 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐚𝐨 𝐍𝐚 𝐘𝐚𝐫😩** ",
    " **𝐆𝐫𝐨𝐮𝐩 𝐊𝐨 𝐀𝐜𝐭𝐢𝐯𝐞 𝐊𝐚𝐫𝐨 𝐁𝐡𝐚𝐢🔥** ",
    " **𝐀𝐛𝐞 𝐒𝐢𝐫𝐟 𝐑𝐞𝐚𝐝 𝐊𝐚𝐫𝐧𝐞 𝐒𝐞 𝐊𝐮𝐜𝐡 𝐍𝐡𝐢 𝐇𝐨𝐠𝐚😏** ",
    " **𝐎𝐲𝐞 𝐁𝐚𝐭𝐚𝐨 𝐊𝐚𝐮𝐧 𝐊𝐚𝐮𝐧 𝐅𝐫𝐞𝐞 𝐇𝐚𝐢 𝐀𝐛𝐡𝐢😎** ",
    " **𝐁𝐡𝐚𝐢 𝐋𝐨𝐠 𝐊𝐢𝐝𝐡𝐚𝐫 𝐆𝐚𝐲𝐚 𝐒𝐚𝐫𝐚 𝐆𝐫𝐨𝐮𝐩🤨** ",
    " **𝐎𝐲𝐞 𝐌𝐚𝐬𝐭𝐢 𝐒𝐭𝐚𝐫𝐭 𝐊𝐚𝐫𝐨 𝐘𝐚𝐫🥳** ",
    " **𝐊𝐮𝐜𝐡 𝐁𝐨𝐥𝐨 𝐍𝐚 𝐁𝐡𝐚𝐢 𝐂𝐡𝐮𝐩 𝐊𝐲𝐮 𝐇𝐨🥲** ",
    " **𝐀𝐛𝐞 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐚𝐤𝐞 𝐁𝐡𝐢 𝐆𝐡𝐨𝐬𝐭 𝐌𝐨𝐝𝐞 𝐌𝐞 𝐇𝐨😑** ",
    " **𝐎𝐲𝐞 𝐁𝐫𝐨 𝐑𝐞𝐩𝐥𝐲 𝐓𝐨 𝐃𝐞 𝐃𝐞𝐤𝐡 𝐑𝐡𝐚 𝐇𝐮 𝐌𝐞👀** "
    " **𝐁𝐫𝐨 𝐘𝐞 𝐆𝐫𝐨𝐮𝐩 𝐇𝐚𝐢 𝐘𝐚 𝐆𝐫𝐚𝐯𝐞𝐲𝐚𝐫𝐝💀** ",
    " **𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐚𝐤𝐞 𝐁𝐡𝐢 𝐍𝐨 𝐑𝐞𝐩𝐥𝐲 𝐖𝐚𝐥𝐞 𝐋𝐞𝐠𝐞𝐧𝐝𝐬😂** ",
    " **𝐎𝐲𝐞 𝐁𝐫𝐨 𝐀𝐭𝐭𝐞𝐧𝐭𝐢𝐨𝐧 𝐂𝐡𝐚𝐡𝐢𝐲𝐞 𝐓𝐨 𝐁𝐨𝐥 𝐍𝐚 𝐂𝐥𝐞𝐚𝐫😏** ",
    " **𝐊𝐮𝐜𝐡 𝐓𝐨 𝐌𝐚𝐭𝐭𝐞𝐫 𝐃𝐚𝐥𝐨 𝐘𝐚𝐫 𝐒𝐢𝐫𝐟 𝐒𝐢𝐥𝐞𝐧𝐭 𝐍𝐚 𝐑𝐡𝐨😑** ",
    " **𝐁𝐫𝐨 𝐋𝐨𝐠 𝐆𝐫𝐨𝐮𝐩 𝐌𝐞 𝐀𝐚𝐤𝐞 𝐁𝐡𝐢 𝐒𝐨𝐥𝐨 𝐊𝐡𝐞𝐥 𝐑𝐡𝐞 𝐇𝐨😂** ",
    " **𝐎𝐲𝐞 𝐆𝐫𝐨𝐮𝐩 𝐊𝐨 𝐃𝐞𝐚𝐝 𝐌𝐚𝐭 𝐁𝐧𝐚𝐨 𝐓𝐡𝐨𝐝𝐚 𝐉𝐢𝐧𝐝𝐚 𝐑𝐚𝐤𝐡𝐨🔥** ",
    " **𝐀𝐛𝐞 𝐊𝐨𝐢 𝐓𝐨 𝐁𝐚𝐭 𝐊𝐚𝐫𝐨 𝐘𝐚 𝐌𝐞 𝐇𝐢 𝐒𝐭𝐚𝐫𝐭 𝐊𝐚𝐫𝐮😏** "
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
    " **➠ ᴏʏᴇ ᴋʜᴜᴍʙʜᴋᴀʀᴀɴ ᴋɪ ᴀᴜʟᴀᴅ, ᴜᴛʜ ᴊᴀ ᴅɪɴ ᴀᴀ ɢʏᴀ ☀️** ",
    " **➠ ᴏʏᴇ ɴɪᴋᴀᴍᴍᴇ, ᴀʙʜɪ ᴛᴋ sᴏ ʀʜᴀ ʜᴀɪ ᴋʏᴀ 😏** ",
    " **➠ ᴜᴛʜ ᴊᴀ ʙʀᴏ, sᴜʀᴀᴊ ᴛᴇʀᴇ sᴇ ᴘᴇʜʟᴇ ᴏɴʟɪɴᴇ ᴀᴀ ɢʏᴀ 🌤️** ",
    " **➠ ᴏʏᴇ ᴀʟᴀʀᴍ ᴋᴏ ᴛᴀʟᴀᴋ ᴅᴇ ᴅɪʏᴀ ᴋʏᴀ ʀᴏᴢ 😑** ",
    " **➠ ᴋʜᴀɴᴀ ᴋʜᴀɴᴇ ᴍᴇ sᴀʙsᴇ ᴀᴀɢᴇ, ᴜᴛʜɴᴇ ᴍᴇ sᴀʙsᴇ ᴘɪᴄʜᴇ 😆** ",
    " **➠ ᴏʏᴇ ᴜᴛʜ ᴊᴀ, ᴠʀɴᴀ ᴍᴏʙɪʟᴇ ᴄʜᴀʀɢᴇʀ ʜɪ ᴋʜɪɴᴄʜ ʟᴜɴɢᴀ 🔌😏** ",
    " **➠ ʙʀᴏ ᴛᴇʀᴇ sᴏɴᴇ ᴋᴀ ᴛᴀʟᴇɴᴛ ᴏʟʏᴍᴘɪᴄ ʟᴇᴠᴇʟ ʜᴀɪ 🏆😴** ",
    " **➠ ᴏʏᴇ ʟᴀsᴛ ᴡᴀʀɴɪɴɢ — ᴜᴛʜ ᴊᴀ ɴᴀʜɪ ᴛᴏ ᴘᴀɴɪ ᴅᴀʟ ᴅᴜɴɢᴀ 🧊😂** ",
    " **➠ ᴜᴛʜ ᴊᴀ ʙʜᴀɪ, ɢʀᴏᴜᴘ ᴍᴇ ᴛᴇʀᴇ ʙɪɴᴀ ᴍᴀᴊᴀ ɴʜɪ ᴀᴀ ʀʜᴀ 😏** ",
    " **➠ ᴏʏᴇ ɴɪɴᴅ ᴋᴇ ʙʀᴀɴᴅ ᴀᴍʙᴀssᴀᴅᴏʀ, ᴜᴛʜ ᴊᴀ 😂** ",
    " **➠ ᴜᴛʜ ᴊᴀ ʙʀᴏ, ᴅɪɴ ᴋᴀ ʜᴀʟғ ᴘᴀss ʜᴏ ɢʏᴀ 😑** ",
    " **➠ ᴏʏᴇ sʟᴇᴇᴘɪɴɢ ᴋɪɴɢ, ᴋᴀʙ ᴛᴀᴋ sɪɴɢʜᴀsᴀɴ ᴘᴇ sᴏᴛᴀ ʀʜᴇɢᴀ 👑😴** ",
    " **➠ ʙʀᴏ ᴛᴜ ᴜᴛʜᴛᴀ ɴʜɪ, ᴅᴜɴɪʏᴀ ᴀᴀɢᴇ ʙᴀᴅʜ ʀʜɪ ʜᴀɪ 😏** ",
    " **➠ ᴏʏᴇ ᴜᴛʜ ᴊᴀ, ɴᴀʜɪ ᴛᴏ ᴛᴇʀᴀ ʙʀᴇᴀᴋғᴀsᴛ ᴍᴇ ʜɪ ᴋʜᴀ ʟᴜɴɢᴀ 🍳😂** ",
    " **➠ ᴋʜᴜᴍʙʜᴋᴀʀᴀɴ ʀᴇʟᴏᴀᴅᴇᴅ — ᴀʙ ᴛᴏ ᴜᴛʜ ᴊᴀ 😆** ",
    " **➠ ᴏʏᴇ ʙʀᴏ, ᴀʟᴀʀᴍ ᴛᴜᴊʜsᴇ ᴅᴀʀᴛᴀ ʜᴀɪ ɪsʟɪᴇ ᴄʜᴜᴘ ʀᴇʜᴛᴀ ʜᴀɪ 😏** ",
    " **➠ ᴜᴛʜ ᴊᴀ ʙʜᴀɪ, ᴍᴏʙɪʟᴇ ʙʜɪ ᴛʜᴀᴋ ɢʏᴀ ᴛᴇʀᴇ sᴀᴛʜ sᴏᴛᴇ sᴏᴛᴇ 😂** ",
    " **➠ ᴏʏᴇ ᴅʀᴇᴀᴍ ᴍᴏᴅᴇ sᴇ ᴏᴜᴛ ᴀᴀ ʀᴇᴀʟ ʟɪғᴇ ᴍᴇ 😑** ",
    " **➠ ᴜᴛʜ ᴊᴀ ʙʀᴏ, ᴄʜᴀɪ ᴛᴇʀᴀ ɪɴᴛᴇᴢᴀʀ ᴋᴀʀ ʀʜɪ ☕😏** ",
    " **➠ ᴏʏᴇ ɴɪɴᴅ ᴋᴇ ʙᴀᴀᴅsʜᴀʜ, ᴀʙ ʀᴀᴀᴊ ᴄʜʜᴏᴅ ᴋᴀᴍ ᴘᴇ ʟᴀɢ 👑🔥** "
]

@Client.on_message(filters.me & filters.command("gmtag", prefixes="."))
async def gmtag_command(client, message):
    await message.delete()
    members = await get_members(client, message.chat.id)
    header = (
        f"🌅 **𝐆𝐨𝐨𝐝 𝐌𝐨𝐫𝐧𝐢𝐧𝐠 𝐒𝐚𝐛𝐤𝐨!** 🌸\n\n"
        f"☀️ _ᴜᴛʜᴏ ᴊᴀɢᴏ, ᴅɪɴ ꜱʜᴜʀᴜ ʜᴏ ɢᴀʏᴀ!_"
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

GN_WISHES = [ " **➠ ɢᴏᴏᴅ ɴɪɢʜᴛ 🌚** ",
           " **➠ ᴄʜᴜᴘ ᴄʜᴀᴘ sᴏ ᴊᴀ 🙊** ",
           " **➠ ʙᴀʙᴜ sᴏɴᴀ cʜᴀᴍᴍᴀcʜ ʙʜᴀɢᴏɴᴀ ʙᴀᴀᴅ ᴍᴇ ᴋᴀʀ ʟᴇɴᴀ. ᴀʙʜɪ sᴏᴊᴀ 🙄** ",
           " **➠ ᴘʜᴏɴᴇ ʀᴀᴋʜ ᴋᴀʀ sᴏ ᴊᴀ, ɴᴀʜɪ ᴛᴏ ʙʜᴏᴏᴛ ᴀᴀ ᴊᴀʏᴇɢᴀ..👻** ",
           " **➠ ᴀᴡᴇᴇ ʙᴀʙᴜ sᴏɴᴀ ᴅɪɴ ᴍᴇɪɴ ᴋᴀʀ ʟᴇɴᴀ ᴀʙʜɪ sᴏ ᴊᴀᴏ..?? 🥲** ",
           " **➠ ᴍᴜᴍᴍʏ ᴅᴇᴋʜᴏ ʏᴇ ᴀᴘɴᴇ ɢғ sᴇ ʙᴀᴀᴛ ᴋʀ ʀʜᴀ ʜ ʀᴀᴊᴀɪ ᴍᴇ ɢʜᴜs ᴋᴀʀ, sᴏ ɴᴀʜɪ ʀᴀʜᴀ 😜** ",
           " **➠ ᴘᴀᴘᴀ ʏᴇ ᴅᴇᴋʜᴏ ᴀᴘɴᴇ ʙᴇᴛᴇ ᴋᴏ ʀᴀᴀᴛ ʙʜᴀʀ ᴘʜᴏɴᴇ ᴄʜᴀʟᴀ ʀʜᴀ ʜᴀɪ 🤭** ",
           " **➠ ɢɴ sᴅ ᴛᴄ.. 🙂** ",
           " **➠ ɢᴏᴏᴅ ɴɪɢʜᴛ sᴡᴇᴇᴛ ᴅʀᴇᴀᴍ ᴛᴀᴋᴇ ᴄᴀʀᴇ..?? ✨** ",
           " **➠ ʀᴀᴀᴛ ʙʜᴜᴛ ʜᴏ ɢʏɪ ʜᴀɪ sᴏ ᴊᴀᴏ, ɢɴ..?? 🌌** ",
           " **➠ ᴍᴜᴍᴍʏ ᴅᴇᴋʜᴏ 11 ʙᴀᴊɴᴇ ᴡᴀʟᴇ ʜᴀɪ ʏᴇ ᴀʙʜɪ ᴛᴀᴋ ᴘʜᴏɴᴇ ᴄʜᴀʟᴀ ʀʜᴀ ɴᴀʜɪ sᴏ ɴᴀʜɪ ʀʜᴀ 🕦** ",
           " **➠ ᴋᴀʟ sᴜʙʜᴀ sᴄʜᴏᴏʟ ɴᴀʜɪ ᴊᴀɴᴀ ᴋʏᴀ, ᴊᴏ ᴀʙʜɪ ᴛᴀᴋ ᴊᴀɢ ʀʜᴇ ʜᴏ 🏫** ",
           " **➠ ʙᴀʙᴜ, ɢᴏᴏᴅ ɴɪɢʜᴛ sᴅ ᴛᴄ..?? 😊** ",
           " **➠ ɢᴏᴏᴅ ɴɪɢʜᴛ 🌷** ",
           " **➠ ᴍᴇ ᴊᴀ ʀᴀʜᴀ sᴏɴᴇ, ɢɴ sᴅ ᴛᴄ 🏵️** ",
           " **➠ ʜᴇʟʟᴏ ᴊɪ ɴᴀᴍᴀsᴛᴇ, ɢᴏᴏᴅ ɴɪɢʜᴛ 🍃** ",
           " **➠ ʜᴇʏ, ʟᴀᴅʟᴇ ᴋᴋʀʜ..? sᴏɴᴀ ɴᴀʜɪ ʜᴀɪ ᴋʏᴀ ☃️** ",
           " **➠ ɢᴏᴏᴅ ɴɪɢʜᴛ ᴊɪ, ʙʜᴜᴛ ʀᴀᴀᴛ ʜᴏ ɢʏɪ..? ⛄** ",
           " **➠ ᴍᴇ ᴊᴀ ʀᴀʜᴀ ʀᴏɴᴇ, ɪ ᴍᴇᴀɴ sᴏɴᴇ ɢᴏᴏᴅ ɴɪɢʜᴛ ᴊɪ 😁** ",
           " **➠ ᴍᴀᴄʜʜᴀʟɪ ᴋᴏ ᴋᴇʜᴛᴇ ʜᴀɪ ғɪsʜ, ɢᴏᴏᴅ ɴɪɢʜᴛ ᴅᴇᴀʀ ᴍᴀᴛ ᴋʀɴᴀ ᴍɪss, ᴊᴀ ʀʜ sᴏɴᴇ 🌄** ",
           " **➠ ɢᴏᴏᴅ ɴɪɢʜᴛ ʙʀɪɢʜᴛғᴜʟʟ ɴɪɢʜᴛ 🤭** ",
           " **➠ ᴛʜᴇ ɴɪɢʜᴛ ʜᴀs ғᴀʟʟᴇɴ, ᴛʜᴇ ᴅᴀʏ ɪs ᴅᴏɴᴇ,, ᴛʜᴇ ᴍᴏᴏɴ ʜᴀs ᴛᴀᴋᴇɴ ᴛʜᴇ ᴘʟᴀᴄᴇ ᴏғ ᴛʜᴇ sᴜɴ... 😊** ",
           " **➠ ᴍᴀʏ ᴀʟʟ ʏᴏᴜʀ ᴅʀᴇᴀᴍs ᴄᴏᴍᴇ ᴛʀᴜᴇ ❤️** ",
           " **➠ ɢᴏᴏᴅ ɴɪɢʜᴛ sᴘʀɪɴᴋʟᴇs sᴡᴇᴇᴛ ᴅʀᴇᴀᴍ 💚** ",
           " **➠ ɢᴏᴏᴅ ɴɪɢʜᴛ, ɴɪɴᴅ ᴀᴀ ʀʜɪ ʜᴀɪ 🥱** ",
           " **➠ ᴅᴇᴀʀ ғʀɪᴇɴᴅ ɢᴏᴏᴅ ɴɪɢʜᴛ 💤** ",
           " **➠ ɪᴛɴɪ ʀᴀᴀᴛ ᴍᴇ ᴊᴀɢ ᴋᴀʀ ᴋʏᴀ ᴋᴀʀ ʀʜᴇ ʜᴏ sᴏɴᴀ ɴᴀʜɪ ʜᴀɪ ᴋʏᴀ 😜** ",
           " **➠ ᴄʟᴏsᴇ ʏᴏᴜʀ ᴇʏᴇs sɴᴜɢɢʟᴇ ᴜᴘ ᴛɪɢʜᴛ,, ᴀɴᴅ ʀᴇᴍᴇᴍʙᴇʀ ᴛʜᴀᴛ ᴀɴɢᴇʟs, ᴡɪʟʟ ᴡᴀᴛᴄʜ ᴏᴠᴇʀ ʏᴏᴜ ᴛᴏɴɪɢʜᴛ... 💫** ",
         ]

@Client.on_message(filters.me & filters.command("gntag", prefixes="."))
async def gntag_command(client, message):
    await message.delete()
    members = await get_members(client, message.chat.id)
    header = (
        f"🌙 **𝐆𝐨𝐨𝐝 𝐍𝐢𝐠𝐡𝐭 𝐒𝐚𝐛𝐤𝐨!** ⭐\n\n"
        f"🛌 _ᴀᴀʀᴀᴀᴍ ᴋᴀʀᴏ, ᴋᴀʟ ꜰɪʀ ᴍɪʟᴇɴɢᴇ!_"
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
