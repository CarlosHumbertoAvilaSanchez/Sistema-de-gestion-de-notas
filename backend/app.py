from config.db import init_db
from fastapi import FastAPI
from routes.equipment import equipment_router

app = FastAPI()
init_db()
app.include_router(equipment_router, prefix="/equipments", tags=["equipment"])


@app.get("/")
def read_root():
    return {"Hello": "World"}
