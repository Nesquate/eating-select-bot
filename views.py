import discord


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