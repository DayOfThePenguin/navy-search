import json

from bson import json_util
from datetime import datetime
from pathlib import Path
import bson

import pytest

from navsearch.parser import ael
from pydantic import ValidationError


class TestAel():
    """Tests for navsearch.parser"""

    def test_ael_model(self):
        # Verify setup
        data_folder = Path("tests/data/")
        assert data_folder.is_dir()
        test_file = data_folder.joinpath("S3030.1.pdf")
        assert test_file.is_file()
        document = ael.AEL(pdf_path=test_file)

        # Verify initial state
        assert document.pdf_path == test_file
        assert document.raw_pdf == {}
        assert document.parse_time.date() == datetime.utcnow().date()
        assert document.parse_time.hour == datetime.utcnow().hour
        assert document.stored is False

        # Verify state after parse
        document.parse_pdf()
        with open(data_folder.joinpath("pdf_test.json"), "r") as file:
            ground_truth_record = json.load(
                file, object_hook=json_util.object_hook)
        test_record = {
            "file_title": document.pdf_path.stem,
            "parsed_time": ground_truth_record["parsed_time"],
            **document.raw_pdf["metadata"],
            "raw_text": document.raw_pdf["content"],
            "X-TIKA:parse_time_millis": ground_truth_record["X-TIKA:parse_time_millis"]
        }
        assert test_record == ground_truth_record
        assert document.stored is False
