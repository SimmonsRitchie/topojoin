#!/usr/bin/env python
"""Tests for `topojoin` package."""
# pylint: disable=redefined-outer-name

import pytest
from click.testing import CliRunner
from pathlib import Path
from topojoin import cli

root = Path(__file__).parent.resolve()


@pytest.fixture
def csv_path():
    return str(root / "fixtures/pa-county-pop.csv")


@pytest.fixture
def topo_path():
    return str(root / "fixtures/pa-county.json")


def test_cli(csv_path, topo_path):
    runner = CliRunner()
    result = runner.invoke(cli.main, [csv_path, topo_path])
    print(result.exc_info)
    print(result.exception)
    assert result.exit_code == 0


def test_cli_help():
    """Test the CLI."""
    runner = CliRunner()
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "--help  Show this message and exit." in help_result.output
