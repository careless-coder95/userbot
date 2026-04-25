import asyncio
from pyrogram import Client, filters
from pyrogram.types import ChatPermissions
from pyrogram.errors import ChatAdminRequired, UserAdminInvalid, FloodWait
from helpers import build_output, stylish
from config import DIVIDER, OWNER_TAG

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   HELPER — get target user from reply or arg
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

async def get_target(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        return message.reply_to_message.from_user
    args = message.text.split(None, 1)
    if len(args) > 1:
        try:
            return await client.get_users(args[1].strip())
        except Exception:
            return None
    return None

def admin_check(func):
    async def wrapper(client, message):
        try:
            await func(client, message)
        except ChatAdminRequired:
            await message.edit("❌ **ᴍᴜᴊʜᴇ ᴀᴅᴍɪɴ ʙᴀɴᴀᴏ ᴘᴀʜʟᴇ!**")
        except UserAdminInvalid:
            await message.edit("❌ **ᴜꜱ ᴜꜱᴇʀ ᴘᴇ ʏᴇ ɴᴀʜɪ ᴋᴀʀ ꜱᴀᴋᴛᴇ!**")
        except Exception as e:
            await message.edit(f"❌ **Error:** `{e}`")
    return wrapper


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   .ᴋɪᴄᴋ — Kick a user
#   Usage: reply + .kick  OR  .kick @user
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@Client.on_message(filters.me & filters.command("kick", prefixes="."))
@admin_check
async def kick_command(client, message):
    user = await get_target(client, message)
    if not user:
        await message.edit("**ᴜꜱᴀɢᴇ:** ʀᴇᴘʟʏ ᴋᴀʀᴋᴇ `.kick` ʏᴀ `.kick @user`")
        return
    await client.ban_chat_member(message.chat.id, user.id)
    await client.unban_chat_member(message.chat.id, user.id)
    result = (
        f"• {stylish('USER')}   : [{user.first_name}](tg://user?id={user.id})\n"
        f"• {stylish('ID')}     : `{user.id}`\n"
        f"• {stylish('ACTION')} : Kicked ✅"
    )
    await message.edit(build_output("❁═════⟬ ᴋɪᴄᴋᴇᴅ ⟭═════❁", result), disable_web_page_preview=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   .ʙᴀɴ — Ban a user
#   Usage: reply + .ban  OR  .ban @user
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@Client.on_message(filters.me & filters.command("ban", prefixes="."))
@admin_check
async def ban_command(client, message):
    user = await get_target(client, message)
    if not user:
        await message.edit("**ᴜꜱᴀɢᴇ:** ʀᴇᴘʟʏ ᴋᴀʀᴋᴇ `.ban` ʏᴀ `.ban @user`")
        return
    await client.ban_chat_member(message.chat.id, user.id)
    result = (
        f"• {stylish('USER')}   : [{user.first_name}](tg://user?id={user.id})\n"
        f"• {stylish('ID')}     : `{user.id}`\n"
        f"• {stylish('ACTION')} : Banned 🔨"
    )
    await message.edit(build_output("❁═════⟬ ʙᴀɴɴᴇᴅ ⟭═════❁", result), disable_web_page_preview=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   .ᴜɴʙᴀɴ — Unban a user
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@Client.on_message(filters.me & filters.command("unban", prefixes="."))
@admin_check
async def unban_command(client, message):
    user = await get_target(client, message)
    if not user:
        await message.edit("**ᴜꜱᴀɢᴇ:** `.unban @user`")
        return
    await client.unban_chat_member(message.chat.id, user.id)
    result = (
        f"• {stylish('USER')}   : [{user.first_name}](tg://user?id={user.id})\n"
        f"• {stylish('ACTION')} : Unbanned ✅"
    )
    await message.edit(build_output("❁═════⟬ ᴜɴʙᴀɴɴᴇᴅ ⟭═════❁", result), disable_web_page_preview=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   .ᴍᴜᴛᴇ — Mute a user
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@Client.on_message(filters.me & filters.command("mute", prefixes="."))
@admin_check
async def mute_command(client, message):
    user = await get_target(client, message)
    if not user:
        await message.edit("**ᴜꜱᴀɢᴇ:** ʀᴇᴘʟʏ ᴋᴀʀᴋᴇ `.mute`")
        return
    await client.restrict_chat_member(
        message.chat.id, user.id,
        ChatPermissions(can_send_messages=False)
    )
    result = (
        f"• {stylish('USER')}   : [{user.first_name}](tg://user?id={user.id})\n"
        f"• {stylish('ACTION')} : Muted 🔇"
    )
    await message.edit(build_output("❁═════⟬ ᴍᴜᴛᴇᴅ ⟭═════❁", result), disable_web_page_preview=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   .ᴜɴᴍᴜᴛᴇ — Unmute a user
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@Client.on_message(filters.me & filters.command("unmute", prefixes="."))
@admin_check
async def unmute_command(client, message):
    user = await get_target(client, message)
    if not user:
        await message.edit("**ᴜꜱᴀɢᴇ:** ʀᴇᴘʟʏ ᴋᴀʀᴋᴇ `.unmute`")
        return
    await client.restrict_chat_member(
        message.chat.id, user.id,
        ChatPermissions(
            can_send_messages=True,
            can_send_media_messages=True,
            can_send_other_messages=True,
            can_add_web_page_previews=True
        )
    )
    result = (
        f"• {stylish('USER')}   : [{user.first_name}](tg://user?id={user.id})\n"
        f"• {stylish('ACTION')} : Unmuted 🔊"
    )
    await message.edit(build_output("❁═════⟬ ᴜɴᴍᴜᴛᴇᴅ ⟭═════❁", result), disable_web_page_preview=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   .ᴘɪɴ — Pin a message
#   Usage: reply + .pin
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@Client.on_message(filters.me & filters.command("pin", prefixes="."))
@admin_check
async def pin_command(client, message):
    if not message.reply_to_message:
        await message.edit("**ᴜꜱᴀɢᴇ:** ᴋɪꜱɪ ᴍᴇꜱꜱᴀɢᴇ ᴋᴏ ʀᴇᴘʟʏ ᴋᴀʀᴋᴇ `.pin`")
        return
    await client.pin_chat_message(message.chat.id, message.reply_to_message.id)
    await message.edit(
        f"❁═════⟬ ᴘɪɴɴᴇᴅ ⟭═════❁\n\n"
        f"• {stylish('MESSAGE')} : Pinned ✅\n\n"
        f"{OWNER_TAG}"
    )


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   .ᴘᴜʀɢᴇ — Delete messages from reply to now
#   Usage: reply + .purge
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@Client.on_message(filters.me & filters.command("purge", prefixes="."))
async def purge_command(client, message):
    if not message.reply_to_message:
        await message.edit("**ᴜꜱᴀɢᴇ:** ᴊᴀʜᴀɴ ꜱᴇ ᴅᴇʟᴇᴛᴇ ᴋᴀʀɴᴀ ʜᴏ ᴜꜱ ᴍᴇꜱꜱᴀɢᴇ ᴋᴏ ʀᴇᴘʟʏ ᴋᴀʀᴋᴇ `.purge`")
        return

    start_id = message.reply_to_message.id
    end_id   = message.id
    ids      = list(range(start_id, end_id + 1))
    count    = 0

    # Delete in chunks of 100
    for i in range(0, len(ids), 100):
        chunk = ids[i:i+100]
        deleted = await client.delete_messages(message.chat.id, chunk)
        count += deleted
        await asyncio.sleep(0.3)

    confirm = await client.send_message(
        message.chat.id,
        f"❁═════⟬ ᴘᴜʀɢᴇᴅ ⟭═════❁\n\n"
        f"• {stylish('DELETED')} : `{count}` messages 🗑️\n\n"
        f"{OWNER_TAG}"
    )
    await asyncio.sleep(3)
    await confirm.delete()


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   .ᴘʀᴏᴍᴏᴛᴇ — Promote user to admin
#   Usage: reply + .promote
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@Client.on_message(filters.me & filters.command("promote", prefixes="."))
@admin_check
async def promote_command(client, message):
    user = await get_target(client, message)
    if not user:
        await message.edit("**ᴜꜱᴀɢᴇ:** ʀᴇᴘʟʏ ᴋᴀʀᴋᴇ `.promote`")
        return
    await client.promote_chat_member(
        message.chat.id, user.id,
        can_manage_chat=True,
        can_delete_messages=True,
        can_restrict_members=True,
        can_invite_users=True,
        can_pin_messages=True
    )
    result = (
        f"• {stylish('USER')}   : [{user.first_name}](tg://user?id={user.id})\n"
        f"• {stylish('ACTION')} : Promoted to Admin ⭐"
    )
    await message.edit(build_output("❁═════⟬ ᴘʀᴏᴍᴏᴛᴇᴅ ⟭═════❁", result), disable_web_page_preview=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   .ᴅᴇᴍᴏᴛᴇ — Remove admin rights
#   Usage: reply + .demote
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@Client.on_message(filters.me & filters.command("demote", prefixes="."))
@admin_check
async def demote_command(client, message):
    user = await get_target(client, message)
    if not user:
        await message.edit("**ᴜꜱᴀɢᴇ:** ʀᴇᴘʟʏ ᴋᴀʀᴋᴇ `.demote`")
        return
    await client.promote_chat_member(
        message.chat.id, user.id,
        can_manage_chat=False,
        can_delete_messages=False,
        can_restrict_members=False,
        can_invite_users=False,
        can_pin_messages=False
    )
    result = (
        f"• {stylish('USER')}   : [{user.first_name}](tg://user?id={user.id})\n"
        f"• {stylish('ACTION')} : Demoted 🔻"
    )
    await message.edit(build_output("❁═════⟬ ᴅᴇᴍᴏᴛᴇᴅ ⟭═════❁", result), disable_web_page_preview=True)
