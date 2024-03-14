import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

def probability_viz_1():
    # Load data from a CSV file
    csv_file_path = "mm24predictions.csv"
    data = pd.read_csv(csv_file_path)  

    # Sidebar filters
    min_prob, max_prob = st.sidebar.slider("Probability Range", 0.0, 1.0, (0.0, 1.0))

    # Filter data
    filtered_data = data[(data["Probability"] >= min_prob) & (data["Probability"] <= max_prob)]

    # Display filtered data
    st.write(filtered_data)

def probability_viz_2():
    # Load data from a CSV file
    csv_file_path = "mm-24-predictions.csv"
    data = pd.read_csv(csv_file_path)  

    # Sidebar filters
    min_prob, max_prob = st.sidebar.slider("Probability Range", 0.0, 1.0, (0.0, 1.0))

    # Filter data
    filtered_data = data[(data["Probability"] >= min_prob) & (data["Probability"] <= max_prob)]

    # Display filtered data
    st.write(filtered_data)

if __name__ == "__main__":
    page_1 = "NCAAB All Analysis"
    page_2 = "NCAAB 23-24 Analysis"
    page = st.sidebar.selectbox("Page", [page_1, page_2])

    if page == page_1:
        probability_viz_1()
    elif page == page_2:
        probability_viz_2()
