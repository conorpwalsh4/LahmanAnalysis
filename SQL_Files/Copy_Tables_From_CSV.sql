-- Moved Data Files To Public As Workaround for COPY Function Errors
--TODO: Allow for COPY to work on desired directory

BEGIN TRANSACTION;

COPY AllstarFull FROM 'C:\Users\Public\lahman_1871-2023_csv\AllstarFullv2.csv' WITH CSV HEADER DELIMITER AS ',';
COPY Appearances FROM 'C:\Users\Public\lahman_1871-2023_csv\Appearances.csv' WITH CSV HEADER DELIMITER AS ',';
COPY AwardsManagers FROM 'C:\Users\Public\lahman_1871-2023_csv\AwardsManagers.csv' WITH CSV HEADER DELIMITER AS ',';
COPY AwardsPlayers FROM 'C:\Users\Public\lahman_1871-2023_csv\AwardsPlayers.csv' WITH CSV HEADER DELIMITER AS ',';
COPY AwardsShareManagers FROM 'C:\Users\Public\lahman_1871-2023_csv\AwardsShareManagers.csv' WITH CSV HEADER DELIMITER AS ',';
COPY AwardsSharePlayers FROM 'C:\Users\Public\lahman_1871-2023_csv\AwardsSharePlayers.csv' WITH CSV HEADER DELIMITER AS ',';
COPY Batting FROM 'C:\Users\Public\lahman_1871-2023_csv\Batting.csv' WITH CSV HEADER DELIMITER AS ',';
COPY BattingPost FROM 'C:\Users\Public\lahman_1871-2023_csv\BattingPost.csv' WITH CSV HEADER DELIMITER AS ',';
COPY CollegePlaying FROM 'C:\Users\Public\lahman_1871-2023_csv\CollegePlaying.csv' WITH CSV HEADER DELIMITER AS ',';
COPY Fielding FROM 'C:\Users\Public\lahman_1871-2023_csv\Fielding.csv' WITH CSV HEADER DELIMITER AS ',';
COPY FieldingOF FROM 'C:\Users\Public\lahman_1871-2023_csv\FieldingOF.csv' WITH CSV HEADER DELIMITER AS ',';
COPY FieldingOFsplit FROM 'C:\Users\Public\lahman_1871-2023_csv\FieldingOFsplit.csv' WITH CSV HEADER DELIMITER AS ',';
COPY FieldingPost FROM 'C:\Users\Public\lahman_1871-2023_csv\FieldingPost.csv' WITH CSV HEADER DELIMITER AS ',';
COPY HallOfFame FROM 'C:\Users\Public\lahman_1871-2023_csv\HallOfFame.csv' WITH CSV HEADER DELIMITER AS ',';
COPY HomeGames FROM 'C:\Users\Public\lahman_1871-2023_csv\HomeGames.csv' WITH CSV HEADER DELIMITER AS ',';
COPY Managers FROM 'C:\Users\Public\lahman_1871-2023_csv\Managers.csv' WITH CSV HEADER DELIMITER AS ',';
COPY ManagersHalf FROM 'C:\Users\Public\lahman_1871-2023_csv\ManagersHalf.csv' WITH CSV HEADER DELIMITER AS ',';
COPY Parks FROM 'C:\Users\Public\lahman_1871-2023_csv\Parks.csv' WITH CSV HEADER DELIMITER AS ',';
COPY People FROM 'C:\Users\Public\lahman_1871-2023_csv\People.csv' WITH CSV HEADER DELIMITER AS ',';
COPY Pitching FROM 'C:\Users\Public\lahman_1871-2023_csv\Pitching.csv' WITH CSV HEADER DELIMITER AS ',';
COPY PitchingPost FROM 'C:\Users\Public\lahman_1871-2023_csv\PitchingPost.csv' WITH CSV HEADER DELIMITER AS ',';
COPY Salaries FROM 'C:\Users\Public\lahman_1871-2023_csv\Salaries.csv' WITH CSV HEADER DELIMITER AS ',';
COPY Schools FROM 'C:\Users\Public\lahman_1871-2023_csv\Schools.csv' WITH CSV HEADER DELIMITER AS ',';
COPY SeriesPost FROM 'C:\Users\Public\lahman_1871-2023_csv\SeriesPost.csv' WITH CSV HEADER DELIMITER AS ',';
COPY Teams FROM 'C:\Users\Public\lahman_1871-2023_csv\Teams.csv' WITH CSV HEADER DELIMITER AS ',';
COPY TeamsFranchises FROM 'C:\Users\Public\lahman_1871-2023_csv\TeamsFranchises.csv' WITH CSV HEADER DELIMITER AS ',';
COPY TeamsHalf FROM 'C:\Users\Public\lahman_1871-2023_csv\TeamsHalf.csv' WITH CSV HEADER DELIMITER AS ','; 

END TRANSACTION;