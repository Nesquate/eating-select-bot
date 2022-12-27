from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from db.tables import *

URI = "sqlite:///database.sqlite"

class DB:
    def __init__(self) -> None:
        self.engine = create_engine(URI, echo=True, future=True)
        Base.metadata.create_all(self.engine)

    def getKeywords(self) -> list():
        getCommand = select(Keywords.c.keywords)

        with Session(self.engine) as session:
            keywords_list = session.execute(getCommand)

        return keywords_list
    
    def storeKeyword(self, keyword: str) -> None:
        keyword_data = Keywords(keyword=keyword)

        with Session(self.engine) as session:
            session.add(keyword_data)
            session.commit()

    def storeModel():
        pass

    def getModelFromUser():
        pass

    def storeSearchRecord(self, discord_id:str, keyword:str) -> None:
        searchRecord = SearchRecord(discord_id=discord_id, keyword=keyword)

        with Session(self.engine) as session:
            session.add(searchRecord)
            session.commit()

    def getSearchRecoreds(self, discord_id:str) -> list():
        getCommand = select(SearchRecord).where(SearchRecord.discord_id == discord_id)

        with Session(self.engine) as session:
            searchRecords = session.execute(getCommand)

        return searchRecords
    
    
