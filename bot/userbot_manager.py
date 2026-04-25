import asyncio
import sys
import os
from pyrogram import Client

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   Active userbots store
#   { user_id: pyrogram.Client }
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

_active_bots: dict[int, Client] = {}


async def start_userbot(user_id: int, session_string: str) -> tuple[bool, str]:
    """
    Start a userbot for given user_id using their session_string.
    Returns (True, "") on success or (False, error_message) on failure.
    """
    # Import userbot's API credentials
    sys.path.insert(0, os.path.abspath("."))
    from config import API_ID, API_HASH

    try:
        # Stop existing if any
        await stop_userbot(user_id)

        client = Client(
            name=f"user_{user_id}",
            session_string=session_string,
            api_id=API_ID,
            api_hash=API_HASH,
            plugins=dict(root="plugins")
        )

        await client.start()
        _active_bots[user_id] = client
        return True, ""

    except Exception as e:
        return False, str(e)


async def stop_userbot(user_id: int):
    """Stop and remove userbot for given user_id."""
    if user_id in _active_bots:
        try:
            await _active_bots[user_id].stop()
        except Exception:
            pass
        del _active_bots[user_id]


def get_active_count() -> int:
    return len(_active_bots)


async def restore_all_userbots():
    """
    Called on bot startup — restores all userbots
    for users who already have sessions saved.
    """
    from bot.database import get_all_users

    users = get_all_users()
    restored = 0
    failed   = 0

    for uid, uname, approved, banned, session, _ in users:
        if not approved or banned or not session:
            continue
        success, err = await start_userbot(uid, session)
        if success:
            restored += 1
            print(f"  ✅ Restored userbot: {uid} (@{uname})")
        else:
            failed += 1
            print(f"  ❌ Failed userbot: {uid} — {err}")

    print(f"\n  Total restored: {restored} | Failed: {failed}")
