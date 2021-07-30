"""Tests for navsearch.scraper.pdf"""
import pytest
from navsearch.scraper import pdf


class TestPdfScraper:
    """Tests for navsearch.scraper.pdf"""

    def test_is_valid_url(self):
        """Tests for pdf.is_valid_url"""
        valid_cases = ["http://example.com",
                       "https://example.com",
                       "https://example.com/test",
                       "https://example.com/test.html",
                       "https://example.com/test.pdf",
                       "https://example.org/test.html",
                       "https://example.net/test.html",
                       " http://example.com",
                       ]
        invalid_cases = ["htxtp://example.com",
                         "javascript://example.com",
                         "ftp://example.com",
                         "ftps://example.com",
                         "http: //example.com",
                         "http:/example.com",
                         "http://example"]
        for case in valid_cases:
            assert pdf.is_valid_url(case) is True
        for case in invalid_cases:
            assert pdf.is_valid_url(case) is False
