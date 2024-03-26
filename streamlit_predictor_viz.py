import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")

csvfile = 'MM_24_Predictions_Day_5.csv'

def big_dance_eliminated_list():
    eliminated_list = [
        'Mississippi State',
        'BYU',
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
        'Florida Atlantic',
        'Colgate',
        'UAB',
        'Western Kentucky',
        'New Mexico',
        'Stetson',
        'Florida',
        'Auburn',
        'Nebraska',
        'College of Charleston',
        'Wisconsin',
        'Longwood',
        'TCU',
        "Saint Mary's",
        'Dayton',
        'Kansas',
        'Michigan State',
        'Washington State',
        'Oakland',
        'Duquesne',
        'Texas',
        'Oregon',
        'Colorado',
        'Utah State',
        'James Madison',
        'Baylor',
        'Grand Canyon',
        'NorthWestern',
        'Texas A&M',
        'Yale',
        'Grambling'
    ]

    return eliminated_list
if __name__ == "__main__":
    #Header
    st.title("Jay's alogrithm for March Madness 24")
    
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
    
   # Select team 1 and team 2
    team_1 = st.selectbox('Select Team 1', options=df['team_name_1'].unique(), key="team_1")
    team_2 = st.selectbox('Select Team 2', options=df['team_name_2'].unique(), key="team_2")
    
    # Filter the dataframe based on selected teams
    matchups_df_1 = df[(df['team_name_1'] == team_1) & (df['team_name_2'] == team_2)]
    matchups_df_2 = df[(df['team_name_1'] == team_2) & (df['team_name_2'] == team_1)]
    
    # Concatenate both dataframes
    all_matchups_df = pd.concat([matchups_df_1, matchups_df_2])
    
    # Display the filtered data
    st.write(all_matchups_df)

    # List of eliminated teams (example)
    eliminated_teams = big_dance_eliminated_list()
    
    # Display eliminated teams
    st.subheader(f"Eliminated Teams")
    if eliminated_teams:
        for team in eliminated_teams:
            st.write("- " + team)
    else:
        st.write("No teams have been eliminated.")
