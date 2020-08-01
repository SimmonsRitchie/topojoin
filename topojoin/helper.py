import csv
from pathlib import Path
from typing import Union, List
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
