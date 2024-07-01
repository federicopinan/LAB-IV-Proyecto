from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = "mysql+mysqlconnector://root:camilo13@localhost:3306/tpi_lab4"

engine = create_engine(DATABASE_URL)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()