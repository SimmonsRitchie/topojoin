"""Console script for topojoin."""
import os
import sys
from pathlib import Path
import click
from topojoin.topojoin import TopoJoin
from typing import Union, Dict, Any


@click.command()
@click.argument("topo_path", type=click.Path(exists=True))
@click.argument("csv_path", type=click.Path(exists=True))
@click.option(
    "topo_key",
    "--topokey",
    "-tk",
    default="id",
    type=click.STRING,
    help="Key in CSV file that will be used to join with CSV file",
    show_default=True,
)
@click.option(
    "csv_key",
    "--csvkey",
    "-ck",
    default="id",
    type=click.STRING,
    help="Key in CSV file that will be used to join with topojson file",
    show_default=True,
)
@click.option(
    "csv_props",
    "--csv_props",
    "-cp",
    type=click.STRING,
    help="Comma separated list of fields in CSV file to merge to each topojson feature "
         "(eg: name,population,net_income). Defaults to including all fields in CSV file.",
)
@click.option(
    "output_path",
    "--output_path",
    "-o",
    default=Path(os.getcwd()) / "joined.json",
    type=click.Path(resolve_path=True),
    help="Output path of joined topojson file. Defaults to current working directory.",
)
@click.option(
    "quiet",
    "--quiet",
    "-q",
    is_flag=True,
    default=False,
    help="Disables stdout during program run",
)
@click.version_option()
def main(
    quiet: bool,
    csv_path: Union[str, Path],
    topo_path: Union[str, Path],
    csv_props: str,
    output_path: Union[str, Path],
    **kwargs,
) -> Dict[str, Any]:
    """
    A CLI utility that joins CSV data to a topojson file.

    Returns:
        Dict[str, Any]: topojson data merged with CSV values.
    """
    if quiet:
        f = open(os.devnull, "w")
        sys.stdout = f
    tj = TopoJoin(topo_path, csv_path, **kwargs)
    click.echo(
        f"Joining {tj.csv_filename} to {tj.topo_filename})..."
    )
    click.echo(
        f"CSV key '{tj.csv_key}' will be joined with topojson key '{tj.topo_key}'"
    )
    clean_output_path = Path(output_path)
    if csv_props:
        csv_props = [x.strip() for x in csv_props.split(",")]
        if not set(csv_props).issubset(set(tj.all_csv_props)):
            click.echo(f"Error: One or more fields in csv_props is not among available CSV properties: "
                       f"{', '.join(tj.all_csv_props)}. Please enter valid fields.")
            exit(code=1)
    topo_data = tj.join(clean_output_path, csv_props)
    click.echo(f"Joined data saved to: {clean_output_path}")

    return topo_data


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
