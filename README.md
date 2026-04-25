# ⍣⃪‌ ᶦ ‌ᵃᵐ⛦⃕‌𝑺𝑻𝑨𝑹𝑲 𝑼𝑺𝑬𝑹𝑩𝑶𝑻❛𝆺𝅥⤹࿗𓆪ꪾ™
> ***ʙʏ ᴍɪsᴛᴇʀ sᴛᴀʀᴋ***

---

## ━━━━━━━━━━━━━━━━━━━━━━
## 📁 FOLDER STRUCTURE
## ━━━━━━━━━━━━━━━━━━━━━━

```
stark-userbot/
│
├── main.py                  ← Yahan se userbot start hoga
├── config.py                ← Apni API keys aur settings yahan bharo
├── helpers.py               ← Internal utility functions (touch mat karna)
├── generate_session.py      ← Pehli baar chalana — string session milegi
├── requirements.txt         ← Sabhi packages ki list
│
├── assets/
│   └── qr.jpg               ← Apna QR code image yahan rakhna
│
└── plugins/                 ← Saare commands yahan hain
    ├── osint/
    │   └── lookup.py        ← .num  .tg  .whois
    ├── utils/
    │   ├── tools.py         ← .qr  .spam
    │   ├── tools2.py        ← .tr  .tts  .calc
    │   ├── group.py         ← .kick .ban .mute .pin .purge .promote .demote
    │   └── help.py          ← .help
    └── fun/
        ├── flex.py          ← .alive .afk .ghost .bio .ping .uptime .id
        └── tagging.py       ← .tagall .gmtag .gntag
```

---

## ━━━━━━━━━━━━━━━━━━━━━━
## ⚙️ SETUP — STEP BY STEP
## ━━━━━━━━━━━━━━━━━━━━━━

### 🔹 STEP 1 — API ID aur API HASH lo

1. Browser mein kholo: **https://my.telegram.org**
2. Apne Telegram number se login karo
3. Click karo **"API Development Tools"**
4. Ek app banao — koi bhi naam daal do
5. Tumhe milega:
   - `App api_id` → yeh hai tumhara **API_ID**
   - `App api_hash` → yeh hai tumhara **API_HASH**

---

### 🔹 STEP 2 — Packages install karo

Terminal/CMD kholo aur yeh command chalaao:

```bash
pip install -r requirements.txt
```

---

### 🔹 STEP 3 — config.py mein API ID aur Hash bharo

`config.py` file kholo aur yeh lines fill karo:

```python
API_ID   = 12345678       # my.telegram.org se mila number
API_HASH = "abcd1234..."  # my.telegram.org se mila hash
```

---

### 🔹 STEP 4 — String Session banao (SIRF EK BAAR)

Terminal mein yeh chalao:

```bash
python generate_session.py
```

- Tumhara phone number manega (country code ke saath, jaise +919876543210)
- Telegram se OTP aayega — woh daalo
- Ek lambi string milegi screen pe — **usse copy karo**

Phir `config.py` mein daalo:

```python
STRING_SESSION = "BQCxxxxxxxxxxxxxxxx..."  # Jo mili woh string
```

> ⚠️ Yeh string kabhi kisi ko mat dena — isse tumhara account access ho sakta hai

---

### 🔹 STEP 5 — OSINT API keys bharo

```python
NUM_API_URL = "https://..."   # Apna phone lookup API URL
TG_API_KEY  = "xxxx"          # Telegram lookup key
```

---

### 🔹 STEP 6 — Apna QR code rakhna (optional)

Agar `.qr` command use karna hai toh:
- Apna QR image rename karke **`qr.jpg`** karo
- `assets/` folder mein rakh do

---

### 🔹 STEP 7 — Userbot chalaao!

```bash
python main.py
```

`ꜱᴛᴀʀᴛɪɴɢ...` dikhe toh sab sahi hai ✅

---

## ━━━━━━━━━━━━━━━━━━━━━━
## 📋 COMMANDS LIST
## ━━━━━━━━━━━━━━━━━━━━━━

> Userbot mein sab commands `.` (dot) se start hote hain
> `.help` likhne par saari categories dikhegi

---

### 🔍 OSINT

| Command | Usage | Kya karta hai |
|---|---|---|
| `.num` | `.num 9876543210` | Phone number ki info nikalta hai |
| `.tg` | `.tg 123456789` ya kisi message ko reply karke `.tg` | Telegram user ID se info nikalta hai |
| `.whois` | Kisi message ko reply karke `.whois` | User ka naam, username, ID sab dikhata hai |

---

### 🛠️ UTILS

| Command | Usage | Kya karta hai |
|---|---|---|
| `.qr` | `.qr` | Tumhara QR code bhejta hai |
| `.spam` | `.spam Hello bhai 5` | Message 5 baar bhejta hai |
| `.tr` | `.tr hi Hello` ya reply + `.tr hi` | Text translate karta hai |
| `.tts` | `.tts Kaise ho` ya reply + `.tts` | Text ko voice message mein convert karta hai |
| `.calc` | `.calc 25 * 4 + 10` | Calculator |

> `.tr` ke liye lang codes: `hi` Hindi, `en` English, `ur` Urdu, `ar` Arabic

---

### 👥 GROUP TOOLS
> ⚠️ Yeh commands sirf tab kaam karenge jab tum group ke admin ho

| Command | Usage | Kya karta hai |
|---|---|---|
| `.kick` | Reply + `.kick` | User ko group se nikaalta hai |
| `.ban` | Reply + `.ban` | User ko ban karta hai |
| `.unban` | `.unban @username` | User ka ban hatata hai |
| `.mute` | Reply + `.mute` | User ko mute karta hai |
| `.unmute` | Reply + `.unmute` | User ko unmute karta hai |
| `.pin` | Reply + `.pin` | Message pin karta hai |
| `.purge` | Reply + `.purge` | Us message se lekar abhi tak saare messages delete karta hai |
| `.promote` | Reply + `.promote` | User ko admin banata hai |
| `.demote` | Reply + `.demote` | Admin ki rights hatata hai |

---

### 😎 FUN & FLEX

| Command | Usage | Kya karta hai |
|---|---|---|
| `.alive` | `.alive` | Userbot ka status aur uptime dikhata hai |
| `.afk` | `.afk So raha hun` | AFK mode on — koi message kare to auto reply jaata hai |
| `.afk` | `.afk` (dobara) | AFK mode off |
| `.ghost` | `.ghost Dekho phir gayab 👻` | Message bhejta hai aur 5 second baad delete kar deta hai |
| `.bio` | `.bio Mister Stark 🔥` | Tumhari Telegram bio change karta hai |
| `.tagall` | `.tagall Dekho kaun hai mere owner` | Group ke sabko tag karta hai custom message ke saath |
| `.gmtag` | `.gmtag` | Sabko ek ek karke Good Morning tag karta hai |
| `.gntag` | `.gntag` | Sabko ek ek karke Good Night tag karta hai |

---

### 📊 STATS

| Command | Usage | Kya karta hai |
|---|---|---|
| `.ping` | `.ping` | Response time check |
| `.uptime` | `.uptime` | Kitne time se chal raha hai |
| `.id` | `.id` ya reply + `.id` | Chat/User ka ID nikalta hai |

---

### ❓ HELP

| Command | Usage | Kya karta hai |
|---|---|---|
| `.help` | `.help` | Saari categories ka overview |
| `.help osint` | `.help osint` | Sirf OSINT commands |
| `.help group` | `.help group` | Sirf Group Tools |
| `.help utils` | `.help utils` | Sirf Utils |
| `.help fun` | `.help fun` | Sirf Fun commands |
| `.help stats` | `.help stats` | Sirf Stats commands |

---

## ━━━━━━━━━━━━━━━━━━━━━━
## ❌ COMMON ERRORS
## ━━━━━━━━━━━━━━━━━━━━━━

| Error | Solution |
|---|---|
| `ModuleNotFoundError` | `pip install -r requirements.txt` dobara chalao |
| `SESSION_REVOKED` | Session expire hui — `generate_session.py` dobara chalao |
| `ChatAdminRequired` | Group mein tumhe admin banana padega |
| `.tts` kaam nahi karta | `pip install gTTS` alag se chalao |
| `.tr` kaam nahi karta | `pip install deep-translator` alag se chalao |

---

> ❁═══⟬ 𝑶𝒘𝒏𝒆𝒓: ᴍɪsᴛᴇʀ sᴛᴀʀᴋ ⟭═══❁
