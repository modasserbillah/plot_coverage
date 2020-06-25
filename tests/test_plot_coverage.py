#!/usr/bin/env python

"""Tests for `plot_coverage` package."""
import pandas
import pytest
from click.testing import CliRunner

from plot_coverage.plot_coverage import prepare_data
from plot_coverage import cli


@pytest.fixture
def mock_df():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    with open("tests/mock_report.html", "r") as data:
        df = pandas.read_html(data)[0]
    return df


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 2
    assert 'Error: Missing option "--plot"' in result.output
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert (
        "This package creates a visualization from the coverage report"
        in help_result.output
    )


def test_prepare_data(mock_df):
    df, depth = prepare_data(mock_df)
    assert depth == 2
    assert df.shape[1] == 9
