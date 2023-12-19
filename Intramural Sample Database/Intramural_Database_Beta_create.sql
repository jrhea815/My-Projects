-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2023-11-22 23:40:08.933

-- tables
-- Table: leagues
CREATE TABLE leagues (
    id int  NOT NULL,
    league_name char(20)  NOT NULL,
    CONSTRAINT leagues_pk PRIMARY KEY  (id)
);

-- Table: matches
CREATE TABLE matches (
    id int  NOT NULL,
    matchup char(20)  NOT NULL,
    date datetime  NOT NULL,
    seasons_id int  NOT NULL,
    sport_id int  NOT NULL,
    leagues_id int  NOT NULL,
    CONSTRAINT matches_pk PRIMARY KEY  (id)
);

-- Table: players
CREATE TABLE players (
    id int  NOT NULL,
    fname char(20)  NOT NULL,
    lname char(20)  NOT NULL,
    email char(100)  NOT NULL,
    CONSTRAINT players_pk PRIMARY KEY  (id)
);

-- Table: players_matches
CREATE TABLE players_matches (
    players_id int  NOT NULL,
    matches_id int  NOT NULL,
    CONSTRAINT players_matches_pk PRIMARY KEY  (players_id,matches_id)
);

-- Table: players_team
CREATE TABLE players_team (
    teams_id int  NOT NULL,
    players_id int  NOT NULL,
    CONSTRAINT players_team_pk PRIMARY KEY  (teams_id,players_id)
);

-- Table: seasons
CREATE TABLE seasons (
    id int  NOT NULL,
    season_name char(20)  NOT NULL,
    CONSTRAINT seasons_pk PRIMARY KEY  (id)
);

-- Table: sport
CREATE TABLE sport (
    id int  NOT NULL,
    sport_name char(20)  NOT NULL,
    CONSTRAINT sport_pk PRIMARY KEY  (id)
);

-- Table: sport_seasons
CREATE TABLE sport_seasons (
    sport_id int  NOT NULL,
    seasons_id int  NOT NULL,
    CONSTRAINT sport_seasons_pk PRIMARY KEY  (sport_id,seasons_id)
);

-- Table: teams
CREATE TABLE teams (
    id int  NOT NULL,
    team_name char(20)  NOT NULL,
    CONSTRAINT teams_pk PRIMARY KEY  (id)
);

-- Table: teams_matches
CREATE TABLE teams_matches (
    matches_id int  NOT NULL,
    teams_id int  NOT NULL,
    CONSTRAINT teams_matches_pk PRIMARY KEY  (matches_id,teams_id)
);

-- foreign keys
-- Reference: Matches_Leagues (table: matches)
ALTER TABLE matches ADD CONSTRAINT Matches_Leagues
    FOREIGN KEY (leagues_id)
    REFERENCES leagues (id);

-- Reference: Matches_Seasons (table: matches)
ALTER TABLE matches ADD CONSTRAINT Matches_Seasons
    FOREIGN KEY (seasons_id)
    REFERENCES seasons (id);

-- Reference: Matches_Sport (table: matches)
ALTER TABLE matches ADD CONSTRAINT Matches_Sport
    FOREIGN KEY (sport_id)
    REFERENCES sport (id);

-- Reference: Players_Matches_Matches (table: players_matches)
ALTER TABLE players_matches ADD CONSTRAINT Players_Matches_Matches
    FOREIGN KEY (matches_id)
    REFERENCES matches (id);

-- Reference: Players_Matches_Players (table: players_matches)
ALTER TABLE players_matches ADD CONSTRAINT Players_Matches_Players
    FOREIGN KEY (players_id)
    REFERENCES players (id);

-- Reference: Players_Teams_Players (table: players_team)
ALTER TABLE players_team ADD CONSTRAINT Players_Teams_Players
    FOREIGN KEY (players_id)
    REFERENCES players (id);

-- Reference: Players_Teams_Teams (table: players_team)
ALTER TABLE players_team ADD CONSTRAINT Players_Teams_Teams
    FOREIGN KEY (teams_id)
    REFERENCES teams (id);

-- Reference: Sport_seasons_Seasons (table: sport_seasons)
ALTER TABLE sport_seasons ADD CONSTRAINT Sport_seasons_Seasons
    FOREIGN KEY (seasons_id)
    REFERENCES seasons (id);

-- Reference: Sport_seasons_Sport (table: sport_seasons)
ALTER TABLE sport_seasons ADD CONSTRAINT Sport_seasons_Sport
    FOREIGN KEY (sport_id)
    REFERENCES sport (id);

-- Reference: Teams_Matches_Matches (table: teams_matches)
ALTER TABLE teams_matches ADD CONSTRAINT Teams_Matches_Matches
    FOREIGN KEY (matches_id)
    REFERENCES matches (id);

-- Reference: Teams_Matches_Teams (table: teams_matches)
ALTER TABLE teams_matches ADD CONSTRAINT Teams_Matches_Teams
    FOREIGN KEY (teams_id)
    REFERENCES teams (id);

-- End of file.

