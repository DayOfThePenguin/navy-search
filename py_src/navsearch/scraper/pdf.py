from pydantic import BaseModel, HttpUrl, validator
import re
import sys

from pathlib import Path
from typing import List
from urllib.parse import urljoin

import requests

from bs4 import BeautifulSoup

PDF_URL_ROOT = "https://www.secnav.navy.mil"


class Url(BaseModel):
    # pylint: disable=no-self-argument,no-self-use,invalid-name
    url: HttpUrl

    @validator("url")
    def check_url_props(cls, v):
        assert v.scheme == "https", "scheme must be https"
        assert v.tld == "mil", "top-level domain must be .mil"
        return v


# def is_valid_url(url: str) -> bool:
#     url_regex = ("((http|https)://)(www.)?" +
#                  "[a-zA-Z0-9@:%._\\+~#?&//=]" +
#                  "{2,256}\\.[a-z]" +
#                  "{2,6}\\b([-a-zA-Z0-9@:%" +
#                  "._\\+~#?&//=]*)")
#     if (url is None):  # return False if url is empty
#         return False

#     if(re.search(url_regex, url)):
#         return True
#     else:
#         return False


def pdf_url_stubs_from_html(html_path: Path) -> List[List[str]]:
    data = []
    soup = BeautifulSoup(html_path, "html.parser")
    table = soup.find("table", {"id": "onetidDoclibViewTbl0"})
    table_body = table.find('tbody')

    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        pdf_url_stub = row.select("a[href$='.pdf']")[0]["href"]
        cols.insert(0, pdf_url_stub)
        # Get rid of empty values
        data.append([ele for ele in cols if ele])

    print(data[:5])


def save_pdfs(data_path: Path, pdf_stub_list: List[str]):
    pass
