"""Console script for plot_coverage."""
import sys
import click
from .plot_coverage import plot_coverage


@click.command()
@click.option("--plot", required=True, help="the type of plot you want (e.g, treemap, sunburst")
def main(plot):
    """This package creates a visualization from the coverage report.

    Usage:

        plot_coverage --plot=treemap/sunburst
    """
    plot_coverage(plot)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
