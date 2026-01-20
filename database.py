from json import load
from models import VerseData

class Database:
  def __init__(self) -> None:
    self.data: dict[str, VerseData] = {}

    with open('assets/verses.json', 'r', encoding='utf-8') as f:
      verses = load(f)
      for verse in verses:
        verse_data = VerseData(**verse)
        self.data[verse_data.verseId] = verse_data

  def get_verses(self) -> list[VerseData]:
    return list(self.data.values())
  
  def get_verse(self, verse_id: str) -> VerseData | None:
    return self.data.get(verse_id)

