import discord
import asyncio
import os
from datetime import datetime

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = 1397256653396775156  

intents = discord.Intents.default()
client = discord.Client(intents=intents)


shame_messages = [
    "I FAILED to wake up. Again. #DisciplineFailure",
    "Another fake grind day. Slept through it. #Shame",
    "Excuses 1, Me 0. #WeakMind",
    "If I keep this up, I deserve to fail. #FixYourself",
    "I lost to the alarm clock. #NoDiscipline"
]

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    
    file_path = "wake_up.txt"
    now = datetime.now()
    deadline_hour = 10
    deadline_minute = 30

    if now.hour > deadline_hour or (now.hour == deadline_hour and now.minute >= deadline_minute):
        try:
            with open(file_path, "r") as f:
                status = f.read().strip().lower()
        except:
            status = ""

        if status != "awake":
            channel = client.get_channel(CHANNEL_ID)
            for msg in shame_messages:
                await channel.send(msg)
                await asyncio.sleep(5)
        else:
            print("✅ You woke up on time.")
    await client.close()

client.run(TOKEN)
