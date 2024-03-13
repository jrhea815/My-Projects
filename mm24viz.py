import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")


def probability_viz():
    # Load data from a CSV file
    csv_file_path = "C:/Users/jcmrh/Desktop/March Madness Data/mm24predictions.csv"
    data = pd.read_csv(csv_file_path)  

    # Page layout
    page = st.sidebar.radio("Page", ["Probabilities", "Team Comparison"])

    # Sidebar filters
    if page == "Probabilities":
        min_prob, max_prob = st.sidebar.slider("Probability Range", 0.0, 1.0, (0.0, 1.0))
    else:
        team_filter = st.sidebar.selectbox("Select Team", data["Team1"].unique())

    # Filter data
    if page == "Probabilities":
        filtered_data = data[(data["Probability"] >= min_prob) & (data["Probability"] <= max_prob)]
    else:
        filtered_data = data[data["Team1"] == team_filter]

    # Display filtered data
    st.write(filtered_data)




if __name__ == "__main__":

    probability_viz()