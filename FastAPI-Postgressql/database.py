from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABESE_URL = 'postgresql://postgres.vgcbavtvzqkkawkyfkqz:Assasstion21@aws-0-ap-south-1.pooler.supabase.com:6543/postgres'

engine = create_engine(DATABESE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()