import streamlit as st
import pandas as pd

csvfile = 'MM_24_Predictions_d_2.csv'

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
