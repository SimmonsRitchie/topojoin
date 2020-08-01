"""Console script for topojoin."""
import os
import sys
import click

from topojoin.topojoin import TopoJoin


@click.command()
@click.argument("csv_path", type=click.STRING)
@click.argument("topo_path", type=click.STRING)
@click.option(
    "csv_key",
    "--csvkey",
    "-c",
    default="fips",
    type=click.STRING,
    help="Key in CSV file that will be used to join " "with topojson file",
    show_default=True,
)
@click.option(
    "topo_key",
    "--topokey",
    "-t",
    default="fips",
    type=click.STRING,
    help="Key in CSV file that will be used to " "join with CSV file",
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
def main(quiet, **kwargs):
    """Console script for topojoin."""
    if quiet:
        f = open(os.devnull, "w")
        sys.stdout = f

    click.echo("Starting topojoin...")
    click.echo(kwargs)
    topojoin_obj = TopoJoin(**kwargs)
    # click.echo(topojoin_obj.csv_data)
    # click.echo(topojoin_obj.topo_data)
    # click.echo(topojoin_obj.topo_keys)
    # click.echo(topojoin_obj.csv_keys)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
