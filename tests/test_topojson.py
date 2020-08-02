import pytest

from topojoin.helper import get_topo_features
from topojoin.topojoin import TopoJoin
from pathlib import Path


def test_topojson_init(csv_path, topo_path):
    """ Test that TopoJoin instance is initialized and attribs are properly set """
    topojoin_obj = TopoJoin(csv_path, topo_path, csv_key="fips", topo_key="GEOID")
    assert isinstance(topojoin_obj.csv_path, Path)
    assert isinstance(topojoin_obj.topo_path, Path)
    assert topojoin_obj.csv_key == "fips"
    assert topojoin_obj.topo_key == "GEOID"
    print(topojoin_obj.topo_key)


def test_error_when_csv_key_not_present(csv_path, topo_path):
    """ Test failure when topo_key is not among keys in CSV file """
    with pytest.raises(Exception):
        TopoJoin(csv_path, topo_path, csv_key="ducks", topo_key="GEOID")


def test_error_when_csv_key_wrong_case(csv_path, topo_path):
    """ Test failure when case doesn't match  """
    with pytest.raises(Exception):
        TopoJoin(csv_path, topo_path, csv_key="FIPS", topo_key="GEOID")


def test_error_when_topo_key_not_present(csv_path, topo_path):
    """ Test failure when topo_key is not among keys in topojson file """

    with pytest.raises(Exception):
        TopoJoin(csv_path, topo_path, csv_key="fips", topo_key="ducks")


def test_error_when_topo_key_changed_to_invalid(csv_path, topo_path):
    with pytest.raises(Exception):
        topojoin_obj = TopoJoin(csv_path, topo_path, csv_key="fips", topo_key="GEOID")
        topojoin_obj.csv_key = "ducks"


def test_file_created_after_join(csv_path, topo_path, tmp_path):
    output_path = tmp_path / "test_joined.json"
    topojoin_obj = TopoJoin(csv_path, topo_path, csv_key="fips", topo_key="GEOID")
    topojoin_obj.join(output_path)
    file_list = tmp_path.glob("**/*")
    file_list = [x for x in file_list if x.is_file()]
    assert len(file_list) == 1


def test_null_fields_after_join(csv_path_non_matching, topo_path, tmp_path):
    """ Test that Allegheny county feature in joined data has several null properties because there was no Allegheny
    County row in provided CSV data."""
    topojoin_obj = TopoJoin(
        csv_path_non_matching, topo_path, csv_key="fips", topo_key="GEOID",
    )
    result = topojoin_obj.join()
    features = get_topo_features(result)
    allegheny_county_props = [
        feature["properties"]
        for feature in features
        if feature["properties"]["NAME"].lower() == "allegheny"
    ][0]
    assert allegheny_county_props["population"] is None
