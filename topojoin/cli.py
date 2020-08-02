"""Console script for topojoin."""
import os
import sys
from pathlib import Path
import click
from topojoin.topojoin import TopoJoin


@click.command()
@click.argument("csv_path", type=click.Path())
@click.argument("topo_path", type=click.Path())
@click.option(
    "csv_key",
    "--csvkey",
    "-ck",
    default="fips",
    type=click.STRING,
    help="Key in CSV file that will be used to join with topojson file",
    show_default=True,
)
@click.option(
    "topo_key",
    "--topokey",
    "-tk",
    default="fips",
    type=click.STRING,
    help="Key in CSV file that will be used to join with CSV file",
    show_default=True,
)
@click.option(
    "output_path",
    "--output_path",
    "-o",
    default=Path(os.getcwd()) / "joined.json",
    type=click.Path(),
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
def main(quiet: bool, csv_path, topo_path, output_path, **kwargs) -> None:
    """
    CLI for topojoin.

    Args:
        quiet (bool): Disables stdout during program run.
        csv_path (str):
        topo_path (str):
        kwargs (dict): Keyword arguments that will be passed to TopoJson.

    Returns:
        None
    """
    if quiet:
        f = open(os.devnull, "w")
        sys.stdout = f
    topojoin_obj = TopoJoin(csv_path, topo_path, **kwargs)
    click.echo(
        f"Joining {topojoin_obj.csv_filename} to {topojoin_obj.topo_filename})..."
    )
    click.echo(
        f"CSV key '{topojoin_obj.csv_key}' will be joined with topojson key '{topojoin_obj.topo_key}'"
    )
    topojoin_obj.join(output_path)
    click.echo(f"File saved as: {output_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
