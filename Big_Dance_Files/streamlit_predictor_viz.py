import streamlit as st
import pandas as pd
from  import logreg_predict, create_team_list  # Import the necessary functions from your existing script

# Function to load CSV data
def load_data():
    return pd.read_csv('MM_24_Update_2.csv')  # Update with your CSV file path

# Function to create the prediction form
def prediction_form(teams):
    team1 = st.selectbox('Select Team 1', teams)
    team2 = st.selectbox('Select Team 2', teams)
    return team1, team2

# Function to display prediction results
def display_prediction(team1, team2, prediction):
    st.write(f"Prediction for {team1} vs {team2}:")
    st.write(f"{team1}: {prediction[0]:.2f}%")
    st.write(f"{team2}: {prediction[1]:.2f}%")

# Main function
def main():
    st.title('March Madness Predictor')

    # Load data
    df = load_data()

    # Create team list
    teams = create_team_list('MM_24_Update_2.csv')  # Update with your CSV file path

    # Prediction form
    team1, team2 = prediction_form(teams)

    # Execute predict function
    prediction = logreg_predict(team1, team2, 'MM_24_Update_2.csv')  # Update with your CSV file path

    # Display prediction results
    display_prediction(team1, team2, prediction)

if __name__ == "__main__":
    main()
