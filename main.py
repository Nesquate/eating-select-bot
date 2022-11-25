import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

class EatWhatView(discord.ui.View):
    def __init__(self):
        super().__init__()

        # self.add_item(discord.ui.Button(label="測試按鈕"))

    @discord.ui.button(label="地圖")
    async def map(self, interation: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="地圖",
            description="以下為此商家的地圖",
            colour=discord.Colour.green()
        )

        embed.set_image(url="https://avatars.githubusercontent.com/u/49124428")
        await interation.response.send_message(embed=embed)


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
        embed = discord.Embed(
            title="今天吃什麼",
            description="吃 **(等待填入)**",
            colour=discord.Colour.blue()
        )
        embed.add_field(name="商家", value="**(預計商家填寫位置)**")

        await ctx.send(embed=embed, view=EatWhatView())

    load_dotenv()
    
    if os.getenv("BOT_TOKEN") != None:
        TOKEN =  os.getenv("BOT_TOKEN")
        bot.run(token=TOKEN)
    else:
        print("缺少\"BOT_TOKEN\"環境變數，無法啟動! ")


if __name__ == "__main__":
    main()

