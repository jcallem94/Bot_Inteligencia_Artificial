import discord
from discord.ext import commands
from modelo import modelo

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachments in  ctx.message.attachments:
            file_name = attachments.filename
            image_path = f"./image/{file_name}"
            file_url = attachments.url
            await attachments.save(f"./image/{file_name}")
            result, final_result = modelo("keras_model.h5", "labels.txt",image_path)
            for i in range(len(result)):
                await ctx.send(result[i])

            await ctx.send("Predicción final: ")
            await ctx.send(final_result[0])
            await ctx.send(final_result[1])

    else:
        await ctx.send("Olvidaste adjuntar la imagen :(")

bot.run("¡Acá va tu TOKEN!")
