import csv
import json
from pathlib import Path
from typing import Union, List, Dict, Any
from collections import OrderedDict
import copy


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


def write_topo(topo_data, output_path) -> None:
    with open(output_path, "w") as outfile:
        json.dump(topo_data, outfile)


def get_topo_features(topo_data: Dict) -> List:
    """
    Gets a list of features stored on a topojson structured dictionary.
    """
    objects = topo_data["objects"]
    first_key = list(objects.keys())[0]
    return objects[first_key]["geometries"]


def get_topo_props(topo_data: Dict) -> List[str]:
    """
    Gets a list of properties in the first feature of topojson data

    Args:
        topo_data (Dict): Dictionary of topojson data.

    Returns:
        List[str]: Properties in the first feature of topojson data
    """
    features = get_topo_features(topo_data)
    property_keys_of_first_feature = features[0]["properties"]
    return list(property_keys_of_first_feature)


def create_lookup_table(
    list_of_dicts: List[Dict[str, Any]], lookup_key
) -> Dict[str, List[Any]]:
    """ Takes a list of dictionaries and converts it into a dictionary of dictionaries indexed by a specified key"""

    payload = {}
    for dict_item in list_of_dicts:
        payload_index = dict_item[lookup_key]
        dict_item = copy.deepcopy(dict_item)
        dict_item.pop(lookup_key)
        payload[payload_index] = dict_item
    return payload
