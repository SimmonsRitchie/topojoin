import pytest
from pathlib import Path


root = Path(__file__).parent.resolve()


@pytest.fixture(scope="session")
def csv_path() -> str:
    """
    Returns a path to a CSV file. The file has a column called 'fips' representing unique county IDs. It joins
    with a column called 'GEOID' in the topojson file at topo_path.
    """
    return str(root / "fixtures/pa-county-pop.csv")


@pytest.fixture(scope="session")
def csv_path_non_matching():
    """
    Returns a path to a CSV file. The file has a column called 'fips' representing unique county IDs. It joins
    with a column called 'GEOID' in the topojson file at topo_path. However, this file is missing rows so it will not
    match cleanly with the topojson.
    """
    return str(root / "fixtures/pa-county-pop__non-matching-rows.csv")


@pytest.fixture(scope="session")
def topo_path():
    return str(root / "fixtures/pa-county.json")
