"""Main module."""
import os
import pandas as pd
import plotly.express as px
from urllib.error import URLError


def plot_coverage(plot):

    if plot.lower() not in ["treemap", "sunburst"]:
        print("Please provide a valid plot type with --plot=treemap / sunburst")
        return
    report_path = f"file:///{os.getcwd()}/htmlcov/index.html"

    try:
        # Assuming coverage report was generated and resides at htmlcov/index.html
        report_df = pd.read_html(report_path)[0]
    except URLError:
        print(
            "File not found! Please make sure your coverage report is in htmlcov/index.html"
        )
        return
    except ValueError:
        print("Missing data. Your coverage report has no tables! ")
        return

    df, depth = prepare_data(report_df)
    fig = create_plot(df, depth, plot)
    fig.show()
    storage_path = f"htmlcov/coverage_{plot}.html"
    fig.write_html(storage_path)
    print(f"Plot saved to {storage_path}")


def prepare_data(report_df):

    # Split the path into separate columns to feed into plotly
    path_columns = report_df["Module"].str.split("/", expand=True)
    depth = path_columns.shape[1]
    df = pd.concat([path_columns, report_df], axis=1)
    # coverage metric needs to be numeric for plotly
    df["coverage"] = df["coverage"].str.rstrip("%").astype("float")
    return df, depth


def create_plot(df, depth, plot):
    path = [col for col in range(depth)]
    if plot.lower() == "treemap":
        treemap = px.treemap(
            df[:-1],  # excludes the summary row
            path=path,
            color_continuous_scale=px.colors.diverging.RdYlGn,
            color="coverage",
        )
        return treemap

    elif plot.lower() == "sunburst":
        sunburst = px.sunburst(
            df[:-1],
            path=path,
            color_continuous_scale=px.colors.diverging.RdYlGn,
            color="coverage",
        )
        return sunburst

    print("Plot not supported. Please use either of treemap or sunburst.")