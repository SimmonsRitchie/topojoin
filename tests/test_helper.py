import json

import pytest

from topojoin.helper import read_csv, read_topo


def test_read_csv(csv_path):
    csv_data = read_csv(csv_path)
    assert csv_data[1]["name"] == "Allegheny"


def test_read_topo(topo_path):
    topo_data = read_topo(topo_path)
    assert topo_data["type"] == "Topology"

    objects = topo_data["objects"]
    first_key = list(objects.keys())[0]
    properties = objects[first_key]["geometries"][0]["properties"]
    keys = list(properties)
    print(keys)
    # json_formatted_str = json.dumps(properties, indent=2)
    # print(json_formatted_str)
