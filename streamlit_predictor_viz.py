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

# Filter by probabilities
min_survive = st.slider('Minimum Survive Probability', min_value=0.0, max_value=100.0, value=0.0)
min_defeat = st.slider('Minimum Defeat Probability', min_value=0.0, max_value=100.0, value=0.0)

filtered_df = df[(df['survive'] >= min_survive) & (df['defeat'] >= min_defeat)]

# Select team 1 and team 2
team_1 = st.selectbox('Select Team 1', options=filtered_df['team_name_1'].unique())
team_2 = st.selectbox('Select Team 2', options=filtered_df['team_name_2'].unique())

# Filter the dataframe based on selected teams
matchups_df = filtered_df[(filtered_df['team_name_1'] == team_1) & (filtered_df['team_name_2'] == team_2)]

# Display the filtered data
st.write(matchups_df)
