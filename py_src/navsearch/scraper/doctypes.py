from datetime import datetime
from pathlib import Path
from typing import List, Optional
from enum import Enum

from pydantic import BaseModel, Field, HttpUrl, validator


class OPNAVEchelon(str, Enum):
    OPNAV: "OPNAV"
    SECNAV: "SECNAV"


class OPNAVNotice(BaseModel):
    """From https://www.secnav.navy.mil/doni/notices.aspx"""
    name: str
    subject: str
    echelon: OPNAVEchelon
    name = 'John Doe'
    pdf_url: Path
    signup_ts: Optional[datetime] = None
    friends: List[int] = []

    @validator('pdf_url')
    def check_url_scheme(cls, v):
        assert v.scheme == "https", "URL must be https"
        return v
