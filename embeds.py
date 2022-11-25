import discord


def eatEmbed() -> discord.Embed:
    embed = discord.Embed(
                title="今天吃什麼",
                description="吃 **(等待填入)**",
                colour=discord.Colour.blue()
            )
    embed.add_field(name="商家", value="**(預計商家填寫位置)**")

    return embed

def mapEmbed() -> discord.Embed:
    embed = discord.Embed(
            title="地圖",
            description="以下為此商家的地圖",
            colour=discord.Colour.green()
        )

    embed.set_image(url="https://avatars.githubusercontent.com/u/49124428")

    return embed

def menuEmbed() -> discord.Embed:
    embed = discord.Embed(
        title="菜單",
        colour=discord.Colour.green()
    )

    embed.set_image(url="https://avatars.githubusercontent.com/u/49124428")
    
    return embed