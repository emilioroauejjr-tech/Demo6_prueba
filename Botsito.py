import discord
from discord.ext import commands
from bot_logic import gen_pass

TOKEN = "MTQ3ODUwODYyOTA1NjI5NTA5Mw.Gs3_s1.NVhu1MDkygVCqFw-Slwz2eUSrlfFCxVIw0nECo"

intents = discord.Intents.default()
intents.message_content = True  # OBLIGATORIO para prefijos

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Conectado como {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.command()
async def password(ctx, length: int):
    generated = gen_pass(length)
    await ctx.send("Tu contraseña es: {generated}")

bot.run(TOKEN)
