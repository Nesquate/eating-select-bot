import discord


def eatEmbed(keyword, title) -> discord.Embed:
    embed = discord.Embed(
                title="今天吃什麼",
                description=f"吃 **{keyword}**",
                colour=discord.Colour.blue()
            )
    embed.add_field(name="商家", value=f"**{title}**")

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