from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DB_URL = 'postgresql://admin:1234@172.29.168.75:5432/vacation'

Base= DeclarativeBase()

engine: Engine = create_engine(DB_URL)
session_maker = sessionmaker(bind=engine)
