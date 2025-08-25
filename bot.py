import discord
from discord.ext import commands
import random

TOKEN = "MTQwOTY1MTA1MjQ0NTQzMzk2NQ.GDWPOe.DP86SysI0CsD65fqaY4qNRcFB2qtDCs9UNsMv4"  # paste the token you copied

intents = discord.Intents.default()
intents.message_content = True  # 👈 this is the important line!

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
async def pop(ctx, size: int = 6, nails: int = 3):
    """
    Bubble wrap game: !pop [size] [nails]
    Example: !pop 6 3 -> 6x6 grid with 3 nails
    """
    total_cells = size * size
    grid = ["||POP!||"] * total_cells

    nail_positions = random.sample(range(total_cells), nails)
    for pos in nail_positions:
        grid[pos] = "||NAIL||"

    output = ""
    for i in range(size):
        row = "".join(grid[i * size:(i + 1) * size])
        output += row + "\n"

    await ctx.send(output)

bot.run(TOKEN)
