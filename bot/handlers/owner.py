from telegram import Update
from telegram.ext import ContextTypes
from bot.config import OWNER_ID
from bot.database import (
    approve_user, unapprove_user, ban_user, unban_user,
    get_all_users, get_stats, get_user, add_user
)
from bot.userbot_manager import stop_userbot, get_active_count


def owner_only(func):
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE):
        if update.effective_user.id != OWNER_ID:
            await update.message.reply_text("❌ *Sirf owner use kar sakta hai!*", parse_mode="Markdown")
            return
        await func(update, context)
    return wrapper


def get_target_id(context, message_text):
    """Extract user_id from command args or replied message"""
    if context.args:
        try:
            return int(context.args[0])
        except ValueError:
            return None
    return None


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   /approve {userid}
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@owner_only
async def approve_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = get_target_id(context, update.message.text)
    if not user_id:
        await update.message.reply_text("**Usage:** `/approve {userid}`", parse_mode="Markdown")
        return

    add_user(user_id)
    approve_user(user_id)

    await update.message.reply_text(
        f"❁═════⟬ ✅ ᴀᴘᴘʀᴏᴠᴇᴅ ⟭═════❁\n\n"
        f"```\n"
        f"• USER ID : {user_id}\n"
        f"• STATUS  : Approved\n"
        f"• ACCESS  : Granted\n"
        f"```\n"
        f"❁═══⟬ 𝑶𝒘𝒏𝒆𝒓: ᴍɪsᴛᴇʀ sᴛᴀʀᴋ ⟭═══❁",
        parse_mode="Markdown"
    )

    # Notify user
    try:
        await context.bot.send_message(
            user_id,
            "❁═════⟬ ✅ ᴀᴄᴄᴇꜱꜱ ɢʀᴀɴᴛᴇᴅ ⟭═════❁\n\n"
            "```\n"
            "• STATUS : Approved!\n"
            "• ACTION : Add your session\n"
            "```\n"
            "_Ab /start karo aur session add karo._\n\n"
            "❁═══⟬ 𝑶𝒘𝒏𝒆𝒓: ᴍɪsᴛᴇʀ sᴛᴀʀᴋ ⟭═══❁",
            parse_mode="Markdown"
        )
    except Exception:
        pass


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   /unapprove {userid}
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@owner_only
async def unapprove_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = get_target_id(context, update.message.text)
    if not user_id:
        await update.message.reply_text("**Usage:** `/unapprove {userid}`", parse_mode="Markdown")
        return

    unapprove_user(user_id)
    await stop_userbot(user_id)

    await update.message.reply_text(
        f"❁═════⟬ ⛔ ᴜɴᴀᴘᴘʀᴏᴠᴇᴅ ⟭═════❁\n\n"
        f"```\n"
        f"• USER ID : {user_id}\n"
        f"• STATUS  : Unapproved\n"
        f"• USERBOT : Stopped\n"
        f"```\n"
        f"❁═══⟬ 𝑶𝒘𝒏𝒆𝒓: ᴍɪsᴛᴇʀ sᴛᴀʀᴋ ⟭═══❁",
        parse_mode="Markdown"
    )


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   /ban {userid}
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@owner_only
async def ban_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = get_target_id(context, update.message.text)
    if not user_id:
        await update.message.reply_text("**Usage:** `/ban {userid}`", parse_mode="Markdown")
        return

    ban_user(user_id)
    await stop_userbot(user_id)

    await update.message.reply_text(
        f"❁═════⟬ 🔨 ʙᴀɴɴᴇᴅ ⟭═════❁\n\n"
        f"```\n"
        f"• USER ID : {user_id}\n"
        f"• STATUS  : Banned\n"
        f"• USERBOT : Stopped\n"
        f"```\n"
        f"❁═══⟬ 𝑶𝒘𝒏𝒆𝒓: ᴍɪsᴛᴇʀ sᴛᴀʀᴋ ⟭═══❁",
        parse_mode="Markdown"
    )


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   /unban {userid}
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@owner_only
async def unban_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = get_target_id(context, update.message.text)
    if not user_id:
        await update.message.reply_text("**Usage:** `/unban {userid}`", parse_mode="Markdown")
        return

    unban_user(user_id)

    await update.message.reply_text(
        f"❁═════⟬ ✅ ᴜɴʙᴀɴɴᴇᴅ ⟭═════❁\n\n"
        f"```\n"
        f"• USER ID : {user_id}\n"
        f"• STATUS  : Unbanned\n"
        f"```\n"
        f"❁═══⟬ 𝑶𝒘𝒏𝒆𝒓: ᴍɪsᴛᴇʀ sᴛᴀʀᴋ ⟭═══❁",
        parse_mode="Markdown"
    )


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   /stats
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@owner_only
async def stats_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    total, approved, banned, with_session = get_stats()
    active = get_active_count()

    await update.message.reply_text(
        f"❁═════⟬ 📊 ꜱᴛᴀᴛꜱ ⟭═════❁\n\n"
        f"```\n"
        f"• TOTAL USERS    : {total}\n"
        f"• APPROVED       : {approved}\n"
        f"• BANNED         : {banned}\n"
        f"• WITH SESSION   : {with_session}\n"
        f"• ACTIVE BOTS    : {active}\n"
        f"```\n"
        f"❁═══⟬ 𝑶𝒘𝒏𝒆𝒓: ᴍɪsᴛᴇʀ sᴛᴀʀᴋ ⟭═══❁",
        parse_mode="Markdown"
    )


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   /users
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@owner_only
async def users_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    users = get_all_users()

    if not users:
        await update.message.reply_text("_Abhi koi user nahi hai._", parse_mode="Markdown")
        return

    lines = []
    for uid, uname, approved, banned, session, joined in users:
        status = "✅" if approved else "❌"
        ban_s  = " 🔨" if banned else ""
        sess   = " 💾" if session else ""
        uname_str = f"@{uname}" if uname else "N/A"
        lines.append(f"  {status}{ban_s}{sess} {uid} | {uname_str}")

    body = "\n".join(lines)
    await update.message.reply_text(
        f"❁═════⟬ 👥 ᴜꜱᴇʀꜱ ʟɪꜱᴛ ⟭═════❁\n\n"
        f"```\n"
        f"✅ Approved  ❌ Not  🔨 Banned  💾 Session\n"
        f"{'─'*35}\n"
        f"{body}\n"
        f"```\n"
        f"❁═══⟬ 𝑶𝒘𝒏𝒆𝒓: ᴍɪsᴛᴇʀ sᴛᴀʀᴋ ⟭═══❁",
        parse_mode="Markdown"
    )


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   /broadcast {text}
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@owner_only
async def broadcast_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("**Usage:** `/broadcast {message}`", parse_mode="Markdown")
        return

    text = " ".join(context.args)
    users = get_all_users()

    sent = 0
    failed = 0

    for uid, *_ in users:
        if uid == OWNER_ID:
            continue
        try:
            await context.bot.send_message(
                uid,
                f"📢 *Broadcast Message*\n\n{text}\n\n"
                f"❁═══⟬ 𝑶𝒘𝒏𝒆𝒓: ᴍɪsᴛᴇʀ sᴛᴀʀᴋ ⟭═══❁",
                parse_mode="Markdown"
            )
            sent += 1
        except Exception:
            failed += 1

    await update.message.reply_text(
        f"❁═════⟬ 📢 ʙʀᴏᴀᴅᴄᴀꜱᴛ ⟭═════❁\n\n"
        f"```\n"
        f"• SENT   : {sent}\n"
        f"• FAILED : {failed}\n"
        f"```\n"
        f"❁═══⟬ 𝑶𝒘𝒏𝒆𝒓: ᴍɪsᴛᴇʀ sᴛᴀʀᴋ ⟭═══❁",
        parse_mode="Markdown"
    )


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   /reload — Restart all active userbots
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@owner_only
async def reload_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    from bot.userbot_manager import restore_all_userbots, _active_bots, stop_userbot

    msg = await update.message.reply_text(
        "🔄 *Sabke userbots reload ho rahe hain...*",
        parse_mode="Markdown"
    )

    # Stop all active userbots first
    active_ids = list(_active_bots.keys())
    for uid in active_ids:
        await stop_userbot(uid)

    # Restore all with fresh plugins
    await restore_all_userbots()

    active = get_active_count()

    await msg.edit_text(
        f"❁═════⟬ 🔄 ʀᴇʟᴏᴀᴅᴇᴅ ⟭═════❁\n\n"
        f"```\n"
        f"• STATUS       : Done\n"
        f"• ACTIVE BOTS  : {active}\n"
        f"• PLUGINS      : Reloaded\n"
        f"```\n"
        f"_Sabke userbots nayi plugins ke saath chal rahe hain._\n\n"
        f"❁═══⟬ 𝑶𝒘𝒏𝒆𝒓: ᴍɪsᴛᴇʀ sᴛᴀʀᴋ ⟭═══❁",
        parse_mode="Markdown"
    )
