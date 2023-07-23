import pandas as pd
import streamlit as st
import altair as alt
import folium
import plotly.express as px

st.set_page_config(
    page_title="Cinema Ticket Analysis",
    page_icon="C",
    layout="wide"
)

main_df = pd.read_csv('tickets.csv')

# st.dataframe(main_df, width=1500)

st.title("Cinema Ticket Analysis")

film_filter = st.selectbox("Select a film", pd.unique(main_df["film_code"]))

placeholder = st.empty()

df = main_df[main_df["film_code"] == film_filter]

total_sales = df["total_sales"].sum()
total_tickets_sold = df["tickets_sold"].sum()
total_tickets_out = df["tickets_out"].sum()
avg_capacity = df["capacity"].mean()
avg_show_time = df["show_time"].mean()
avg_ticket_price = df["ticket_price"].mean()


with placeholder.container():
    sales, tickets_sold, tickets_out, capacity, show_time, ticket_price = st.columns(6)

    sales.metric(label="Total Sales", value=total_sales)
    tickets_sold.metric(label="Total Tickets Sold:", value=total_tickets_sold)
    tickets_out.metric(label="Total Tickets Out:", value=total_tickets_out)
    capacity.metric(label="Average Capacity:", value=round(avg_capacity, 2))
    show_time.metric(label="Average Show Time: ", value=round(avg_show_time, 2))
    ticket_price.metric(label="Ticket Price:", value=round(avg_ticket_price, 2))
    st.dataframe(df, width=1500)

    day_col, month_col, quarter_col = st.columns(3)

    
    # Creating a day filter
    with day_col:
        day_filter = st.selectbox("Select a day", pd.unique(df["day"].sort_values()))
        day_df = df[df["day"] == day_filter]

        daily_tickets_sold, daily_total_sales = st.columns(2)

        daily_tickets_sold_data = day_df["tickets_sold"].sum()
        daily_avg_tickets_sold = day_df["tickets_sold"].mean()
        daily_avg_show_time = day_df["show_time"].mean()
        daily_avg_capacity = day_df["capacity"].mean()

        daily_tickets_sold.metric(label="Total Tickets Sold", value=daily_tickets_sold_data)
        daily_tickets_sold.metric(label="Daily Avg Tickets Sold", value=round(daily_avg_tickets_sold, 2))
        daily_tickets_sold.metric(label="Daily Avg Show Time", value=round(daily_avg_show_time, 2))

        daily_total_sales_data = day_df["total_sales"].sum()
        daily_avg_sales_data = day_df["total_sales"].mean()

        daily_total_sales.metric(label="Total Sales", value=daily_total_sales_data)
        daily_total_sales.metric(label="Average Sales", value=round(daily_avg_sales_data, 2))
        daily_total_sales.metric(label="Daily Avergae Capacity", value=round(daily_avg_capacity, 2))


    with month_col:
        month_filter = st.selectbox("Select a month", pd.unique(df["month"].sort_values()))
        month_df = df[df["month"] == month_filter]

        st.subheader("Monthly Tickets Sold")
        monthly_ticket_chart_data = month_df[["tickets_sold","date"]]
        monthly_line_chart = alt.Chart(monthly_ticket_chart_data).mark_line().encode(
            y="tickets_sold", x="date"
        )

        st.altair_chart(monthly_line_chart, use_container_width=True)

    with quarter_col:
        quarter_filter = st.selectbox("Select a quarter", pd.unique(df["quarter"].sort_values()))
        # Plotting the graphs
        quarter_df = df[df["quarter"] == quarter_filter]

        st.subheader("Quarterly Tickets Sold")
        quarterly_ticket_chart_data = quarter_df[["tickets_sold","date"]]
        quarterly_line_chart = alt.Chart(quarterly_ticket_chart_data).mark_line().encode(
            y="tickets_sold", x="date"
        )

        st.altair_chart(quarterly_line_chart, use_container_width=True)


    fig1, fig2 = st.columns(2)
    
    with fig1:
        st.subheader("Datewise Total Sales")

        sales_chart_data = df[["total_sales", "date"]]
        line_chart = alt.Chart(sales_chart_data).mark_line().encode(
            y="total_sales", x="date"
        )
        st.altair_chart(line_chart, use_container_width=True)
        # st.write(line_chart, )

    with fig2:
        st.subheader("Datewise Tickets Sales")

        ticket_chart_data = df[["tickets_sold", "date"]]

        ticket_line_chart = alt.Chart(ticket_chart_data).mark_line().encode(
            y="tickets_sold", x="date"
        )

        st.altair_chart(ticket_line_chart, use_container_width=True)

    fig3, fig4 = st.columns(2)

    with fig3:
        st.subheader("Datewise Ticket Price")

        price_chart_data = df[["ticket_price", "date"]]
        price_line_chart_data = alt.Chart(price_chart_data).mark_line().encode(
            y="ticket_price", x="date"
        )

        st.altair_chart(price_line_chart_data, use_container_width=True)

    with fig4:
        st.subheader("Datewise Ticket Used")

        used_chart_data = df[["ticket_use", "date"]]
        used_line_chart = alt.Chart(used_chart_data).mark_line().encode(
            y="ticket_use", x="date"
        )

        st.altair_chart(used_line_chart, use_container_width=True)


    cinema_filter = st.selectbox("Select a Hall", pd.unique(main_df["cinema_code"]))

    cinema_placeholder = st.empty()
    cinema_df = df[df["cinema_code"] == cinema_filter]
    # st.dataframe(cinema_df, width=1500)

    total_sales = cinema_df["total_sales"].sum()
    total_tickets_sold = cinema_df["tickets_sold"].sum()
    total_tickets_out = cinema_df["tickets_out"].sum()
    avg_capacity = cinema_df["capacity"].mean()
    avg_show_time = cinema_df["show_time"].mean()
    avg_ticket_price = cinema_df["ticket_price"].mean()

    sales, tickets_sold, tickets_out, capacity, show_time, ticket_price = st.columns(6)

    sales.metric(label="Total Sales", value=total_sales)
    tickets_sold.metric(label="Total Tickets Sold:", value=total_tickets_sold)
    tickets_out.metric(label="Total Tickets Out:", value=total_tickets_out)
    capacity.metric(label="Average Capacity:", value=round(avg_capacity, 2))
    show_time.metric(label="Average Show Time: ", value=round(avg_show_time, 2))
    ticket_price.metric(label="Ticket Price:", value=round(avg_ticket_price, 2))
    st.dataframe(cinema_df, width=1500)

    # Plotting the graphs
    fig1, fig2 = st.columns(2)
    
    with fig1:
        st.subheader("Datewise Total Sales")

        sales_chart_data = cinema_df[["total_sales", "date"]]
        line_chart = alt.Chart(sales_chart_data).mark_line().encode(
            y="total_sales", x="date"
        )
        st.altair_chart(line_chart, use_container_width=True)
        # st.write(line_chart, )

    with fig2:
        st.subheader("Datewise Tickets Sales")

        ticket_chart_data = cinema_df[["tickets_sold", "date"]]

        ticket_line_chart = alt.Chart(ticket_chart_data).mark_line().encode(
            y="tickets_sold", x="date"
        )

        st.altair_chart(ticket_line_chart, use_container_width=True)
    
    fig3, fig4 = st.columns(2)

    with fig3:
        st.subheader("Datewise Ticket Price")

        price_chart_data = cinema_df[["ticket_price", "date"]]
        price_line_chart_data = alt.Chart(price_chart_data).mark_line().encode(
            y="ticket_price", x="date"
        )

        st.altair_chart(price_line_chart_data, use_container_width=True)

    with fig4:
        st.subheader("Datewise Ticket Used")

        used_chart_data = cinema_df[["ticket_use", "date"]]
        used_line_chart = alt.Chart(used_chart_data).mark_line().encode(
            y="ticket_use", x="date"
        )

        st.altair_chart(used_line_chart, use_container_width=True)

    day_col, month_col, quarter_col = st.columns(3)

    
    # Creating a day filter
    with day_col:
        cinema_day_filter = st.selectbox("Hall: Select a day", pd.unique(cinema_df["day"].sort_values()))
        day_df = cinema_df[cinema_df["day"] == cinema_day_filter]

        daily_tickets_sold, daily_total_sales = st.columns(2)

        daily_tickets_sold_data = day_df["tickets_sold"].sum()
        daily_avg_tickets_sold = day_df["tickets_sold"].mean()
        daily_avg_show_time = day_df["show_time"].mean()
        daily_avg_capacity = day_df["capacity"].mean()

        daily_tickets_sold.metric(label="Total Tickets Sold", value=daily_tickets_sold_data)
        daily_tickets_sold.metric(label="Daily Avg Tickets Sold", value=round(daily_avg_tickets_sold, 2))
        daily_tickets_sold.metric(label="Daily Avg Show Time", value=round(daily_avg_show_time, 2))

        daily_total_sales_data = day_df["total_sales"].sum()
        daily_avg_sales_data = day_df["total_sales"].mean()

        daily_total_sales.metric(label="Total Sales", value=daily_total_sales_data)
        daily_total_sales.metric(label="Average Sales", value=round(daily_avg_sales_data, 2))
        daily_total_sales.metric(label="Daily Avg Capacity", value=round(daily_avg_capacity, 2))


    with month_col:
        cinema_month_filter = st.selectbox("Hall: Select a month", pd.unique(cinema_df["month"].sort_values()))
        month_df = cinema_df[cinema_df["month"] == cinema_month_filter]

        monthly_tickets_sold, monthly_total_sales = st.columns(2)
        monthly_tickets_sold_data = month_df["tickets_sold"].sum()
        monthly_avg_tickets_sold = month_df["tickets_sold"].mean()
        monthly_avg_show_time = month_df["show_time"].mean()
        monthly_avg_capacity = month_df["capacity"].mean()

        monthly_tickets_sold.metric(label="Total Tickets Sold", value=monthly_tickets_sold_data)
        monthly_tickets_sold.metric(label="Monthly Avg Tickets Sold", value=round(monthly_avg_tickets_sold, 2))
        monthly_tickets_sold.metric(label="Monthly Avg Show Time", value=round(monthly_avg_show_time, 2))

        monthly_total_sales_data = month_df["total_sales"].sum()
        monthly_avg_sales_data = month_df["total_sales"].mean()
        monthly_total_sales.metric(label="Total Sales", value=monthly_total_sales_data)
        monthly_total_sales.metric(label="Average Sales", value=round(monthly_avg_sales_data, 2))
        monthly_total_sales.metric(label="Monthly Avg Capacity", value=round(monthly_avg_capacity,2))

    with quarter_col:
        quarter_filter = st.selectbox("Hall: Select a quarter", pd.unique(cinema_df["quarter"].sort_values()))
        # Plotting the graphs
        quarter_df = cinema_df[cinema_df["quarter"] == quarter_filter]

        st.subheader("Quarterly Tickets Sold")
        quarterly_ticket_chart_data = quarter_df[["tickets_sold","date"]]
        quarterly_line_chart = alt.Chart(quarterly_ticket_chart_data).mark_line().encode(
            y="tickets_sold", x="date"
        )

        st.altair_chart(quarterly_line_chart, use_container_width=True)









# We will select individual films and find our
# - total sales of individual films
# - total tickets sold
# - total tickets out
# - average capapcity
# - average show time
# - average ticket price
# - datewise tickets sales
# - datewise total sales
# - date wise ticket price (line chart)
# - date wise tickets sales (line_chart)
# - Quarter wise tickets sales (line_chart)
