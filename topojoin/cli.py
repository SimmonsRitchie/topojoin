"""Console script for topojoin."""
import sys
import click

from topojoin.topojoin import Topojoin


@click.command()
@click.argument("csv_path", type=click.STRING)
@click.argument("topo_path", type=click.STRING)
@click.option("--csvkey", "-ck", default="fips", type=click.STRING)
@click.option("--topokey", "-tk", default="fips", type=click.STRING)
def main(csv_path: str, topo_path: str, csvkey: str, topokey: str):
    """Console script for topojoin."""
    click.echo("Starting topojoin...")
    click.echo(csv_path)
    topojoin_obj = Topojoin(csv_path, topo_path)
    topojoin_obj.hello()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
