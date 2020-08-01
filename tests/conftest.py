import pytest
from pathlib import Path


@pytest.fixture(scope="session")
def csv_path() -> Path:
    """ Returns path to CSV fixture """
    return Path("./fixtures/pa-county-pop.csv")
