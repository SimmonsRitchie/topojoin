"""Main module."""
import copy
from pathlib import Path
from typing import List, Union, Dict, Any
from topojoin.helper import (
    read_csv,
    read_topo,
    get_topo_props,
    create_lookup_table,
    write_topo,
    get_topo_features,
)
import click


class TopoJoin:
    def __init__(
        self,
        topo_path: Union[str, Path],
        csv_path: Union[str, Path],
        *,
        topo_key: str = "id",
        csv_key: str = "id",
    ):
        """
            Args:
                topo_path (Union[str, Path]): Path to topojson file
                csv_path (Union[str, Path]): Path to CSV file
                csv_key (str, optional): Field on CSV field that will be used for join. Defaults to 'id'.
                topo_key (str, optional):  Field on topojson file that will be used for join. Defaults to 'id'.
        """
        self.topo_path = topo_path
        self.topo_data = read_topo(topo_path)
        self.all_topo_props = get_topo_props(self.topo_data)
        self.topo_key = topo_key
        self.csv_path = csv_path
        self.csv_data = read_csv(csv_path)
        self.all_csv_props = list(self.csv_data[0])
        self.csv_key = csv_key

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
    def topo_filename(self) -> str:
        return self.topo_path.name

    @property
    def topo_key(self) -> str:
        return self._topo_key

    @topo_key.setter
    def topo_key(self, new_topo_key: str) -> None:
        if new_topo_key in self.all_topo_props:
            self._topo_key = new_topo_key
        else:
            raise Exception(
                f"Provided topo_key '{new_topo_key}' is not among TopoJson keys: {self.all_topo_props}."
            )

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
    def csv_filename(self) -> str:
        return self.csv_path.name

    @property
    def csv_key(self) -> str:
        return self._csv_key

    @csv_key.setter
    def csv_key(self, new_csv_key: str) -> None:
        if new_csv_key in self.all_csv_props:
            self._csv_key = new_csv_key
        else:
            raise Exception(
                f"Provided csv_key '{new_csv_key}' is not among CSV keys: {self.all_csv_props}."
            )

    def join(self, output_path: Union[str, Path] = None, csv_props: List[str] = None) -> Dict[str, Any]:
        """
        Returns a topojson-structured Dict with CSV data appended onto existing topojson properties based on specified
        keys.

        Args:
            output_path( Union[str, Path]): Writes joined topojson data to specified path. Defaults to None. No file
                will be saved.
            csv_props (List[str]): Determines which columns from CSV to add to each topojson property. If
                not specified, defaults to including all CSV props.

        Returns:
            A dict representing topojson structured data. Fields from CSV are added to existing topojson properties.

        """
        if csv_props:
            assert set(csv_props).issubset(set(self.all_csv_props)), "One or more keys provided " \
                "in selected_csv_keys are not among columns in CSV file"
        else:
            csv_props = self.all_csv_props
        joined_topo_data = copy.deepcopy(self.topo_data)
        csv_lookup_table = create_lookup_table(self.csv_data, self.csv_key)
        features = get_topo_features(joined_topo_data)
        with click.progressbar(features) as bar:
            for feature in bar:
                topo_props = feature["properties"]
                topo_join_val = topo_props[self.topo_key]
                csv_row = csv_lookup_table.get(topo_join_val)
                if csv_row:
                    csv_row = {k: v for k, v in csv_row.items() if k in csv_props}  # filter keys
                    new_props = {**topo_props, **csv_row}
                else:
                    clean_csv_keys = copy.deepcopy(self.all_csv_props)
                    clean_csv_keys.remove(self.csv_key)
                    null_fields = {x: None for x in clean_csv_keys}
                    new_props = {**topo_props, **null_fields}
                feature["properties"] = new_props
        if output_path:
            write_topo(joined_topo_data, output_path)
        return joined_topo_data
