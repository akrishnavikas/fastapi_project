from sqlalchemy.orm import  sessionmaker
from sqlalchemy import create_engine


dburl = "postgresql://postgres:postgres@localhost:5432/sampletemp"
engine = create_engine(dburl)
session = sessionmaker(autocommit=False, autoflush=False,bind=engine)