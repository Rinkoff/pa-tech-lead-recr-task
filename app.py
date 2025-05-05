from utils.data_processing import load_data, get_merged_df
from utils.file_helpers import file_download
import streamlit as st
import plotly.express as px



def main(available_years=["2015", "2016", "2017", "2018", "2019"]):
    st.sidebar.header("Filtration")

    selected_year = st.sidebar.selectbox("Year", available_years,
                                         help="Select the year from which you want to view the data.")
    df = load_data(selected_year)

    unique_countries = df["Country"].dropna().unique()

    selected_country = st.sidebar.multiselect("Country", options=["All"] + list(unique_countries), default=["All"],
                                             help="Select one or more countries to filter the data.")

    st.sidebar.caption("ℹ️ **Note:** To apply a 'Country' filter, please deselect 'All'.")

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

        if "All" not in selected_country:
            df = df[df["Country"].isin(selected_country)]

        st.header(f"Displayed data form: {selected_year}")

        st.dataframe(df)

        st.markdown(file_download(df, selected_year), unsafe_allow_html=True)

    with tab2:
        if "All" in selected_country and len(selected_country) == 1:
            fig_hm = px.choropleth(df,
                                    locations="Country",
                                    locationmode="country names",
                                    color="Happiness Score",
                                    hover_name="Country",
                                    hover_data={
                                        'Happiness Score': True,
                                        'Happiness Rank': True
                                    },
                                    color_continuous_scale="Plasma",
                                    title="Happiness Heatmap")

            fig_hm.add_annotation(
                    text="🙂",
                    x=1.06, y=0.83,
                    xref="paper", yref="paper",
                    showarrow=False,
                    font=dict(size=20))

            fig_hm.add_annotation(
                    text="🙁",
                    x=1.06, y=0.22,
                    xref="paper", yref="paper",
                    showarrow=False,
                    font=dict(size=20))
            
            st.plotly_chart(fig_hm)

            fig_cor = px.scatter(df, x="Happiness Score", y="Country", title="Correlation")

            st.plotly_chart(fig_cor)
        else:
            if "All" in selected_country and len(selected_country) > 1:
                st.info("To apply 'All', please remove the specific countries from your selection.")
            st.warning("This tab will be available only for \"All\" Countries")

    with tab3:
        merged_df = get_merged_df(2015, 2019)

        if "All" not in selected_country:
            merged_df = merged_df[merged_df["Country"].isin(selected_country)]

            for country in selected_country:
                country_df = merged_df[merged_df["Country"] == country]

                trend_fig = px.line(
                    country_df,
                    x="Year",
                    y="Happiness Score",
                    title=f"Time Trend for {country}",
                    markers=True
                )
                st.plotly_chart(trend_fig)
        else:
            st.warning("This tab is active only when specific countries are selected. Please deselect 'All' to proceed.")






if __name__ == '__main__':
    main()

