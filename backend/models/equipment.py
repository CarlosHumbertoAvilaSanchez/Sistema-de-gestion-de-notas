from config.db import Base
from sqlalchemy import Column, Integer, String


class Equipment(Base):
    __tablename__ = "equipments"

    equipmentID = Column(Integer, primary_key=True, autoincrement=True)
    serialNumber = Column(String(50))
    equipmentBrand = Column(String(200))
