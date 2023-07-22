import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import plotly.express as px
import folium
from streamlit_folium import folium_static

# This is where we are setting the entire webpage
st.set_page_config(
    page_title="Performance Analysis: Virat Kohli",
    page_icon="T",
    layout="wide"
)

main_df = pd.read_csv("kohlidf.csv")
# st.dataframe(main_df, width=1500)

st.title("Performance Analysis: Virat Kohli")

opponent_filter = st.selectbox("Select an opponent", pd.unique(main_df["Opposition"]))
st.write(opponent_filter)

placeholder = st.empty()

# get all the data from the opposition got selected from selectbox
df = main_df[main_df["Opposition"] == opponent_filter]


total_matches = df.shape[0]

total_runs = df["Runs"].sum()

total_6s = df["6s"].sum()

total_4s = df["4s"].sum()

average_strike_rate = df["SR"].mean()

highest_score = df["Runs"].max()

with placeholder.container():
    matches, runs, sixes, fours, strike_rates, score = st.columns(6)

    matches.metric(label="Total Matches", value=total_matches)

    runs.metric(label="Total Runs Scored", value=total_runs)

    sixes.metric(label="Total 6s",value=total_6s)

    fours.metric(label="Total Fours",value=total_4s)

    strike_rates.metric(label="Average Strike Rate", value=round(average_strike_rate, 2))

    score.metric(label="Highest Score", value=highest_score)

    fig1, fig2 = st.columns(2)

    with fig1:
        st.subheader("Runs Scored throughout the timeline")
        chart_data = df[["Runs", "Start Date"]]

        line_chart = alt.Chart(chart_data).mark_line().encode(
            y="Runs", x="Start Date"
        )

        st.write(line_chart)

    with fig2:
        st.subheader("Strike Rate throughout the timeline")
        chart_data = df[["SR", "Start Date"]]

        line_chart = alt.Chart(chart_data).mark_line().encode(
            y="SR", x="Start Date"
        )

        st.write(line_chart)

    fig3, fig4 = st.columns(2)

    with fig3:
        st.subheader("Histogram of Positions that Virat batted")
        pos_data = px.histogram(data_frame=df, x="Pos")
        st.write(pos_data)

    with fig4:
        st.subheader("Density Heatmap: Dismissal vs Balls Faced")
        heat_map_data = px.density_heatmap(data_frame=df, x="Dismissal", y="BF")
        st.write(heat_map_data)


st.subheader("Stadium Map")

map_center = [df["Lat"].mean(), df["Lon"].mean()]

stadium_map = folium.Map(location=map_center, zoom_start=5)

for index, row in df.iterrows():
    # index of the row and the complete row will get picked on every iteration
    ground_names = row["Ground"]
    lat = row["Lat"]
    lon = row["Lon"]
    marker = folium.Marker([lat, lon], popup=ground_names)
    marker.add_to(stadium_map)

folium_static(stadium_map, width=1500)