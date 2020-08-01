"""Main module."""
from pathlib import Path
from typing import List
import click

from topojoin.helper import read_csv, read_topo


class TopoJoin:
    def __init__(self, csv_path, topo_path):
        self.csv_path = csv_path
        self.topo_path = topo_path
        self.csv_data = read_csv(csv_path)
        self.topo_data = read_topo(topo_path)
        self.topo_keys = self.get_topo_keys()

    @property
    def csv_path(self):
        return self._csv_path

    @csv_path.setter
    def csv_path(self, d):
        p = Path(d)
        if not p.exists():
            raise Exception(f"csv_path must specify a file")
        if p.suffix.lower() not in [".csv"]:
            raise Exception(f"csv_path must have .csv extension")
        self._csv_path = Path(d)

    @property
    def topo_path(self):
        return self._topo_path

    @topo_path.setter
    def topo_path(self, d):
        p = Path(d)
        if not p.exists():
            raise Exception(f"topo_path must specify a file.")
        if p.suffix.lower() not in [".json", ".topojson", ".geojson"]:
            print(p.suffix)
            raise Exception(
                f"topo_path must have .json .topojson or .geojson extension"
            )
        self._topo_path = Path(d)

    def get_topo_keys(self) -> List[str]:
        """
        Gets a list of properties in the first feature of topojson data
        """
        objects = self.topo_data["objects"]
        first_key = list(objects.keys())[0]
        properties = objects[first_key]["geometries"][0]["properties"]
        return list(properties)
