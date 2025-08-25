import discord
from discord.ext import commands
import random
import os

# --------------------------
# Discord Bot Setup
# --------------------------
intents = discord.Intents.default()
intents.message_content = True  # Required for reading messages

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

# --------------------------
# Run the bot using environment variable
# --------------------------
bot.run(os.environ['TOKEN'])

