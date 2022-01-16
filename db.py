import sqlite3
from sqlalchemy import create_engine

def create_connection():
    engine = create_engine('sqlite:///pl.db', echo = True)
    #conn = sqlite3.connect("./pl.db")
    #return conn
