import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Data(Base):
    __tablename__ = 'Data'
    id = Column(Integer, primary_key=True)
    data= Column(String(255), nullable=False)
    date = Column(DateTime(timezone=True), nullable=False)
    time = Column(DateTime(timezone=True), nullable=False)
    def __init__(self,  data, date=datetime.datetime.now(), time=datetime.datetime.now()):
        self.data = data
        self.date = date
        self.time = time

    def __repr__(self):
        return '<Data %r>' % self.data

