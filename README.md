# ꜱᴛᴀʀᴋ ᴜꜱᴇʀʙᴏᴛ
> ʙʏ ᴍɪsᴛᴇʀ sᴛᴀʀᴋ

---

## ꜱᴇᴛᴜᴘ

```bash
pip install -r requirements.txt
```

1. `config.py` mein `API_ID` aur `API_HASH` bharo (my.telegram.org se)
2. String session lo:
```bash
python generate_session.py
```
3. `config.py` mein `STRING_SESSION` bharo
4. Apna QR image `assets/qr.jpg` mein rakhna
5. Chalaao:
```bash
python main.py
```

---

## ᴄᴏᴍᴍᴀɴᴅꜱ

### 🔍 OSINT
| Command | Usage | Description |
|---|---|---|
| `.num` | `.num 9876543210` | Phone number lookup |
| `.tg` | `.tg 123456` ya reply + `.tg` | Telegram ID lookup |
| `.whois` | Reply + `.whois` ya `.whois @user` | User info from Telegram |

### 🛠️ UTILS
| Command | Usage | Description |
|---|---|---|
| `.qr` | `.qr` | Apna QR code bhejo |
| `.spam` | `.spam Hello bro 5` | Message N times spam karo |

### 🎉 FUN
| Command | Usage | Description |
|---|---|---|
| `.tagall` | `.tagall {text}` | Sabko tag karo custom text ke saath |
| `.gmtag` | `.gmtag` | Sabko Good Morning tag karo |
| `.gntag` | `.gntag` | Sabko Good Night tag karo |

---

## ꜰᴏʟᴅᴇʀ ꜱᴛʀᴜᴄᴛᴜʀᴇ

```
stark-userbot/
├── main.py
├── config.py
├── helpers.py
├── generate_session.py
├── requirements.txt
├── assets/
│   └── qr.jpg        ← Apna QR yahan rakhna
└── plugins/
    ├── osint/
    │   └── lookup.py  (.num, .tg, .whois)
    ├── utils/
    │   └── tools.py   (.qr, .spam)
    └── fun/
        └── tagging.py (.tagall, .gmtag, .gntag)
```
