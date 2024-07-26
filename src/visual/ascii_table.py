import pandas as pd
from tabulate import tabulate
from io import StringIO

from visual.ansi_colors import COLOR


def csv_string_to_ascii_table(csv_string, header_color="reset", number_color="reset", string_color="reset"):
    # Convert the CSV string to a pandas DataFrame
    csv_data = StringIO(csv_string)
    df = pd.read_csv(csv_data)

    # Apply colors to the headers
    colored_headers = [f'{COLOR[header_color]}{header}{COLOR["reset"]}' for header in df.columns]

    # Function to color the cells
    def color_cell(cell):
        if isinstance(cell, (int, float)):
            return f'{COLOR[number_color]}{cell}{COLOR["reset"]}'  # Color for numbers
        else:
            return f'{COLOR[string_color]}{cell}{COLOR["reset"]}'  # Color for text

    # Apply colors to all cells in the DataFrame
    df = df.map(color_cell)

    # Generate the ASCII table using tabulate
    table = tabulate(df, headers=colored_headers, tablefmt='grid')

    return table
