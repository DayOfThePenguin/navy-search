"""Tests for navsearch.scraper.pdf"""
import pytest

from navsearch.scraper import pdf
from pydantic import ValidationError
from pymongo.errors import DuplicateKeyError


class TestPdfScraper:
    """Tests for navsearch.scraper.pdf"""

    def test_url(self):
        """Tests for pdf.URL class"""
        valid_cases = [
            "https://example.mil",
            "https://example.navy.mil",
            "https://example.army.mil",
            "https://example.mil/test",
            "https://example.mil/test.html",
            "https://example.mil/test.pdf",
            "https://example.mil/test.html",
            "https://example.mil/test.html",
        ]
        invalid_cases = ["http://example.mil",
                         " http://example.mil",
                         "htxtp://example.mil",
                         "javascript://example.mil",
                         "ftp://example.mil",
                         "ftps://example.mil",
                         "http: //example.mil",
                         "http:/example.mil",
                         "http://example",
                         "http://.mil",
                         "http://*.mil",
                         ]
        for case in valid_cases:
            assert pdf.Url(url=case)
        for case in invalid_cases:
            with pytest.raises(ValidationError):
                pdf.Url(url=case)
