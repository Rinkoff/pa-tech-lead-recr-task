import base64
import pandas as pd


def file_download(df: pd.DataFrame, year:str) -> str:
    """
    Generates a downloadable CSV file from the provided DataFrame for a specific year.

    :param df: pd.DataFrame
        The DataFrame containing the data to be saved.
    :param year: str
        The year (as a string) that will be used to name the file.
    :return: str(href)
        A HTML download link (href) that allows users to download the CSV file.
    """

    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode() # str <-> bytes conversion
    href = f" <a href=\"data:file/csv;base64,{b64}\" download=\"Happiness_Rate_{year}.csv\">Download CSV File</a>"

    return href