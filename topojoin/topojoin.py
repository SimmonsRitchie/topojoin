"""Main module."""
from pathlib import Path
from typing import List, Union
import operator
from topojoin.helper import read_csv, read_topo


class TopoJoin:
    def __init__(
        self,
        csv_path: Union[str, Path],
        topo_path: Union[str, Path],
        *,
        csv_key: str,
        topo_key: str,
    ):
        self.csv_path = csv_path
        self.topo_path = topo_path
        self.csv_data = read_csv(csv_path)
        self.csv_keys = list(self.csv_data[0])
        self.topo_data = read_topo(topo_path)
        self.topo_keys = self.get_topo_keys()
        self.csv_key = csv_key
        self.topo_key = topo_key

    @property
    def csv_path(self) -> Path:
        return self._csv_path

    @csv_path.setter
    def csv_path(self, new_csv_path: Union[str, Path]) -> None:
        new_csv_path = Path(new_csv_path)
        if new_csv_path.exists():
            self._csv_path = new_csv_path
        else:
            raise Exception(f"File doesn't exist at path '{new_csv_path}'.")

    @property
    def topo_path(self) -> Path:
        return self._topo_path

    @topo_path.setter
    def topo_path(self, new_topo_path: Union[str, Path]) -> None:
        new_topo_path = Path(new_topo_path)
        if new_topo_path.exists():
            self._topo_path = new_topo_path
        else:
            raise Exception(f"File doesn't exist at path '{new_topo_path}'.")

    @property
    def csv_key(self) -> str:
        return self._csv_key

    @csv_key.setter
    def csv_key(self, new_csv_key: str) -> None:
        if new_csv_key in self.csv_keys:
            self._csv_key = new_csv_key
        else:
            raise Exception(
                f"Provided csv_key '{new_csv_key}' is not among CSV keys: {self.csv_keys}."
            )

    @property
    def topo_key(self) -> str:
        return self._topo_key

    @csv_key.setter
    def topo_key(self, new_topo_key: str) -> None:
        if new_topo_key in self.topo_keys:
            self._topo_key = new_topo_key
        else:
            raise Exception(
                f"Provided topo_key '{new_topo_key}' is not among TopoJson keys: {self.topo_keys}."
            )

    def get_topo_keys(self) -> List[str]:
        """
        Gets a list of properties in the first feature of topojson data
        """
        objects = self.topo_data["objects"]
        first_key = list(objects.keys())[0]
        properties = objects[first_key]["geometries"][0]["properties"]
        return list(properties)
