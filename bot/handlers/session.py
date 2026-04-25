from telegram import Update
from telegram.ext import ContextTypes
from bot.database import save_session, is_approved, is_banned
from bot.userbot_manager import start_userbot


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   Message handler — waits for session string
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

async def session_receiver(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    if is_banned(user.id):
        return

    if not context.user_data.get("waiting_session"):
        return

    if not is_approved(user.id):
        await update.message.reply_text(
            "❌ *Tumhe access nahi hai.*",
            parse_mode="Markdown"
        )
        return

    session_string = update.message.text.strip()

    # Basic validation
    if len(session_string) < 50:
        await update.message.reply_text(
            "❌ *Yeh valid session nahi lagta!*\n\n_Sahi string paste karo._",
            parse_mode="Markdown"
        )
        return

    await update.message.reply_text("⏳ *Session verify ho raha hai...*", parse_mode="Markdown")

    # Try to start userbot with this session
    success, error = await start_userbot(user.id, session_string)

    if success:
        save_session(user.id, session_string)
        context.user_data["waiting_session"] = False
        await update.message.reply_text(
            "❁═════⟬ ✅ ꜱᴜᴄᴄᴇꜱꜱ ⟭═════❁\n\n"
            "```\n"
            "• STATUS  : Userbot Started\n"
            "• SESSION : Saved\n"
            "• MODE    : Active\n"
            "```\n"
            "_Tumhara userbot ab chal raha hai!_\n\n"
            "❁═══⟬ 𝑶𝒘𝒏𝒆𝒓: ᴍɪsᴛᴇʀ sᴛᴀʀᴋ ⟭═══❁",
            parse_mode="Markdown"
        )
    else:
        await update.message.reply_text(
            f"❁═════⟬ ❌ ꜰᴀɪʟᴇᴅ ⟭═════❁\n\n"
            f"```\n"
            f"• STATUS : Session Invalid\n"
            f"• ERROR  : {error}\n"
            f"```\n"
            f"_Sahi session generate karke dobara try karo._\n\n"
            f"❁═══⟬ 𝑶𝒘𝒏𝒆𝒓: ᴍɪsᴛᴇʀ sᴛᴀʀᴋ ⟭═══❁",
            parse_mode="Markdown"
        )
