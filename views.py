import discord
from db.db import DB

from embeds import mapEmbed, menuEmbed


class EatWhatView(discord.ui.View):
    def __init__(self, db: DB, record_id: int):
        super().__init__()

        self.db = db
        self.record_id = record_id
        self.self_rate = 0.5

        # self.add_item(discord.ui.Button(label="測試按鈕"))

    # TODO: 按下特定按鈕時要會紀錄喜好值
    # TODO: 完善爬蟲後搞定地圖與菜單

    # @discord.ui.button(label="地圖", emoji="🗺️")
    # async def map(self, interation: discord.Interaction, button: discord.ui.Button):
    #     embed = mapEmbed()
    #     await interation.response.send_message(embed=embed)

    # @discord.ui.button(label="菜單", emoji="📰")
    # async def menu(self, interation: discord.Interaction, button: discord.ui.Button):
    #     embed = menuEmbed()
    #     await interation.response.send_message(embed=embed)

    @discord.ui.button(emoji="👍")
    async def like(self, interation: discord.Interaction, button: discord.ui.Button):
        self.self_rate = 1
        self.db.updateRecordRate(id=self.record_id, new_rate=self.self_rate)
        await interation.response.send_message(content="感謝您的意見，往後將會推薦類似商家")

    @discord.ui.button(emoji="👎")
    async def dislike(self, interation: discord.Interaction, button: discord.ui.Button):
        self.self_rate = -1
        self.db.updateRecordRate(id=self.record_id, new_rate=self.self_rate)
        await interation.response.send_message(content="感謝您的意見，下次將不會推薦類似商家")