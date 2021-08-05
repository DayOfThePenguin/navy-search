from datetime import datetime
from pathlib import Path
from typing import Dict


from pydantic import BaseModel, Field

from .utils import translate_pdfs_to_objs


class AEL(BaseModel):


def load_aels(ael_library_path: Path):
    translate_pdfs_to_objs(ael_library_path, AEL)
    for artifact in ael_library_path.iterdir():
        if artifact.suffix == "pdf":
            doc = AEL(pdf_path=ael_library_path.joinpath(artifact))
            doc.write()
        elif artifact.is_dir():
