import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from bot.config import (
    START_IMAGE, START_TEXT, OWNER_TEXT, HELP_TEXT,
    NOT_APPROVED_TEXT, SESSION_ASK_TEXT, OWNER_USER
)
from bot.database import add_user, is_approved, is_banned


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   Inline keyboard builder
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def main_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("👑 Owner",           callback_data="owner"),
            InlineKeyboardButton("📋 Help & Commands", callback_data="help"),
        ],
        [
            InlineKeyboardButton("➕ Add Your Session", callback_data="add_session"),
        ]
    ])

def back_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Back", callback_data="back")]
    ])


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   /start
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    add_user(user.id, user.username)

    if is_banned(user.id):
        await update.message.reply_text("❌ *Tumhe ban kar diya gaya hai.*", parse_mode="Markdown")
        return

    if os.path.exists(START_IMAGE):
        await update.message.reply_photo(
            photo=open(START_IMAGE, "rb"),
            caption=START_TEXT,
            parse_mode="Markdown",
            reply_markup=main_keyboard()
        )
    else:
        await update.message.reply_text(
            START_TEXT,
            parse_mode="Markdown",
            reply_markup=main_keyboard()
        )


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   Callback Query Handler
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user  = query.from_user
    data  = query.data
    await query.answer()

    if data == "owner":
        await query.edit_message_caption(
            caption=OWNER_TEXT.format(owner=OWNER_USER),
            parse_mode="Markdown",
            reply_markup=back_keyboard()
        ) if query.message.photo else await query.edit_message_text(
            text=OWNER_TEXT.format(owner=OWNER_USER),
            parse_mode="Markdown",
            reply_markup=back_keyboard()
        )

    elif data == "help":
        await query.edit_message_caption(
            caption=HELP_TEXT,
            parse_mode="Markdown",
            reply_markup=back_keyboard()
        ) if query.message.photo else await query.edit_message_text(
            text=HELP_TEXT,
            parse_mode="Markdown",
            reply_markup=back_keyboard()
        )

    elif data == "add_session":
        if is_banned(user.id):
            await query.answer("❌ Tumhe ban kar diya gaya hai.", show_alert=True)
            return

        if not is_approved(user.id):
            text = NOT_APPROVED_TEXT.format(owner=OWNER_USER)
            await query.edit_message_caption(
                caption=text,
                parse_mode="Markdown",
                reply_markup=back_keyboard()
            ) if query.message.photo else await query.edit_message_text(
                text=text,
                parse_mode="Markdown",
                reply_markup=back_keyboard()
            )
            return

        # Approved user — session maango
        context.user_data["waiting_session"] = True
        await query.edit_message_caption(
            caption=SESSION_ASK_TEXT,
            parse_mode="Markdown",
            reply_markup=back_keyboard()
        ) if query.message.photo else await query.edit_message_text(
            text=SESSION_ASK_TEXT,
            parse_mode="Markdown",
            reply_markup=back_keyboard()
        )

    elif data == "back":
        if query.message.photo:
            await query.edit_message_caption(
                caption=START_TEXT,
                parse_mode="Markdown",
                reply_markup=main_keyboard()
            )
        else:
            await query.edit_message_text(
                text=START_TEXT,
                parse_mode="Markdown",
                reply_markup=main_keyboard()
            )
