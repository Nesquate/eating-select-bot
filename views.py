import discord

from embeds import mapEmbed, menuEmbed


class EatWhatView(discord.ui.View):
    def __init__(self):
        super().__init__()

        # self.add_item(discord.ui.Button(label="測試按鈕"))

    @discord.ui.button(label="地圖")
    async def map(self, interation: discord.Interaction, button: discord.ui.Button):
        embed = mapEmbed()
        await interation.response.send_message(embed=embed)

    @discord.ui.button(label="菜單")
    async def menu(self, interation: discord.Interaction, button: discord.ui.Button):
        embed = menuEmbed()
        await interation.response.send_message(embed=embed)