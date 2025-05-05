import base64
import pandas as pd


def file_download(df: pd.DataFrame, year:str) -> str:
    """
    Allows the users to download the current df.

    :param df: pd.DataFrame
    :param year: str
    :return: str(href)
    """

    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode() # str <-> bytes conversion
    href = f" <a href=\"data:file/csv;base64,{b64}\" download=\"Happiness_Rate_{year}.csv\">Download CSV File</a>"

    return href