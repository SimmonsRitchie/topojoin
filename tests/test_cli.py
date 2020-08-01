#!/usr/bin/env python
"""Tests for `topojoin` package."""
# pylint: disable=redefined-outer-name

import pytest
from click.testing import CliRunner
from pathlib import Path
from topojoin import cli


def test_cli_basic(csv_path, topo_path):
    runner = CliRunner()
    result = runner.invoke(cli.main, ["-tk", "GEOID", csv_path, topo_path])
    print(result.output)
    assert result.exit_code == 0


def test_cli_invalid_topo_path(csv_path):
    """ Test exception raised if topojson file doesn't exist"""
    runner = CliRunner()
    result = runner.invoke(cli.main, [csv_path, "./fixtures/pa-county.txt"])
    print(result.exc_info)
    assert result.exit_code != 0


def test_cli_invalid_csv_path(topo_path):
    runner = CliRunner()
    result = runner.invoke(cli.main, ["./fixtures/foobar.csv", topo_path])
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


def test_cli_quiet(csv_path, topo_path):
    """ Test no console output """
    runner = CliRunner()
    result = runner.invoke(cli.main, ["--quiet", csv_path, topo_path])
    print(result.output)
    assert result.output == ""
