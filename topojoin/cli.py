"""Console script for topojoin."""
import sys
import click

from topojoin.topojoin import TopoJoin


@click.command()
@click.argument("csv_path", type=click.STRING)
@click.argument("topo_path", type=click.STRING)
@click.option("--csvkey", "-ck", default="fips", type=click.STRING)
@click.option("--topokey", "-tk", default="fips", type=click.STRING)
def main(csv_path: str, topo_path: str, csvkey: str, topokey: str):
    """Console script for topojoin."""
    click.echo("Starting topojoin...")
    click.echo(csv_path)
    topojoin_obj = TopoJoin(csv_path, topo_path)
    click.echo(topojoin_obj.csv_data)
    click.echo(topojoin_obj.topo_data)
    click.echo(topojoin_obj.topo_keys)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
