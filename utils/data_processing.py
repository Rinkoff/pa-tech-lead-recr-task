import streamlit as st
import pandas as pd


@st.cache_data
def load_data(year: str) -> pd.DataFrame|None:
    """
    Loads a DataFrame from a csv file, select only required columns, rename them if necessary, and adds/validate missing
    data when needed

    :param year:str
    :return:pd.DataFrame|None
    """

    column_params = {
        "Country":"Country",
        "Happiness Rank":"Happiness Rank",
        "Happiness Score": "Happiness Score",
        "Happiness.Rank": "Happiness Rank",
        "Happiness.Score": "Happiness Score",
        "Country or region": "Country",
        "Score": "Happiness Score"
    }

    try:
        df = pd.read_csv(f"data/{year}.csv")

        needed_columns = []

        for col in column_params.keys():
            if col in df.columns:
                if column_params[col] != col:
                    df = df.rename(columns={col: column_params[col]})
                    col = column_params[col]

                needed_columns.append(col)

        df = df[needed_columns]

        if "Happiness Rank" not in df.columns:
            df.insert(1, "Happiness Rank", range(1, len(df)+1))

        if not validate_rank_and_score(df):
            st.error("The data is invalid! Please contact the dev team. Email: Rinkoff99@gmail.com")

        return df

    except Exception as err:
        st.error("⚠️ Page cannot loaded.")

        col1, col2, col3 = st.columns([1,2,1])

        with col2:
            st.image("https://media.giphy.com/media/26ufdipQqU2lhNA4g/giphy.gif",
                     caption = "Oops! Something went wrong!",
                     use_container_width=True)



def validate_rank_and_score(df: pd.DataFrame, score_val = "Happiness Score", rank_val = "Happiness Rank") -> bool:
    """
    Validate the rank and score to check for issues in the initial data.

    :param df: pd.DataFrame
    :param score_val:str
    :param rank_val:str
    :return: bool
    """

    is_valid = True

    for i in range(len(df)):
        for j in range(len(df)):
            if i == j:
                continue

            score_i = df.iloc[i][score_val]
            score_j = df.iloc[j][score_val]

            rank_i = df.iloc[i][rank_val]
            rank_j = df.iloc[j][rank_val]

            if score_i > score_j:
                if rank_i >= rank_j:
                    is_valid = False

            elif score_i < score_j:
                if rank_i <= rank_j:
                    is_valid = False


    return is_valid



def get_merged_df(first_year: int, last_year: int) -> pd.DataFrame:
    all_data = []

    for year in range(first_year, last_year+1):
        df = load_data(str(year))
        df.insert(0, "Year", year)

        all_data.append(df)

    merged_df = pd.concat(all_data, ignore_index=True)

    return merged_df

