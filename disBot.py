import openai
from discord.ext import commands
import discord
from dotenv import dotenv_values
from keep_alive import keep_alive

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has awakened')

@bot.command()
async def gpt(ctx, *, query):
    print(query)
    output = openai.Completion.create(
        engine="text-davinci-003",
        prompt=query,
        temperature=1,
        max_tokens=100,
    )
    text = output['choices'][0]['text']
    print(text)
    await ctx.send(text)

bot.run(config["DISCORD_BOT_KEY"])
