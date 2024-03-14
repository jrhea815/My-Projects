import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

def top_10_teams(data):
    # Group data by Team 1 and calculate the average probability
    team1_avg_prob = data.groupby("Team1")["Probability"].mean().reset_index()
    team1_avg_prob.columns = ['Team', 'Avg Probability']

    # Group data by Team 2 and calculate the average probability
    team2_avg_prob = data.groupby("Team2")["Probability"].mean().reset_index()
    team2_avg_prob.columns = ['Team', 'Avg Probability']

    # Merge both dataframes to get average probability for each team
    avg_prob_df = pd.concat([team1_avg_prob, team2_avg_prob]).groupby('Team').mean().reset_index()

    # Sort teams based on average probability
    avg_prob_df = avg_prob_df.sort_values(by='Avg Probability', ascending=False)

    # Select top 10 teams
    top_10 = avg_prob_df.head(10)

    return top_10
    
def probability_viz_1():
    # Load data from a CSV file
    csv_file_path = "mm24predictions.csv"
    data = pd.read_csv(csv_file_path)  
    
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
