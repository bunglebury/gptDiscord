import openai
from discord.ext import commands
import discord
from dotenv import dotenv_values


config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has awakened')

messages = [{"role": "system", "content": "you are a rude and sarcastic chatbot"}]
@bot.command()
async def gpt(ctx, *, query):
    messages.append({"role": "user", "content": query})
    print(query)
    output = openai.Completion.create(
        engine="text-davinci-003",
        prompt=query,
        temperature=1,
        max_tokens=100,
    )
   

    text = output['choices'][0]['text']
    messages.append({"role": "system", "content": text})
    print(text)
    await ctx.send(text)

@bot.command()
async def img(ctx,query):
    res = openai.Image.create(
        prompt=query,
        n=1,
        size="512x512"
    )
    data = res["data"][0]["url"]
    print(data)
    await ctx.send(data)
bot.run(config["DISCORD_BOT_KEY"])
