import csv
import json
from pathlib import Path
from typing import Union, List, Dict
from collections import OrderedDict


def read_csv(csv_path: Union[Path, str]) -> "List[OrderedDict[str, str]]":
    """ Reads a CSV file.

    Args:
        csv_path (Union[Path, str]): Path to CSV file

    Returns:
        List[OrderedDict[str, str]]: CSV file contents. Each row is an OrderedDict.

    """
    with open(csv_path, "r") as fin:
        reader = csv.DictReader(fin)
        csv_data = [x for x in reader]
    return csv_data


def read_topo(topo_path):
    """ Reads a topojson file.

    Args:
        topo_path (Union[Path, str]): Path to CSV file

    Returns:

    """
    data = open(topo_path)
    return json.load(data)


def get_topo_keys(topo_data: Dict) -> List[str]:
    """
    Gets a list of properties in the first feature of topojson data

    Args:
        topo_data (Dict): Dictionary of topojson data.

    Returns:
        List[str]: Properties in the first feature of topojson data
    """
    objects = topo_data["objects"]
    first_key = list(objects.keys())[0]
    properties = objects[first_key]["geometries"][0]["properties"]
    return list(properties)
