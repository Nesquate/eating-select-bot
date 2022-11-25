import discord


def eatEmbed():
    embed = discord.Embed(
                title="今天吃什麼",
                description="吃 **(等待填入)**",
                colour=discord.Colour.blue()
            )
    embed.add_field(name="商家", value="**(預計商家填寫位置)**")

    return embed