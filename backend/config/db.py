from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///./lavarenta.db", echo=True)

metadata = MetaData()

Base = declarative_base(metadata=metadata)


def init_db():
    Base.metadata.create_all(engine)
