import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")


def probability_viz_1():
    # Load data from a CSV file
    csv_file_path = "mm24predictions.csv"
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

def probablitiy_viz_2()
        # Load data from a CSV file
    csv_file_path = "mm-24-predictions.csv"
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
    page = st.sidebar.radio("Page", ["Probability Viz 1", "Probability Viz 2"])

    if page == "Probability Viz 1":
        probability_viz_1()
    elif page == "Probability Viz 2":
        probability_viz_2()
