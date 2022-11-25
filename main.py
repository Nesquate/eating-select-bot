import discord
import os
from discord.ext import commands
from dotenv import load_dotenv


def main():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix='?', intents=intents)

    @bot.event
    async def on_ready():
        print(f"Logged in as {bot.user} (ID: {bot.user.id})")
        print("-----")

    @bot.command()
    async def eat(ctx: commands.Context):
        await ctx.send("吃東西!")

    load_dotenv()
    
    if os.getenv("BOT_TOKEN") != None:
        TOKEN =  os.getenv("BOT_TOKEN")
        bot.run(token=TOKEN)
    else:
        print("缺少\"BOT_TOKEN\"環境變數，無法啟動! ")


if __name__ == "__main__":
    main()

