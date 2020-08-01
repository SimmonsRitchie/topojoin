import pytest
from pathlib import Path


root = Path(__file__).parent.resolve()


@pytest.fixture(scope="session")
def csv_path():
    return str(root / "fixtures/pa-county-pop.csv")


@pytest.fixture(scope="session")
def topo_path():
    return str(root / "fixtures/pa-county.json")
