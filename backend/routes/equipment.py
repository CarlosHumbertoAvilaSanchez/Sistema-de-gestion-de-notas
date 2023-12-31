from config.db import engine
from fastapi import APIRouter
from models.equipment import Equipment
from sqlalchemy.orm import sessionmaker

equipment_router = APIRouter()
session = sessionmaker(bind=engine)()


@equipment_router.get("/")
def get_equipments():
    res = session.query(Equipment).all()

    return res
