from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://root:1002025918Ds@practica1.cfayxotfiehc.us-east-1.rds.amazonaws.com/practica1')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
