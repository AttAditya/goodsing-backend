from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from database import Database

app = FastAPI()
db = Database()

origins = [
  "http://localhost:5173",
  "https://goodsing.vercel.app",
  "https://goodsing.vercel.app/",
  "https://goodsing.vercel.app/*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def index():
  return "Hello, GoodSing!"

@app.get("/api/v1/verses")
async def get_verses():
  return db.get_verses()

@app.get("/api/v1/verse/{verse_id}")
async def get_verse(verse_id: str):
  return db.get_verse(verse_id)

@app.get("/api/v1/verse/{verse_id}/audio")
async def get_verse_audio(verse_id: str):
  return FileResponse(
    f"assets/songs/song_{verse_id}.mp3",
    media_type="audio/mpeg",
    filename=f"song_{verse_id}.mp3"
  )

