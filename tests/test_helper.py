import pytest

from topojoin.helper import read_csv


def test_read_csv(csv_path):
    csv_data = read_csv(csv_path)
    assert csv_data[1]["name"] == "Allegheny"
