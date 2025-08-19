import os
import discord
import cohere
from keep_alive import keep_alive

# --- Beállítások Secrets-ből ---
DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
COHERE_API_KEY = os.environ.get("COHERE_API_KEY")

if not DISCORD_TOKEN or not COHERE_API_KEY:
    raise ValueError("❌ Hiányzik a DISCORD_TOKEN vagy COHERE_API_KEY a Secrets-ből!")

co = cohere.Client(COHERE_API_KEY)

# --- Discord bot beállítások ---
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
client = discord.Client(intents=intents)

# Felhasználónkénti beszélgetési memória
conversation_history = {}

@client.event
async def on_ready():
    print(f"✅ Bejelentkezve mint {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    user_id = str(message.author.id)
    content = message.content.strip()

    # --- AI parancs ---
    if content.startswith("!ai"):
        user_message = content.replace("!ai", "", 1).strip()

        if user_id not in conversation_history:
            conversation_history[user_id] = []

        try:
            # Cohere API hívás (gyorsabb modell)
            response = co.chat(
                model="command-r",
                message=user_message,
                chat_history=conversation_history[user_id],
                temperature=0.7
            )

            answer = response.text.strip()

            # Előzmények mentése
            conversation_history[user_id].append({"role": "USER", "message": user_message})
            conversation_history[user_id].append({"role": "CHATBOT", "message": answer})

            await message.channel.send(answer)

        except Exception as e:
            await message.channel.send(f"⚠️ Hiba történt: {e}")
            print(e)

    # --- CLEAR parancs ---
    elif content.startswith("!clear"):
        try:
            if user_id in conversation_history:
                del conversation_history[user_id]

            async for msg in message.channel.history(limit=100):
                if msg.author == client.user:  # bot üzenete
                    await msg.delete()
                elif msg.author == message.author and msg.content.startswith("!ai"):
                    await msg.delete()

            await message.channel.send("🧹 Az AI-val folytatott beszélgetés törölve!")

        except Exception as e:
            await message.channel.send(f"⚠️ Nem sikerült törölni: {e}")
            print(e)

# --- Keep-alive indítása ---
keep_alive()

# --- Bot futtatása ---
client.run(DISCORD_TOKEN)