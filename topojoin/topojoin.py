"""Main module."""
from pathlib import Path

import click


class Topojoin:
    def __init__(self, csv_path, topo_path):
        self.csv_path = csv_path
        self.topo_path = topo_path

    @property
    def csv_path(self):
        return self._csv_path

    @csv_path.setter
    def csv_path(self, d):
        p = Path(d)
        if not p.exists():
            raise Exception("csv_path must specify a valid file")
        if p.suffix.lower() not in [".csv"]:
            raise Exception(
                f"csv_path has extension {p.suffix}. csv_path must be a CSV file"
            )
        self._csv_path = Path(d)

    @property
    def topo_path(self):
        return self._topo_path

    @topo_path.setter
    def topo_path(self, d):
        p = Path(d)
        if not p.exists():
            raise Exception("topo_path must specify a valid file")
        if p.suffix.lower() not in [".json", ".topojson", ".geojson"]:
            print(p.suffix)
            raise Exception(
                f"topo_path has extension {p.suffix}. topo_path must be a CSV file"
            )
        self._topo_path = Path(d)

    def hello(self):
        click.echo(f"csv_path is {self.csv_path}")
        click.echo(f"topo_path is {self.topo_path}")


topo = Topojoin(
    "../tests/fixtures/pa-county-pop.csv", "../tests/fixtures/pa-county.json"
)
# topo = Topojoin("../pa-county.json","../pa-county.json")
topo.hello()
