from sqlalchemy import create_engine, select
from sqlalchemy.engine import Row
from sqlalchemy.orm import Session
from db.tables import *

URI = "sqlite:///database.sqlite"

class DB:
    def __init__(self) -> None:
        self.engine = create_engine(URI, echo=True, future=True)
        Base.metadata.create_all(self.engine)

    def getKeywords(self) -> list():
        getCommand = select(Keywords.keyword)
        print(getCommand)

        with Session(self.engine) as session:
            result = session.execute(getCommand)
            keywords_list = result.all()
            
        return keywords_list

    def checkKeyword(self, keyword:String):
        getCommand = select(Keywords).where(Keywords.keyword == keyword)

        with Session(self.engine) as session:
            result = session.execute(getCommand)
            result_list = result.all()
        
        return result_list

    
    def storeKeyword(self, keyword: str) -> None:
        keyword_data = Keywords(keyword=keyword)

        with Session(self.engine) as session:
            session.add(keyword_data)
            session.commit()

    def storeModel():
        pass

    def getModelFromUser():
        pass

    def storeSearchRecord(self, discord_id:str, title:str, keyword:str, map_rate:str, tag:str, map_address:str) -> None:
        searchRecord = SearchRecord(discord_id=discord_id, title=title, keyword=keyword, map_rate=map_rate, tag=tag, address=map_address, self_rate=0.5)

        with Session(self.engine) as session:
            session.add(searchRecord)
            session.commit()

    def getSearchRecoreds(self, discord_id:str) -> list():
        getCommand = select(SearchRecord).where(SearchRecord.discord_id == discord_id)

        with Session(self.engine) as session:
            searchRecords = session.execute(getCommand)

        return searchRecords
    
    
