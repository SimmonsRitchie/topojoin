import json

import pytest

from topojoin.helper import read_csv, read_topo


def test_read_csv(csv_path):
    csv_data = read_csv(csv_path)
    assert csv_data[1]["name"] == "Allegheny"


def test_read_topo(topo_path):
    topo_data = read_topo(topo_path)
    assert topo_data["type"] == "Topology"
