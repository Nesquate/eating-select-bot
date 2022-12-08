import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from bot import EatWhatBot
from embeds import eatEmbed
from providers.googlemap_crawler import GoogleMapCrawler

from views import EatWhatView

def main():

    load_dotenv()
    
    if os.getenv("BOT_TOKEN") != None:
        TOKEN =  os.getenv("BOT_TOKEN")

        # Set intents
        intents = discord.Intents.default()
        intents.message_content = True

        bot = EatWhatBot(intents=intents)

        @bot.command()
        async def eat(ctx: commands.Context, keyword="1"):
            if(keyword == "1"):
                await ctx.send("你沒有輸入任何文字!")
            else:
                map = GoogleMapCrawler()
                (title, rate, tag, address) = map.search(keyword)
                embed = eatEmbed(keyword=keyword, title=title)
                await ctx.send(embed=embed, view=EatWhatView())

        bot.run(token=TOKEN)
    else:
        print("缺少\"BOT_TOKEN\"環境變數，無法啟動! ")


if __name__ == "__main__":
    main()

