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
    "output_path",
    "--output_path",
    "-o",
    # callback=lambda ctx, param, value: Path(os.getcwd()) / value,
    default=Path(os.getcwd()) / "joined.json",
    type=click.Path(resolve_path=True),
    help="Key in CSV file that will be used to join with CSV file",
    show_default=True,
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
    topojoin_obj = TopoJoin(topo_path, csv_path, **kwargs)
    click.echo(
        f"Joining {topojoin_obj.csv_filename} to {topojoin_obj.topo_filename})..."
    )
    click.echo(
        f"CSV key '{topojoin_obj.csv_key}' will be joined with topojson key '{topojoin_obj.topo_key}'"
    )
    output_path = Path(output_path)
    topo_data = topojoin_obj.join(output_path)
    click.echo(f"Joined data saved to: {output_path}")

    return topo_data


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
