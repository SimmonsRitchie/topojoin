#!/usr/bin/env python
"""Tests for `topojoin` package."""
# pylint: disable=redefined-outer-name

import pytest
from click.testing import CliRunner
from topojoin import cli
from topojoin.helper import read_topo, get_topo_features


def test_cli_basic(topo_path, csv_path, tmp_path):
    output_path = tmp_path / "test_joined.json"
    runner = CliRunner()
    result = runner.invoke(
        cli.main,
        ["-tk", "GEOID", "-ck", "fips", "-o", output_path, topo_path, csv_path,],
    )
    assert result.exit_code == 0
    file_list = tmp_path.glob("**/*")
    file_list = [x for x in file_list if x.is_file()]
    assert len(file_list) == 1


def test_cli_csv_props_option(topo_path, csv_path, tmp_path):
    output_path = tmp_path / "test_joined.json"
    runner = CliRunner()
    result = runner.invoke(
        cli.main,
        ["-tk", "GEOID", "-ck", "fips", "-cp", "population","-o", output_path, topo_path, csv_path],
    )
    topo_data = read_topo(output_path)
    first_feature = get_topo_features(topo_data)[0]
    assert not first_feature["properties"].get("name")


def test_cli_fails_when_invalid_csv_prop_provided(topo_path, csv_path, tmp_path):
    output_path = tmp_path / "test_joined.json"
    runner = CliRunner()
    result = runner.invoke(
        cli.main,
        ["-tk", "GEOID", "-ck", "fips", "-cp", "duck","-o", output_path, topo_path, csv_path],
    )
    # Exit code 1 indicates failure
    assert result.exit_code == 1


def test_cli_invalid_topo_path(csv_path):
    """ Test exception raised if topojson file doesn't exist"""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["./fixtures/pa-county.txt", csv_path])
    print(result.exc_info)
    assert result.exit_code != 0


def test_cli_invalid_csv_path(topo_path):
    runner = CliRunner()
    result = runner.invoke(cli.main, [topo_path, "./fixtures/foobar.csv"])
    print(result.exc_info)
    assert result.exit_code != 0


def test_cli_help():
    """Test help output from CLI."""
    runner = CliRunner()
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "Show this message and exit." in help_result.output


def test_cli_version():
    """ Test version """
    runner = CliRunner()
    result = runner.invoke(cli.main, ["--version"])
    assert "version" in result.output


def test_cli_quiet(topo_path, csv_path):
    """ Test no console output """
    runner = CliRunner()
    result = runner.invoke(cli.main, ["--quiet", topo_path, csv_path])
    print(result.output)
    assert result.output == ""
