import streamlit as st
from streamlit_folium import folium_static
import altair as alt
import numpy as np
import pandas as pd
import plotly.express as px
import folium


st.set_page_config(
    page_title="Virat Kohli Performance Dashboard",
    page_icon="T",
    layout="wide"
)

main_df = pd.read_csv("kohlidf.csv")
# st.write(main_df)  
st.dataframe(data=main_df, width=1500)

st.title("Kohli Performance Analysis Dashboard")

opponent_filter = st.selectbox("Select Opponent", pd.unique(main_df["Opposition"]))
st.write(opponent_filter)
placeholder = st.empty()
df = main_df[main_df["Opposition"] == opponent_filter]

# Creating metrics
st.write("Overall analysis of data vs ", opponent_filter)
st.dataframe(data=df.describe(), width=1500)
# st.write(df.describe())

total_matches = df.shape[0]

total_runs_scored = df["Runs"].sum()

total_sixes = df["6s"].sum()

total_fours = df["4s"].sum()

avg_strike_rate = df["SR"].mean()

highest_score = df["Runs"].max()

with placeholder.container():
    matches, runs, sixes, fours, strike_rate, highest = st.columns(6)

    matches.metric(label="Total Matches Played", value=total_matches)
    runs.metric(label="Total Runs Scored", value=total_runs_scored)
    sixes.metric(label="Total No. of Sixes", value=total_sixes)
    fours.metric(label="Total No. of Fours", value=total_fours)
    strike_rate.metric(label="Average Strike Rate", value=avg_strike_rate)
    highest.metric(label="Highest Score", value=highest_score)

    #Line charts
    fig1, fig2 = st.columns(2)

    with fig1:
        st.markdown("Runs scored on different matches")
        chart_data = df[["Runs", "Start Date"]]
        line_chart = alt.Chart(chart_data).mark_line().encode(
            y="Runs", x="Start Date"
        )
        st.write(line_chart)

    with fig2:
        st.markdown("Strike rates on different matches")
        chart_data = df[["SR", "Start Date"]]
        line_chart = alt.Chart(chart_data).mark_line().encode(
            y="SR", x="Start Date"
        )
        st.write(line_chart)

    fig3, fig4 = st.columns(2)

    with fig3:
        st.markdown("In at playing positions")
        pos_data = px.histogram(data_frame=df, x="Pos")
        st.write(pos_data)

    with fig4:
        st.markdown("Dismissal at Balls Faced")
        heat_data = px.density_heatmap(data_frame=df, y="BF", x="Dismissal")
        st.write(heat_data)


# with map:
st.markdown("Stadium plot")

map_center = [df["Lat"].mean(), df['Lon'].mean()]
stadium_map = folium.Map(location=map_center, zoom_start=5)
for index, row in df.iterrows():
    name = row['Ground']
    lat = row['Lat']
    lon = row['Lon']
    marker = folium.Marker([lat, lon], popup=name)
    marker.add_to(stadium_map)

folium_static(stadium_map, width=1500)