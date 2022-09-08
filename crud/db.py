from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://root:8001@localhost/practica_1')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()