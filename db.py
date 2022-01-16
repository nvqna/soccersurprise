import sqlite3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from datetime import datetime, timedelta
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker

def create_connection():
    engine = create_engine('sqlite:///pl.db', echo = True)
    Session = sessionmaker(bind=engine)
    s = Session()
    return s
    #conn = sqlite3.connect("./pl.db")
    #return conn
