import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

def top_10_teams(data):
    # Calculate the average probability for Team 1
    team_avg_prob = data.groupby("Team1")["Probability"].mean().reset_index()
    team_avg_prob.columns = ['Team', 'Avg Probability']

    # Sort teams based on average probability
    team_avg_prob = team_avg_prob.sort_values(by='Avg Probability', ascending=False)

    # Select top 10 teams
    top_10 = team_avg_prob.head(10)

    return top_10
    
def probability_viz_1():
    # Load data from a CSV file
    csv_file_path = "mm24predictions.csv"
    data = pd.read_csv(csv_file_path)  

    # Get top 10 teams with highest average probability
    top_10 = top_10_teams(data)

    # Display ranking
    st.header("Top 10 Teams with Highest Average Probability of Winning")
    st.bar_chart(top_10.set_index('Team'))
    
    # Sidebar filters
    min_prob, max_prob = st.sidebar.slider("Probability Range", 0.0, 1.0, (0.0, 1.0))
    team_filter = st.sidebar.selectbox("Select Team", data["Team1"].unique())

    # Filter data
    filtered_data = data[(data["Probability"] >= min_prob) & (data["Probability"] <= max_prob)]
    if team_filter:
        filtered_data = filtered_data[(filtered_data["Team1"] == team_filter) | (filtered_data["Team2"] == team_filter)]

    # Display filtered data
    st.header("NCAAB Probability that Team 1 beats Team 2")
    st.write(filtered_data)

def probability_viz_2():
    # Load data from a CSV file
    csv_file_path = "mm-24-predictions.csv"
    data = pd.read_csv(csv_file_path)  

    # Get top 10 teams with highest average probability
    top_10 = top_10_teams(data)

    # Display ranking
    st.header("Top 10 Teams with Highest Average Probability of Winning")
    st.bar_chart(top_10.set_index('Team'))
    
    # Sidebar filters
    min_prob, max_prob = st.sidebar.slider("Probability Range", 0.0, 1.0, (0.0, 1.0))
    team_filter = st.sidebar.selectbox("Select Team", data["Team1"].unique())

    # Filter data
    filtered_data = data[(data["Probability"] >= min_prob) & (data["Probability"] <= max_prob)]
    if team_filter:
        filtered_data = filtered_data[(filtered_data["Team1"] == team_filter) | (filtered_data["Team2"] == team_filter)]

    # Display filtered data
    st.header("NCAAB Probability that Team 1 beats Team 2")
    st.write(filtered_data)

if __name__ == "__main__":
    page_1 = "NCAAB All Analysis"
    page_2 = "NCAAB 22-23 Analysis"
    page = st.sidebar.selectbox("Page", [page_1, page_2])

    if page == page_1:
        probability_viz_1()
    elif page == page_2:
        probability_viz_2()
