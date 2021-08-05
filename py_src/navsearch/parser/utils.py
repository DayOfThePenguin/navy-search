import abc

from datetime import datetime
from pathlib import Path
from typing import Dict

import pymongo

from pydantic import BaseModel, Field
from pymongo.errors import DuplicateKeyError
from tika import parser


class Document(BaseModel):
    pdf_path: Path
    raw_pdf: Dict = {}
    parse_time: datetime = Field(default_factory=datetime.utcnow)
    stored: bool = False

    def parse_pdf(self):
        self.raw_pdf = parser.from_file(self.pdf_path.as_posix())

    def to_db(self):
        if self.stored:
            raise DuplicateKeyError(
                f"{self.__repr_name__} has already been written to DB")

    @abc.abstractmethod
    def write(self):
        self.parse_pdf()
        record = {
            "file_title": self.pdf_path.stem,
            "parsed_time": self.parse_time,
            **self.raw_pdf['metadata'],
            "raw_text": self.raw_pdf['content'],
        }
        with pymongo.MongoClient() as client:
            db = client["dc"]
            db[f"{self.__repr_name__}"].insert_one(record)
            self.stored = True


def translate_pdfs_to_objs(path: Path, file_type):
    """Recursively etl pdfs from path into Mono objects of type file_type"""
    for artifact in path.iterdir():
        if artifact.suffix == "pdf":
            doc = file_type(pdf_path=path.joinpath(artifact))
            doc.write()
        elif artifact.is_dir():  # recurse through subdirectories
            translate_pdfs_to_objs(artifact, file_type)
