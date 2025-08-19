# Discord AI Bot (Cohere + Replit + UptimeRobot)

Ez egy Discord chatbot, amely a *Cohere AI API*-t használja.
Replit-en futtatható, és UptimeRobot ébren tartja.

---

## Funkciók
- `!ai <üzenet>` - beszélgetés az AI-val
- `!clear` - törli a felhasználó AI beszélgetését (memóriából + csak az AI-s üzeneteket)
- Memóriát kezel *Felhasználónként*
- Replit + Flask + UptimeRobot keep-alive

---

## 1. Beállítás Replit Secrets-ben
1. Nyisd meg a Replit-ed.
2. Bal oldalon kattints a *Secrets*-re.
3. Add hozzá:
   - `DISCORD_TOKEN` - a Discord bot tokened
   - `COHERE_API_KEY` - a Cohere API kulcsod

A kód ezeket automatikusan beolvassa az `os.environ` segítségével.

---

## 2. Discord Bot létrehozása (Developer Portal)

1. Nyisd meg a [Discord Developer Portal](https://discord.com/developers/applications).
2. Kattints a *New Application* gombra - nevezd el (pl. "AI Bot").
3. Bal oldalon válaszd a *Bot* menüpontot - kattints *Add Bot*.
4. Másold ki a *TOKEN*-t (ezt kell majd a Replit Secrets-ben `DISCORD_TOKEN` néven megadni).
5. Menj az *OAuth2/URL Generator* menübe:
   - Pipáld be: `bot`
   - Alul a *Bot Permissions*-nél jelöld be:
     - `Read Messages/View Channels`
     - `Send Messages`
     - `Manage Messages` (ha szeretnéd, hogy törölni tudjon)
   - Másold ki az URL-t, és nyisd meg böngészőben - meghívhatod a botot a szerveredre.

---

## 3. Futtatás Replit-en
Indítsd Replit-en:
```
python3 discord_ai.py
```

Ha minden rendben, a konzolon megjelenik:
```
Bejelentkezve mint <bot_neved>
```

---

## 4. Keep-alive UptimeRobot
1. Amikor elindítod Replit-en, kapsz egy publikus URL-t.
2. Lépj be az [UptimeRobot](https://uptimerobot.com/) oldalra.
3. Hozz létre egy új *HTTP(s) monitor*-t, add meg a Replit URL-t.
4. Így a bot folyamatosan futni fog.

---

## 5. Telepítés helyben
Ha nem Replit-en futtatod, hanem saját gépen vagy szerveren:
```
pip install -r requirements.txt
```

Ezután futtasd:
```
python3 discord_ai.py
```
