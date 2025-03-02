import psycopg2 as pg
import pandas as pd

def sql_query(query: str):
    with pg.connect(host='localhost', port=5432, dbname='LahmanDataBase', user='postgres') as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        rows=cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        resulting_df = pd.DataFrame(rows, columns=columns)
    
    return resulting_df

pitching_query = '''
            SELECT p.playerid as "player",
                sum(p.ER) AS "earned_runs",
                sum(p.IPouts) / 3 AS "innings_pitched",
                sum(p.H) AS "H_P",
                sum(p.SO) AS "SO_P",
                sum(p.ERA) AS "ERA",
                sum(p.BFP) AS "batters_faced",
                sum(p.BAOpp) AS "Opp_BA",
                sum(p.BB) AS "BB_P",
                sum(p.HR) AS "HR_P",
                sum(p.HBP) AS "HBP_P",
                sum(p.G) AS "G_P",
                p.yearID AS "year"
                
                FROM pitching as p

                INNER JOIN people as peo ON p.playerID = peo.playerID
                
                WHERE p.yearID > 2020 and p.teamID = 'PHI'

                GROUP BY p.playerid, p.yearID, peo.nameFirst, peo.nameLast

                ORDER BY innings_pitched DESC
                
                LIMIT 5;
'''
curr_teams_query = '''
                SELECT t.teamidbr as "Team", 
                t.name as "Name",
                t.W as "Wins",
                t.L as "Losses",
                ROUND(t.W::decimal / (t.W + t.L),3) as "Winning %",
                t.BPF as "3Yr B PF",
                t.PPF as "3Yr P PF",
                t.yearID
                
                FROM teams as t

                WHERE t.yearID >= 2022

                ORDER BY t.W DESC               
                
                    '''
batting_query = '''
            SELECT peo.nameFirst as "First Name",
                peo.nameLast as "Last Name",
                b.playerid as "player",
                sum(b.H) AS "H",
                sum(b.SO) AS "SO",
                sum(b.H - (b.H2B + b.H3B + b.HR)) AS "singles",
                sum(b.H2B) AS "doubles",
                sum(b.H3B) AS "triples",
                sum(b.HR) AS "HR",
                sum(b.AB) AS "AB",
                sum(b.BB) AS "BB",
                sum(b.HBP) AS "HBP",
                sum(b.SF) AS "SF",
                sum(b.G) AS "G",
                b.yearID AS "year"
                
                FROM batting as b

                INNER JOIN people as peo ON b.playerID = peo.playerID
                
                WHERE b.yearID > 2020 and b.teamID = 'PHI' and b.AB > 100

                GROUP BY b.playerid, b.yearID, peo.nameFirst, peo.nameLast

                ORDER BY triples DESC
                
                LIMIT 5;         
                '''

Phils_SP_query = '''
                SELECT 
                    pitching.*, 
                    peo.nameFirst || ' ' || peo.nameLast AS "Full Name" 
                FROM 
                    pitching 
                INNER JOIN 
                    people AS peo ON pitching.playerID = peo.playerID 
                WHERE 
                    pitching.teamid = 'PHI' 
                    AND pitching.yearid >= 2022 
                    AND pitching.gs > 10;        
                '''
SP_query = '''
                WITH Pitchers_2022 AS (
                    SELECT
                        p.playerID,
                        STRING_AGG(p.teamID, ' / ') AS teams2022,
                        SUM(p.GS) AS GS2022,
                        AVG(p.era) AS ERA2022
                    FROM
                        pitching AS p
                    WHERE
                        p.yearID = 2022
                    GROUP BY
                        p.playerID
                    HAVING
                        SUM(p.GS) >= 7
                ),
                Pitchers_2023 AS (
                    SELECT
                        p.playerID,
                        STRING_AGG(p.teamID, ' / ') AS teams2023,
                        SUM(p.GS) AS GS2023,
                        AVG(p.era) AS ERA2023
                    
                    FROM
                        pitching AS p
                    WHERE
                        p.yearID = 2023
                    GROUP BY
                        p.playerID
                    HAVING
                        SUM(p.GS) >= 7
                )
                SELECT
                    peo.nameFirst || ' ' || peo.nameLast AS "Full Name",
                    p2022.teams2022 AS "Teams 2022",
                    p2022.GS2022 AS "Games Started 2022",
                    p2022.ERA2022 AS "ERA 2022",
                    p2023.teams2023 AS "Teams 2023",
                    p2023.GS2023 AS "Games Started 2023",
                    p2023.ERA2023 AS "ERA 2023",
                    ROUND((p2023.ERA2023 - p2022.ERA2022)::numeric,3) AS "ERA CHANGE YOY"
                FROM
                    Pitchers_2022 AS p2022
                INNER JOIN
                    Pitchers_2023 AS p2023 ON p2022.playerID = p2023.playerID
                INNER JOIN
                    people AS peo ON p2022.playerID = peo.playerID;    
                '''