INSERT INTO players (id, fname, lname, email)
VALUES
(1, 'John', 'Doe', 'john.doe@example.com'),
(2, 'Jane', 'Smith', 'jane.smith@example.com'),
(3, 'Michael', 'Johnson', 'michael.johnson@example.com'),
(4, 'Emily', 'Williams', 'emily.williams@example.com'),
(5, 'Christopher', 'Brown', 'christopher.brown@example.com'),
(6, 'Amanda', 'Jones', 'amanda.jones@example.com'),
(7, 'Daniel', 'Miller', 'daniel.miller@example.com'),
(8, 'Ashley', 'Davis', 'ashley.davis@example.com'),
(9, 'Matthew', 'Garcia', 'matthew.garcia@example.com'),
(10, 'Jessica', 'Rodriguez', 'jessica.rodriguez@example.com'),
(11, 'David', 'Martinez', 'david.martinez@example.com'),
(12, 'Brittany', 'Hernandez', 'brittany.hernandez@example.com'),
(13, 'Brian', 'Lopez', 'brian.lopez@example.com'),
(14, 'Megan', 'Young', 'megan.young@example.com'),
(15, 'Justin', 'Lee', 'justin.lee@example.com'),
(16, 'Lauren', 'White', 'lauren.white@example.com'),
(17, 'Ryan', 'Scott', 'ryan.scott@example.com'),
(18, 'Samantha', 'Green', 'samantha.green@example.com'),
(19, 'Tyler', 'Hall', 'tyler.hall@example.com'),
(20, 'Alexis', 'Adams', 'alexis.adams@example.com'),
(21, 'Nicholas', 'Allen', 'nicholas.allen@example.com'),
(22, 'Katherine', 'Nelson', 'katherine.nelson@example.com'),
(23, 'Ethan', 'Turner', 'ethan.turner@example.com'),
(24, 'Olivia', 'Hill', 'olivia.hill@example.com'),
(25, 'Cody', 'Baker', 'cody.baker@example.com'),
(26, 'Emma', 'Cooper', 'emma.cooper@example.com'),
(27, 'Jordan', 'Perez', 'jordan.perez@example.com'),
(28, 'Kyle', 'Taylor', 'kyle.taylor@example.com'),
(29, 'Haley', 'Ward', 'haley.ward@example.com'),
(30, 'Brandon', 'Flores', 'brandon.flores@example.com'),
(31, 'Gabrielle', 'Morris', 'gabrielle.morris@example.com'),
(32, 'Evan', 'Simmons', 'evan.simmons@example.com'),
(33, 'Madison', 'Russell', 'madison.russell@example.com'),
(34, 'Dylan', 'Griffin', 'dylan.griffin@example.com'),
(35, 'Kayla', 'Diaz', 'kayla.diaz@example.com'),
(36, 'Aaron', 'Harrison', 'aaron.harrison@example.com'),
(37, 'Taylor', 'Morgan', 'taylor.morgan@example.com'),
(38, 'Logan', 'Fisher', 'logan.fisher@example.com'),
(39, 'Jordan', 'Woods', 'jordan.woods@example.com'),
(40, 'Kelsey', 'Cruz', 'kelsey.cruz@example.com'),
(41, 'Jared', 'Hayes', 'jared.hayes@example.com'),
(42, 'Vanessa', 'Barnes', 'vanessa.barnes@example.com'),
(43, 'Timothy', 'Gordon', 'timothy.gordon@example.com'),
(44, 'Alexandra', 'Reed', 'alexandra.reed@example.com'),
(45, 'Seth', 'Wells', 'seth.wells@example.com'),
(46, 'Hannah', 'Sanders', 'hannah.sanders@example.com'),
(47, 'Austin', 'Coleman', 'austin.coleman@example.com'),
(48, 'Alyssa', 'Powell', 'alyssa.powell@example.com'),
(49, 'Nathan', 'Wagner', 'nathan.wagner@example.com'),
(50, 'Sydney', 'Fuller', 'sydney.fuller@example.com');

INSERT INTO sport (id, sport_name)
VALUES
(01, 'Basketball'),
(02, 'Soccer'),
(03, 'Volleyball'),
(04, 'Tennis'),
(05, 'Baseball'),
(06, 'Softball'),
(07, 'Swimming');

INSERT INTO leagues (id, league_name)
VALUES
(001, 'A-league'),
(002, 'B-league');

INSERT INTO seasons (id, season_name)
VALUES
(0001, 'fall'),
(0002, 'winter'),
(0003, 'spring'),
(0004, 'summer');


INSERT INTO teams (id, team_name)
VALUES
(100, 'Team A'),
(101, 'Team B'),
(102, 'Team C'),
(103, 'Team D'),
(104, 'Team E'),
(105, 'Team F'),
(106, 'Team G');

INSERT INTO matches (id, matchup, date, seasons_id, sport_id, leagues_id)
VALUES
(201, 'A vs B', '2023-11-23 14:00:00', 201, 202, 203),
(202, 'B vs C', '2023-11-24 15:30:00', 202, 203, 204),
(203, 'Match 3', '2023-11-25 13:45:00', 203, 204, 205),
(204, 'Match 4', '2023-11-26 16:15:00', 204, 205, 206),
(205, 'Match 5', '2023-11-27 11:00:00', 205, 206, 207),
(206, 'Match 6', '2023-11-28 14:45:00', 206, 207, 208),
(207, 'Match 7', '2023-11-29 17:30:00', 207, 208, 209);
