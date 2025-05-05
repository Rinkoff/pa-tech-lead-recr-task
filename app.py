from utils.data_processing import load_data, get_merged_df
from utils.file_helpers import file_download
import streamlit as st
import plotly.express as px



def main():
    st.sidebar.header("Filtration")

    selected_year = st.sidebar.selectbox("Year", ["2015", "2016", "2017", "2018", "2019"],
                                         help="Select the year from which you want to view the data.")
    df = load_data(selected_year)

    unique_countries = df["Country"].dropna().unique()

    selected_country = st.sidebar.selectbox("Country", options=["All"] + list(unique_countries),
                                            help="Select the country for which you want to view the data.")

    col1, col2, col3 = st.sidebar.columns([1, 1, 1])

    with col1:
        st.header("Sorting...")

    with col2:
        asc_sort = st.button("Rank Sort ↑", help="Sort by ascending Happiness Rank.")

    with col3:
        desc_sort = st.button("Rank Sort ↓", help="Sort by descending Happiness Rank.")

    if asc_sort:
        df = df.sort_values(by="Happiness Rank", ascending=True).reset_index(drop=True)
    elif desc_sort:
        df = df.sort_values(by="Happiness Rank", ascending=False).reset_index(drop=True)

    tab1, tab2, tab3 = st.tabs(["📊 Analysis", "📈 Graphs", "⌛ Time Trend"])

    with tab1:

        if selected_country != "All":
            df = df[df["Country"] == selected_country]

        st.header(f"Displayed data form: {selected_year}")

        st.dataframe(df)

        st.markdown(file_download(df, selected_year), unsafe_allow_html=True)

    with tab2:

        if selected_country == "All":
            fig_hm = px.choropleth(df,
                                   locations="Country",
                                   locationmode="country names",
                                   color="Happiness Rank",
                                   hover_name="Country",
                                   color_continuous_scale="Plasma",
                                   title="Happiness Heatmap")
            st.plotly_chart(fig_hm)

            fig_cor = px.scatter(df, x="Happiness Score", y="Country", title="Correlation")

            st.plotly_chart(fig_cor)
        else:
            st.warning("This tab is available only for \"All\" Countries")

    with tab3:
        merged_df = get_merged_df(2015, 2019)

        if selected_country != "All":
            merged_df = merged_df[merged_df["Country"] == selected_country]

            trend_fig = px.line(merged_df,
                                x="Year",
                                y="Happiness Score",
                                title=f"Time trend for {selected_year} in {selected_country}",
                                markers=True)

            st.plotly_chart(trend_fig)

        else:
            st.warning("This tab is available only for different countries.")






if __name__ == '__main__':
    main()

