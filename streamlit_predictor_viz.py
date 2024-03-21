import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from xgboost import XGBRegressor
import Levenshtein
from sklearn.preprocessing import StandardScaler

big_dance_df = pd.read_csv('Big_Dance_CSV.csv')

miya_data_2015 = pd.read_csv('EvanMiya Team Ratings 2014-15.csv')
miya_data_2016 = pd.read_csv('EvanMiya Team Ratings 2015-16.csv')
miya_data_2017 = pd.read_csv('EvanMiya Team Ratings 2016-17.csv')
miya_data_2018 = pd.read_csv('EvanMiya Team Ratings 2017-18.csv')
miya_data_2019 = pd.read_csv('EvanMiya Team Ratings 2018-19.csv')
year_list = [2015, 2016, 2017, 2018, 2019] #Years to Train

def build_matchup_results(df, year_list):
    results = []
    for year in year_list:
        year_data = df[df.iloc[:, 0] == year]  # Using positional indexing for the 'Year' column

        for index, row in year_data.iterrows():
            team1 = row.iloc[6]  # Using positional indexing for 'Team 1' (column 6)
            team2 = row.iloc[7]  # Using positional indexing for 'Team 2' (column 7)
            score1 = row.iloc[5]  # Using positional indexing for 'Score 1' (column 5)
            score2 = row.iloc[8]  # Using positional indexing for 'Score 2' (column 9)
            if score1 > score2:
                result = [[year], [team1, team2], [1, 0]]  # Team 1 wins
            else:
                result = [[year], [team1, team2], [0, 1]]  # Team 2 wins

            # Append the result to the results list
            results.append(result)

    return results


# Build get_team_stats function
def get_team_stats(data, team_name:str):
    team_stats = []
    if team_name == None:
      return [team_stats]
    team_data = data[data['team'] == team_name]
    if not team_data.empty:
        team_stats.append(team_data['rank'].iloc[0])
        team_stats.append(team_data['obpr'].iloc[0])
        team_stats.append(team_data['dbpr'].iloc[0])
        team_stats.append(team_data['bpr'].iloc[0])
        team_stats.append(team_data['opponent_adjust'].iloc[0])
        team_stats.append(team_data['pace_adjust'].iloc[0])
        team_stats.append(team_data['off_rank'].iloc[0])
        team_stats.append(team_data['def_rank'].iloc[0])
        team_stats.append(team_data['tempo'].iloc[0])
        team_stats.append(team_data['tempo_rank'].iloc[0])
        team_stats.append(team_data['home_rank'].iloc[0])
        team_stats.append(team_data['wins'].iloc[0])
        team_stats.append(team_data['losses'].iloc[0])

    return team_stats

# To Reduce Discrepancy in Team Names
def is_string_match(string1, string2, threshold=0.75):
    distance = Levenshtein.distance(string1, string2)
    max_length = max(len(string1), len(string2))
    similarity = 1 - (distance / max_length)
    return similarity >= threshold

# Check to see if team name matches with other dataset
def is_team_match(df, team_string:str):
    team_match_list = []
    df = df
    for team in df['team']:
        if is_string_match(team, team_string):
            team_match_list.append(team)
        else:
            pass

    if len(team_match_list) == 1:
        team_name = team_match_list[0]
    else:
        team_name = None

    return team_name

#Normalize CSV DF
def normalize_df(df):
    # Select only the numerical columns for normalization
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    # Initialize the StandardScaler
    scaler = StandardScaler()
    # Apply StandardScaler to the numerical columns
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

    normalized_df = df

    return normalized_df


# Build training list using Evan Miya Data
def build_Miya_training_set():
    year_team_stat_list = [miya_data_2015, miya_data_2016, miya_data_2017, miya_data_2018, miya_data_2019]
    training_set = []
    matchup_results = build_matchup_results(big_dance_df, year_list)

    for match in matchup_results:
        year = match[0][0]
        team1 = match[1][0]
        team2 = match[1][1]
        team1_result = match[2][0]
        team2_result = match [2][1]

        for i in range(5):
            if year_list[i] == year:
                df = normalize_df(year_team_stat_list[i])
                team1_stats = get_team_stats(df, team1)
                team2_stats = get_team_stats(df, team2)
                matchup_1 = [team1_stats, team2_stats, team1_result]
                matchup_2 = [team2_stats, team1_stats, team2_result]
                training_set.append(matchup_1)
                training_set.append(matchup_2)

    return training_set




# Logistic Regression Model
def logistic_regression_model(X_train, y_train):
    X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.2, random_state=15)
    logreg = LogisticRegression(max_iter=2000)
    logreg.fit(X_train, y_train)
    y_pred = logreg.predict(X_test)
    return classification_report(y_test, y_pred)

# Bayes Model
def naive_bayes_model(X_train, y_train):
    X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.2, random_state=15)
    nb = GaussianNB()
    nb.fit(X_train, y_train)
    y_pred = nb.predict(X_test)
    return classification_report(y_test, y_pred)

# XGBoost Regression Model
def xgboost_regression_model(X_train, y_train):
    X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.2, random_state=0)
    xgb = XGBRegressor()
    xgb.fit(X_train, y_train)
    y_pred = xgb.predict(X_test)
    return accuracy_score(y_test, y_pred)


#Flatten_list to apply to model
def flatten_list(list:list):
    flattened_list = []
    for sublist in list:
        new_list = sublist[0] + sublist[1]
        flattened_list.append(new_list)
    return flattened_list



def create_team_dict(df):
    team_stats_dict = {}

    for team_name in df['team']:
        team_stats = get_team_stats(df,team_name)
        team_stats_dict[team_name] = team_stats

    return team_stats_dict

#Team1 vs Team2
def create_team_matchup(dict:dict, team1:str, team2:str):
    matchup = [dict[team1] + dict[team2]]
    return matchup

def get_X_train_y_train(training_set:list):
    #Create a cleaned training_set:
    training_set = build_Miya_training_set()
    cleaned_training_set = []
    for sublist in training_set:
        if [] not in sublist:
            cleaned_training_set.append(sublist)

    data = cleaned_training_set

    #Split cleaned_training_set into labels:
    X_train = [matchup[:-1] for matchup in data]  # Extract features for each matchup
    y_train = [matchup[-1] for matchup in data]   # Extract labels for each matchup
    
    #Flatten X_train
    X_train = flatten_list(X_train)

    return X_train, y_train

def logreg_predict(team1:str , team2:str, CSVFILE):
    
    training_set = build_Miya_training_set()
    X_train, y_train = get_X_train_y_train(training_set)

    X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.2, random_state=15)
    logreg = LogisticRegression(max_iter=5000)
    logreg.fit(X_train, y_train)

    Dataset = pd.read_csv(CSVFILE)
    Normalized_Dataset = normalize_df(Dataset)
    team_dict_stats_24 = create_team_dict(Normalized_Dataset)

    match_test = create_team_matchup(team_dict_stats_24, team1, team2)

    # match_test_2= create_team_matchup(team_dict_stats_24, team2, team1)
    
   
    ypred1 = logreg.predict_proba(match_test)
    # ypred2 = logreg.predict_proba(match_test_2)
    

    value1 = ypred1[0][1]*100 
    value2 = ypred1[0][0]*100
    
    team1_values = [value1, value2]
    return team1_values

def create_team_list(CSVFILE):
    
    # Read the CSV file
    df = pd.read_csv(CSVFILE)

    # Extract the "team" column as a list
    team_names = df["team"].tolist()

    # Print the list of team names
    return team_names[0:10]
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
