from fastapi import FastAPI, HTTPException, Response, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from config.settings import settings, Base, engine
from apps.users.routers import app as user_app


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

origin_cors = ["*"]

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origin_cors,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.on_event('startup')
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(
    user_app
)

@app.get('/')
def home():
    return {"message": "ok", "db_name": settings.db_url}