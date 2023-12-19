"""
Created on Thu Nov 23 2023

@author: Jayson Rhea
"""

import pyodbc 
import pandas as pd

server = 'mysqlserver077.database.windows.net' 
database = 'mySampleDatabase' 
username = 'azureuser' 
password = '"<YourStrong@Passw0rd>"' 

cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+password+';TrustServerCertificate=yes;')
cursor = cnxn.cursor()

"""
   Query Bank:
   Query 1: Find players who are not on a team.
   Query 2: Find the numbers of matches for each team that plays in B-League.
   Query 3: Find a match(es) for a specific date and time
   Query 4: Find all matches for a specific season and sport
   Query 5: Find players that have played more than one volleyball match in the fall season. 
   
"""
query_1 = pd.read_sql_query('''SELECT players.id, players.fname, players.lname 
FROM players WHERE players.id NOT IN (SELECT players_id FROM players_team); ''', cnxn)
print(query_1)

query_2 = pd.read_sql_query('''SELECT teams.team_name, 
COUNT(teams_matches.matches_id) AS number_of_matches
FROM teams
JOIN teams_matches ON teams.id = teams_matches.teams_id
JOIN matches ON teams_matches.matches_id = matches.id
JOIN leagues ON matches.leagues_id = leagues.id
WHERE leagues.league_name = 'B-league'
GROUP BY teams.team_name; ''', cnxn)
print(query_2)

query_3 = pd.read_sql_query('''SELECT id, matchup, date
FROM matches WHERE date = '2023-11-25 13:45:00'; ''', cnxn)
print(query_3)

query_4 = pd.read_sql_query('''SELECT matchup, date
FROM matches m
JOIN seasons ON m.seasons_id = seasons.id
JOIN sport ON m.sport_id = sport.id
WHERE seasons.season_name = 'fall' AND sport.sport_name = 'Volleyball'; ''', cnxn)
print(query_4)

query_5 = pd.read_sql_query('''SELECT players.id, players.fname, players.lname
FROM players
JOIN players_matches ON players.id = players_matches.players_id
JOIN matches ON players_matches.matches_id = matches.id
JOIN sport ON matches.sport_id = sport.id
JOIN seasons ON matches.seasons_id = seasons.id
WHERE sport.sport_name = 'Volleyball'
      AND seasons.season_name = 'fall'
GROUP BY players.id, players.fname, players.lname
HAVING COUNT(DISTINCT matches.id) > 1; ''', cnxn)
print(query_5)




## insert
cursor.execute('''INSERT INTO players (id, fname, lname, email)
VALUES
(51, 'Alexander', 'Johnson', 'alexander.johnson@example.com'),
(52, 'Sophia', 'Anderson', 'sophia.anderson@example.com'),
(53, 'Liam', 'Williams', 'liam.williams@example.com'),
(54, 'Olivia', 'Davis', 'olivia.davis@example.com'),
(55, 'Noah', 'Martinez', 'noah.martinez@example.com'); ''')

## update
cursor.execute('''UPDATE players
SET email = 'ajohnson@example.com'
WHERE id = 51; ''')




## Stored Procedure
stored_procedure_query = """
EXEC dbo.GetTeamInfo @team_name = 'Team B';
"""
print(pd.read_sql_query(stored_procedure_query, cnxn))
cnxn.commit()
cursor.close()
cnxn.close()
