# ⍣⃪‌ ᶦ ‌ᵃᵐ⛦⃕‌𝑺𝑻𝑨𝑹𝑲 𝑼𝑺𝑬𝑹𝑩𝑶𝑻❛𝆺𝅥⤹࿗𓆪ꪾ™
> ***ʙʏ ᴍɪsᴛᴇʀ sᴛᴀʀᴋ***

---

## ━━━━━━━━━━━━━━━━━━━━━━
## 📁 FOLDER STRUCTURE
## ━━━━━━━━━━━━━━━━━━━━━━

```
stark-userbot/
│
├── main.py                      ← Tumhara khud ka userbot start karo
├── config.py                    ← Userbot ki API keys yahan
├── helpers.py                   ← Internal functions (touch mat karna)
├── generate_session.py          ← String session banane ke liye
├── requirements.txt             ← Sabhi packages
│
├── assets/
│   ├── qr.jpg                   ← Tumhara QR code (.qr command ke liye)
│   └── start.jpg                ← Bot ka welcome image
│
├── plugins/                     ← Userbot ke saare commands
│   ├── osint/
│   │   └── lookup.py            ← .num  .tg  .whois
│   ├── utils/
│   │   ├── tools.py             ← .qr  .spam
│   │   ├── tools2.py            ← .tr  .tts  .calc
│   │   ├── group.py             ← .kick .ban .mute .pin .purge .promote .demote
│   │   └── help.py              ← .help
│   └── fun/
│       ├── flex.py              ← .alive .afk .ghost .bio .ping .uptime .id
│       └── tagging.py           ← .tagall .gmtag .gntag
│
└── bot/                         ← Telegram Bot (dusron ko userbot dene ke liye)
    ├── bot_main.py              ← Bot start karo yahan se
    ├── config.py                ← Bot ki settings
    ├── database.py              ← Users ka data (SQLite)
    ├── userbot_manager.py       ← Users ke userbots manage karta hai
    └── handlers/
        ├── start.py             ← /start + inline buttons
        ├── owner.py             ← Owner commands
        └── session.py           ← User ka session lena
```

---

## ━━━━━━━━━━━━━━━━━━━━━━
## ⚙️ PART 1 — APNA USERBOT SETUP
## ━━━━━━━━━━━━━━━━━━━━━━

### 🔹 STEP 1 — Packages install karo

```bash
pip install -r requirements.txt
```

---

### 🔹 STEP 2 — API ID aur API HASH lo

1. Browser mein kholo: **https://my.telegram.org**
2. Apne Telegram number se login karo
3. Click karo **"API Development Tools"**
4. Ek app banao — koi bhi naam daal do
5. Milega:
   - `App api_id` → **API_ID**
   - `App api_hash` → **API_HASH**

---

### 🔹 STEP 3 — config.py fill karo (root wala)

```python
API_ID         = 12345678
API_HASH       = "abcd1234..."
STRING_SESSION = ""           # Abhi khali — Step 4 mein aayega

NUM_API_URL    = "https://..."  # Phone lookup API
TG_API_KEY     = "xxxx"         # TG lookup key
```

---

### 🔹 STEP 4 — String Session banao

```bash
python generate_session.py
```

- Phone number daalo (+91xxxxxxxxxx)
- OTP daalo
- Lambi string milegi → copy karo → `STRING_SESSION` mein daalo

> ⚠️ String session kisi ko mat dena

---

### 🔹 STEP 5 — Apna userbot chalaao

```bash
python main.py
```

---

## ━━━━━━━━━━━━━━━━━━━━━━
## ⚙️ PART 2 — TELEGRAM BOT SETUP
## ━━━━━━━━━━━━━━━━━━━━━━

> Yeh bot dusron ko tumhara userbot system use karne deta hai

### 🔹 STEP 1 — Bot Token lo

1. Telegram pe **@BotFather** kholo
2. `/newbot` karo
3. Naam aur username do
4. Token milega — copy karo

---

### 🔹 STEP 2 — bot/config.py fill karo

```python
BOT_TOKEN  = "123456:ABC-xxxx"   # BotFather se mila token
OWNER_ID   = 123456789           # Tumhara Telegram user ID
OWNER_USER = "misterstark"       # Tumhara username (without @)
```

> Apna user ID nahi pata? @userinfobot pe `/start` karo

---

### 🔹 STEP 3 — Welcome image rakhna (optional)

- Koi bhi image rename karke `start.jpg` karo
- `assets/` folder mein rakh do
- Nahi rakha toh sirf text aayega — koi dikkat nahi

---

### 🔹 STEP 4 — Bot chalaao

```bash
python bot/bot_main.py
```

---

## ━━━━━━━━━━━━━━━━━━━━━━
## 🔄 DONO EK SAATH CHALANA
## ━━━━━━━━━━━━━━━━━━━━━━

**Terminal 1 — Tumhara userbot:**
```bash
python main.py
```

**Terminal 2 — Telegram Bot:**
```bash
python bot/bot_main.py
```

> VPS pe ho toh `screen` ya `tmux` use karo dono alag rakhne ke liye

---

## ━━━━━━━━━━━━━━━━━━━━━━
## 👑 OWNER COMMANDS (BOT)
## ━━━━━━━━━━━━━━━━━━━━━━

| Command | Usage | Kya karta hai |
|---|---|---|
| `/approve` | `/approve 123456789` | User ko access deta hai |
| `/unapprove` | `/unapprove 123456789` | Access wapas leta hai |
| `/ban` | `/ban 123456789` | User ko ban karta hai |
| `/unban` | `/unban 123456789` | Ban hatata hai |
| `/stats` | `/stats` | Total users, active bots ka data |
| `/users` | `/users` | Sabhi users ki list |
| `/broadcast` | `/broadcast Koi bhi message` | Sabko message bhejta hai |

---

## ━━━━━━━━━━━━━━━━━━━━━━
## 👤 USER FLOW (BOT)
## ━━━━━━━━━━━━━━━━━━━━━━

```
User → /start
         ↓
   Welcome Image + Message
         ↓
   3 Inline Buttons:
   ├── 👑 Owner        → Owner info (sabke liye)
   ├── 📋 Help         → Commands list (sabke liye)
   └── ➕ Add Session  → Approved: session maango
                         Not approved: "Owner se contact karo"
```

**Jab user session deta hai:**
1. Bot session verify karta hai
2. Valid hai toh userbot start ho jaata hai
3. Database mein save ho jaata hai
4. Bot restart ho toh bhi automatically restore ho jaata hai

---

## ━━━━━━━━━━━━━━━━━━━━━━
## 📋 USERBOT COMMANDS
## ━━━━━━━━━━━━━━━━━━━━━━

> Sab commands `.` (dot) se start hote hain

### 🔍 OSINT
| Command | Usage | Kya karta hai |
|---|---|---|
| `.num` | `.num 9876543210` | Phone number info |
| `.tg` | `.tg 123456` ya reply + `.tg` | Telegram ID info |
| `.whois` | Reply + `.whois` | User ka naam, ID, username |

### 🛠️ UTILS
| Command | Usage | Kya karta hai |
|---|---|---|
| `.qr` | `.qr` | QR code bhejo |
| `.spam` | `.spam Hello 5` | 5 baar message bhejo |
| `.tr` | `.tr hi Hello` | Translate karo |
| `.tts` | `.tts Kaise ho` | Voice message banao |
| `.calc` | `.calc 25*4+10` | Calculator |

### 👥 GROUP TOOLS
| Command | Usage | Kya karta hai |
|---|---|---|
| `.kick` | Reply + `.kick` | User ko nikalo |
| `.ban` | Reply + `.ban` | Ban karo |
| `.unban` | `.unban @user` | Unban karo |
| `.mute` | Reply + `.mute` | Mute karo |
| `.unmute` | Reply + `.unmute` | Unmute karo |
| `.pin` | Reply + `.pin` | Pin karo |
| `.purge` | Reply + `.purge` | Messages delete karo |
| `.promote` | Reply + `.promote` | Admin banao |
| `.demote` | Reply + `.demote` | Admin hatao |

### 😎 FUN & FLEX
| Command | Usage | Kya karta hai |
|---|---|---|
| `.alive` | `.alive` | Status check |
| `.afk` | `.afk So raha hun` | AFK on/off |
| `.ghost` | `.ghost Text` | 5s baad delete |
| `.bio` | `.bio Mister Stark` | Bio change |
| `.tagall` | `.tagall Text` | Sabko tag |
| `.gmtag` | `.gmtag` | Good Morning tag |
| `.gntag` | `.gntag` | Good Night tag |

### 📊 STATS
| Command | Usage | Kya karta hai |
|---|---|---|
| `.ping` | `.ping` | Response time |
| `.uptime` | `.uptime` | Kitne time se chal raha |
| `.id` | `.id` | Chat/User ID |

### ❓ HELP
| Command | Usage |
|---|---|
| `.help` | Saari categories |
| `.help osint` | Sirf OSINT |
| `.help group` | Sirf Group Tools |
| `.help utils` | Sirf Utils |
| `.help fun` | Sirf Fun |
| `.help stats` | Sirf Stats |

---

## ━━━━━━━━━━━━━━━━━━━━━━
## ❌ COMMON ERRORS
## ━━━━━━━━━━━━━━━━━━━━━━

| Error | Solution |
|---|---|
| `ModuleNotFoundError` | `pip install -r requirements.txt` dobara chalao |
| `SESSION_REVOKED` | `generate_session.py` dobara chalao |
| `ChatAdminRequired` | Group mein admin banao |
| Bot respond nahi kar raha | `BOT_TOKEN` check karo `bot/config.py` mein |
| Userbot start nahi ho raha | `STRING_SESSION` check karo `config.py` mein |
| `.tts` kaam nahi karta | `pip install gTTS` |
| `.tr` kaam nahi karta | `pip install deep-translator` |

---

> ❁═══⟬ 𝑶𝒘𝒏𝒆𝒓: ᴍɪsᴛᴇʀ sᴛᴀʀᴋ ⟭═══❁
