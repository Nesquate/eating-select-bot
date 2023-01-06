import random
import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from bot import EatWhatBot
from db.db import DB
from embeds import eatEmbed
from providers.googlemap_crawler import GoogleMapCrawler
from train.train import Train

from views import EatWhatView

def main():

    load_dotenv()
    
    if os.getenv("BOT_TOKEN") != None:
        TOKEN =  os.getenv("BOT_TOKEN")

        # Set intents
        intents = discord.Intents.default()
        intents.message_content = True

        bot = EatWhatBot(intents=intents)

        db = DB()
        train = Train(db=db)

        @bot.command()
        async def eat(ctx: commands.Context, keyword="_"):
            predict = None
            
            if(keyword == "_"):
                keywords_list = db.getKeywords() 
                if len(keywords_list) == 0:
                    await ctx.send("你沒有輸入任何文字!")
                    return
                else:
                    # Row list 經觀察可以把他當 tuple 來看，所以要解包兩次 (一次 list 一次 tuple)
                    keyword = keywords_list[round(random.randint(0, len(keywords_list)-1))][0]
                    # TODO: 使用使用者喜好模型預測使用者喜好的關鍵字或店家
                    predict = train.predict(discord_id=str(ctx.author.id))

            else:
                if len(db.checkKeyword(keyword=keyword)) == 0:
                    db.storeKeyword(keyword)

            map = GoogleMapCrawler()
            
            try:
                if(predict != None):
                    (title_pred, rate_pred, tag_pred, address_pred) = map.search(predict)
                    embed = eatEmbed(keyword=predict, title=title_pred)
                    if len(db.checkKeyword(keyword=tag_pred)) == 0:
                        db.storeKeyword(tag_pred)
                    
                    id = db.storeSearchRecord(str(ctx.author.id), title=title_pred, keyword=predict, map_rate=rate_pred, tag=tag_pred, map_address=address_pred)
                else:
                    (title, rate, tag, address) = map.search(keyword)
                    embed = eatEmbed(keyword=keyword, title=title)
                    if len(db.checkKeyword(keyword=tag)) == 0:
                        db.storeKeyword(tag)
                    
                    id = db.storeSearchRecord(str(ctx.author.id), title=title, keyword=keyword, map_rate=rate, tag=tag, map_address=address)

                print(f"Debug: Search record id: {id}")

                # TODO: Store user id & keyword to model for training

                await ctx.send(embed=embed, view=EatWhatView(db=db, record_id=id, discord_id=str(ctx.author.id)))

                train.genModel(str(ctx.author.id))
            except Exception as e:
                print(e)
                await ctx.send(f"原本想推薦你吃 {keyword if predict is None else predict}，但很抱歉系統出錯了QQ")
        bot.run(token=TOKEN)
    else:
        print("缺少\"BOT_TOKEN\"環境變數，無法啟動! ")


if __name__ == "__main__":
    main()

