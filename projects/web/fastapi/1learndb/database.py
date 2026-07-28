## 1 create database connection 

#import engine 
from sqlalchemy import create_engine

# define db storage location 
SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"


# create engine instance and connection db storage place 
engine = create_engine(SQLALCHEMY_DATABASE_URL , connect_args={"check_same_thread":False})






from sqlalchemy.orm import sessionmaker , declarative_base

SessionLocal = sessionmaker(bind = engine , autoflush=False , autocommit=False)



## decalre mapping


Base = declarative_base()


## create session




