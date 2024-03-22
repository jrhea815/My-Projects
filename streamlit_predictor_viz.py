import streamlit as st
import pandas as pd

csvfile = 'MM_24_Predictions_d_2.csv'

#Header
st.title("Jay's Algo for March Madness 24")

# Add a description
st.write("""
Welcome to Jay's Algo for March Madness 24! This app allows you to analyze matchups between different teams based on their probabilities of winning and losing.

This algorithm uses Evan Miya's Team Rating Data and will be updated as each round moves on!

Use the sliders to filter matchups based on the minimum probability of survival and defeat. Then, select two teams from the dropdown menus to view specific matchup details.

Let's explore some matchups!
""")

# Read the CSV file
df = pd.read_csv(csvfile)

# Select team 1
team_1 = st.selectbox('Select Team 1', options=df['team_name_1'].unique())

# Filter the dataframe based on selected team 1
team_1_df = df[df['team_name_1'] == team_1]

# Select team 2 or multiple team 2s
selected_team_2s = st.multiselect('Select Team 2(s)', options=team_1_df['team_name_2'].unique())

# Filter the dataframe based on selected teams
matchups_df = team_1_df[team_1_df['team_name_2'].isin(selected_team_2s)]

# Display the filtered data
st.write(matchups_df)
