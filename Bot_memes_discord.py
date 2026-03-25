import discord
import random
import requests
from discord.ext import commands

# Configuración de intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
# Prefijo de comandos
bot = commands.Bot(command_prefix="$", intents=intents)

# Función para obtener un meme aleatorio de pato
def get_duck_image_url():
    url = "https://random-d.uk/api/v2/random"
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command()
async def meme(ctx):
    lista = [
        "images/meme1.jpg",
        "images/meme2.jpg",
        "images/meme3.jpg"
    ]

    nombre_random = random.choice(lista)

    with open(nombre_random, 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send("😂 Aquí tienes tu meme:", file=picture)

# Evento cuando el bot se conecta
@bot.event
async def on_ready():   
    print(f"✅ Bot conectado como {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    await bot.process_commands(message)

@bot.command()
async def ayuda(ctx):
    await ctx.send(
        "📋 Lista de comandos:\n"
        "$meme → envía un meme aleatorio\n"
        "$mostrar_imagenes [nombre] → muestra una imagen específica\n"
        "$duck → envía una imagen aleatoria de un pato\n"
        "$animales → envía un meme de animales\n"
        "$ayuda → muestra esta ayuda"
    )

@bot.command()
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def animales(ctx):
    try:
        lista = [
            "images/animal1.jpg",
            "images/animal2.jpg",
            "images/animal3.jpg"
        ]

        nombre_random = random.choice(lista)

        with open(nombre_random, "rb") as f:
            picture = discord.File(f)
            await ctx.send("🐶 Aquí tienes tu meme de animales:", file=picture)

    except Exception as e:
        await ctx.send(f"❌ Error: {e}")

@bot.command()
async def mostrar_imagenes(ctx, nombre: str):
    try:
        with open(nombre, 'rb') as f:
            # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
            picture = discord.File(f)
            # A continuación, podemos enviar este archivo como parámetro.
            await ctx.send(file=picture)
    except FileNotFoundError:
        await ctx.send("❌ No se encontró la imagen.")


bot.run("TU_TOKEN_AQUI")
