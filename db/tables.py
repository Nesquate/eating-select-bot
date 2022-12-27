import datetime
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserPref(Base):
    __tablename__ = "user_pref"
    id = Column(Integer, primary_key=True, autoincrement=True)
    discord_id = Column(String)
    model_uri = Column(String) # TODO: change type to uri (?)
    last_update = Column(String)

class SearchRecord(Base):
    __tablename__ = "search_record"
    id = Column(Integer, primary_key=True, autoincrement=True)
    discord_id = Column(String)
    keyword = Column(String)
    rate = Column(Float)
    date = Column(String)

    def __init__(self, discord_id:str, keyword:str):
        self.discord_id = discord_id
        self.keyword = keyword
        self.rate = 0.5
        self.date = str(datetime.datetime.now().timestamp())

class Keywords(Base):
    __tablename__ = "keywords"
    id = Column(Integer, primary_key=True, autoincrement=True)
    keyword = Column(String)
    add_date = Column(String)

    def __init__(self, keyword:String):
        self.keyword = keyword
        self.add_date = str(datetime.datetime.now().timestamp())
