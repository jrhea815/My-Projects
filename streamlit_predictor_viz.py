import streamlit as st
import pandas as pd

csvfile = 'MM_24_Predictions_d_2.csv'

def big_dance_eliminated_list():
    eliminated_list = [
        'Mississippi State',
        'Akron',
        'Long Beach State',
        'Wagner',
        'Morehead State',
        'South Carolina',
        'Nevada',
        'Colorado State',
        'Kentucky',
        'McNeese State',
        'South Dakota State',
        "Saint Peter's",
        'Texas Tech',
        'Drake',
        'Samford'
    ]

    return eliminated_list
if __name__ == "__main__":
    #Header
    st.title("Jay's Algo for March Madness 24")
    
    # Add a description
    st.write("""
    Welcome to Jay's Algo for March Madness 24! This app allows you to analyze matchups between different teams based on their probabilities of winning and losing.
    
    This algorithm uses Evan Miya's Team Rating Data and will be updated as each round moves on!
    
    Select a team from the dropdown menu to view all matchups involving that team. Then, select one or more teams for the opposing side.
    
    **Please note that the "survive" column represents the probability that Team 1 survives, and the "defeat" column represents the probability that Team 1 is defeated.**
    
    For exploring matchups from the perspective of Team 2, try selecting Team 2 first and then Team 1.
    """)
    
    # Read the CSV file
    df = pd.read_csv(csvfile)
    
    # Filter by probabilities
    min_survive = st.slider('Minimum Survive Probability', min_value=0.0, max_value=100.0, value=0.0)
    min_defeat = st.slider('Minimum Defeat Probability', min_value=0.0, max_value=100.0, value=0.0)
    
    filtered_df = df[(df['survive'] >= min_survive) & (df['defeat'] >= min_defeat)]
    
    # If no team is selected, display the filtered dataframe
    if not st.session_state.team_1:
        st.write(df)
    
    # Select team 1
    team_1 = st.selectbox('Select Team 1', options=filtered_df['team_name_1'].unique(), key="team_1")
    
    # Filter the dataframe based on selected team 1
    team_1_df = df[df['team_name_1'] == team_1]
    
    # Select team 2 or multiple team 2s
    selected_team_2s = st.multiselect('Select Team 2(s)', options=team_1_df['team_name_2'].unique(), key="team_2")
    
    # Filter the dataframe based on selected teams
    matchups_df = team_1_df[team_1_df['team_name_2'].isin(selected_team_2s)]
    
    # Display the filtered data
    st.write(matchups_df)

    # List of eliminated teams (example)
    eliminated_teams = big_dance_eliminated_list()
    
    # Display eliminated teams
    st.subheader("Eliminated Teams")
    if eliminated_teams:
        for team in eliminated_teams:
            st.write("- " + team)
    else:
        st.write("No teams have been eliminated.")
