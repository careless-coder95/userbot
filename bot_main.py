import asyncio
from telegram.ext import (
    Application, CommandHandler,
    CallbackQueryHandler, MessageHandler, filters
)
from bot.config import BOT_TOKEN
from bot.database import init_db
from bot.handlers.start   import start_handler, callback_handler
from bot.handlers.session import session_receiver
from bot.handlers.owner   import (
    approve_handler, unapprove_handler,
    ban_handler, unban_handler,
    stats_handler, users_handler, broadcast_handler
)
from bot.userbot_manager import restore_all_userbots


async def post_init(application):
    print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("  ꜱᴛᴀʀᴋ ʙᴏᴛ ꜱᴛᴀʀᴛɪɴɢ...")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("\n🔄 Restoring saved userbots...\n")
    await restore_all_userbots()
    print("\n✅ Bot is ready!\n")


def main():
    init_db()

    app = (
        Application.builder()
        .token(BOT_TOKEN)
        .post_init(post_init)
        .build()
    )

    # ── Command Handlers ──────────────────────────
    app.add_handler(CommandHandler("start",      start_handler))
    app.add_handler(CommandHandler("approve",    approve_handler))
    app.add_handler(CommandHandler("unapprove",  unapprove_handler))
    app.add_handler(CommandHandler("ban",        ban_handler))
    app.add_handler(CommandHandler("unban",      unban_handler))
    app.add_handler(CommandHandler("stats",      stats_handler))
    app.add_handler(CommandHandler("users",      users_handler))
    app.add_handler(CommandHandler("broadcast",  broadcast_handler))

    # ── Callback (Inline Buttons) ─────────────────
    app.add_handler(CallbackQueryHandler(callback_handler))

    # ── Message Handler (Session input) ──────────
    app.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        session_receiver
    ))

    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
