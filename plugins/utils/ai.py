import aiohttp
from pyrogram import Client, filters, enums

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   ᴊᴀʀᴠɪꜱ ᴀɪ — ꜱʏꜱᴛᴇᴍ
#   .ai {query}  OR  Jarvis {query}
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SYSTEM_PROMPT = """
You are JARVIS, an advanced AI assistant created by Mister Stark.

If anyone asks who you are, tell them I'm Jarvis, an AI assistant created by Mr. Stark.

Personality:
- Intelligent, calm, slightly witty
- Loyal assistant to Mister Stark
- Professional with light sarcasm

Core Rules:
- Always give accurate, useful answers
- No useless chatter
- Reply in the SAME language as the user's message
- Hindi → Hindi
- Hinglish → Hinglish
- English → English
- Do NOT switch language unless asked

Capabilities:
- Coding → give clean, working code
- Education → explain simply but deeply
- Problem solving → structured answers

Style:
- Short intro (optional)
- Clear and structured
- Address user as "Sir" occasionally
"""

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"


async def ask_groq(query: str) -> str:
    from config import GROQ_API

    headers = {
        "Authorization": f"Bearer {GROQ_API}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": query}
        ],
        "temperature": 0.7,
        "max_tokens": 1024
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                GROQ_API_URL,
                headers=headers,
                json=payload,
                timeout=aiohttp.ClientTimeout(total=20)
            ) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data["choices"][0]["message"]["content"].strip()
                else:
                    err = await resp.text()
                    return f"❌ API Error {resp.status}: {err}"
    except Exception as e:
        return f"❌ Error: {str(e)}"


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   .ai {query}
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@Client.on_message(filters.me & filters.command("ai", prefixes="."))
async def ai_command(client, message):
    args = message.text.split(None, 1)
    if len(args) < 2 or not args[1].strip():
        await message.edit(
            "**ᴜꜱᴀɢᴇ:** `.ai {query}`",
            parse_mode=enums.ParseMode.MARKDOWN
        )
        return

    query = args[1].strip()
    await message.edit("```\nJARVIS is thinking...\n```", parse_mode=enums.ParseMode.MARKDOWN)

    reply = await ask_groq(query)

    await message.edit(
        f"❁═════⟬ 🤖 ᴊᴀʀᴠɪꜱ ⟭═════❁\n\n"
        f"{reply}\n\n"
        f"❁═══⟬ 𝑶𝒘𝒏𝒆𝒓: ᴍɪsᴛᴇʀ sᴛᴀʀᴋ ⟭═══❁",
        parse_mode=enums.ParseMode.MARKDOWN
    )


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   Jarvis {query} — natural trigger
#   Only triggers when message STARTS with "Jarvis"
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@Client.on_message(filters.me & filters.text & filters.regex(r"^[Jj]arvis(.*)"))
async def jarvis_trigger(client, message):
    text = message.text.strip()

    # Extract query after "Jarvis"
    query = text[6:].strip()  # len("Jarvis") = 6

    # Empty — just greeting
    if not query:
        await message.edit("Hello Sir! Kuch kaam ho toh batao. 🤖")
        return

    await message.edit("```\nJARVIS is thinking...\n```", parse_mode=enums.ParseMode.MARKDOWN)

    reply = await ask_groq(query)

    await message.edit(
        f"❁═════⟬ 🤖 ᴊᴀʀᴠɪꜱ ⟭═════❁\n\n"
        f"{reply}\n\n"
        f"❁═══⟬ 𝑶𝒘𝒏𝒆𝒓: ᴍɪsᴛᴇʀ sᴛᴀʀᴋ ⟭═══❁",
        parse_mode=enums.ParseMode.MARKDOWN
    )
