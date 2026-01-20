from pydantic import BaseModel

class Creator(BaseModel):
  name: str
  link: str

class Lyric(BaseModel):
  lyric: str
  wait: int
  timestamp: int

class Audios(BaseModel):
  original: str
  instrumental: str

class VerseData(BaseModel):
  verseId: str
  verseName: str
  songName: str
  creators: list[Creator]
  lyrics: list[Lyric]
  audios: Audios

