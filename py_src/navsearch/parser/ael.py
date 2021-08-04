from datetime import datetime
from pathlib import Path
from typing import Dict

from tika import parser
import pymongo
from pymongo.errors import DuplicateKeyError
from pydantic import BaseModel, Field


class AEL(BaseModel):
    pdf_path: Path
    raw_pdf: Dict = {}
    parse_time: datetime = Field(default_factory=datetime.utcnow)
    stored: bool = False

    def parse_pdf(self):
        self.raw_pdf = parser.from_file(self.pdf_path.as_posix())

    def write(self):
        if self.stored:
            raise DuplicateKeyError("AEL has already been written to DB")
        else:
            self.parse_pdf()
        record = {
            "file_title": self.pdf_path.stem,
            "parsed_time": self.parse_time,
            **self.raw_pdf['metadata'],
            "raw_text": self.raw_pdf['content'],
        }
        with pymongo.MongoClient() as client:
            db = client["dc"]
            db["ael"].insert_one(record)
            self.stored = True


def load_aels(library_path: Path):
    for artifact in library_path.iterdir():
        if artifact.suffix == "pdf":
            doc = AEL(pdf_path=library_path.joinpath(artifact))
            doc.write()
