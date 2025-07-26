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
    "I lost to the alarm clock. #NoDiscipline",
    "KARTAVAY is a WEAKLING",
    "Kartavay is not pushing his limits not trying to do better than his best. How can he choose to become a weakling if even if he has all those great people in front of him"
]

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    
    file_path = "wake_up.txt"
    log_path = "fail_log.txt"
    now = datetime.now()

    try:
        with open(file_path, "r") as f:
            status = f.read().strip().lower()
    except:
        status = ""

    if status == "awake":
        print("✅ You woke up on time.")
    else:
        if now.hour > 4 or (now.hour == 4 and now.minute >= 0):
            channel = client.get_channel(CHANNEL_ID)
            for msg in shame_messages:
                await channel.send(msg)
                await asyncio.sleep(5)

            with open(log_path, "a") as f:
                f.write(f"Missed wake-up on {now.strftime('%Y-%m-%d %H:%M:%S')}\n")

    await client.close()

client.run(TOKEN)
