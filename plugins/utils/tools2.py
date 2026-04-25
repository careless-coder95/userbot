import asyncio
import io
from pyrogram import Client, filters
from helpers import build_output, stylish
from config import DIVIDER, OWNER_TAG

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   .ᴛʀ — Translate Text
#   Usage: .tr {lang} {text}  OR  reply + .tr {lang}
#   Example: .tr hi Hello how are you
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@Client.on_message(filters.me & filters.command("tr", prefixes="."))
async def translate_command(client, message):
    args = message.text.split(None, 2)

    if len(args) < 2:
        await message.edit(
            f"**ᴜꜱᴀɢᴇ:**\n"
            f"• `.tr hi Hello world` — direct translate\n"
            f"• Reply + `.tr hi` — replied text translate karo\n\n"
            f"**ʟᴀɴɢ ᴄᴏᴅᴇꜱ:** `hi` Hindi | `en` English | `ur` Urdu | `ar` Arabic"
        )
        return

    lang = args[1].strip()

    if message.reply_to_message and message.reply_to_message.text:
        text = message.reply_to_message.text
    elif len(args) > 2:
        text = args[2].strip()
    else:
        await message.edit("❌ **Text ya reply dena zaroori hai!**")
        return

    await message.edit(f"🌐 **ᴛʀᴀɴꜱʟᴀᴛɪɴɢ...**")

    try:
        from deep_translator import GoogleTranslator
        translated = GoogleTranslator(source="auto", target=lang).translate(text)
        result = (
            f"• {stylish('FROM')} : {text}\n"
            f"• {stylish('TO')} : {translated}\n"
            f"• {stylish('LANG')} : {lang}"
        )
        await message.edit(build_output("❁═════⟬ ᴛʀᴀɴꜱʟᴀᴛᴇ ⟭═════❁", result))
    except Exception as e:
        await message.edit(f"❌ **Error:** `{e}`\n\n`pip install deep-translator` karo pehle!")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   .ᴛᴛꜱ — Text to Speech
#   Usage: .tts {text}  OR  reply + .tts
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@Client.on_message(filters.me & filters.command("tts", prefixes="."))
async def tts_command(client, message):
    args = message.text.split(None, 1)

    if message.reply_to_message and message.reply_to_message.text:
        text = message.reply_to_message.text
    elif len(args) > 1:
        text = args[1].strip()
    else:
        await message.edit("**ᴜꜱᴀɢᴇ:** `.tts {text}` ʏᴀ ʀᴇᴘʟʏ ᴋᴀʀᴋᴇ `.tts`")
        return

    await message.edit("🔊 **ɢᴇɴᴇʀᴀᴛɪɴɢ ᴠᴏɪᴄᴇ...**")

    try:
        from gtts import gTTS
        tts = gTTS(text=text, lang="hi")
        audio = io.BytesIO()
        tts.write_to_fp(audio)
        audio.name = "voice.mp3"
        audio.seek(0)

        await message.delete()
        await client.send_voice(
            chat_id=message.chat.id,
            voice=audio,
            caption=f"🔊 **ᴛᴛꜱ**\n{OWNER_TAG}"
        )
    except Exception as e:
        await message.edit(f"❌ **Error:** `{e}`\n\n`pip install gtts` karo pehle!")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   .ᴄᴀʟᴄ — Calculator
#   Usage: .calc {expression}
#   Example: .calc 25 * 4 + 100 / 2
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@Client.on_message(filters.me & filters.command("calc", prefixes="."))
async def calc_command(client, message):
    args = message.text.split(None, 1)

    if len(args) < 2 or not args[1].strip():
        await message.edit("**ᴜꜱᴀɢᴇ:** `.calc {expression}`\n**ᴇxᴀᴍᴘʟᴇ:** `.calc 25 * 4 + 100`")
        return

    expr = args[1].strip()
    await message.edit(f"🧮 **ᴄᴀʟᴄᴜʟᴀᴛɪɴɢ...**")

    try:
        # Safe eval — only math allowed
        allowed = set("0123456789+-*/(). %")
        if not all(c in allowed for c in expr.replace(" ", "")):
            await message.edit("❌ **Sirf math expressions allowed hain!**")
            return

        answer = eval(expr)
        result = (
            f"• {stylish('INPUT')}  : `{expr}`\n"
            f"• {stylish('RESULT')} : `{answer}`"
        )
        await message.edit(build_output("❁═════⟬ ᴄᴀʟᴄᴜʟᴀᴛᴏʀ ⟭═════❁", result))
    except ZeroDivisionError:
        await message.edit("❌ **Zero se divide nahi kar sakte!**")
    except Exception as e:
        await message.edit(f"❌ **Error:** `{e}`")
