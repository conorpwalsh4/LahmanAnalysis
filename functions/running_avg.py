import pandas as pd

# Function to calculate running average
def running_average(var, window_size=10):
    """
    Calculates Running average of a variable

    Parameters:
    var (pd.DataFrame): df of a log of all games.
    window_size (str): Amount of time to calculate over.

    Returns:
    np.Float: Running Avg result
    """
    if len(var) < window_size:
        return sum(var) / len(var)
    else:
        return sum(var[-window_size:]) / window_size


def get_running_avg_df(gamelogs_: pd.DataFrame, timeframe= 10):
    """
    Returns df appending running average of
    of runs per game where time is defined by timeframe variable.

    Parameters:
    gamelogs_ (pd.DataFrame): df of a log of all games.
    timeframe (str): The name of the column to normalize.

    Returns:
    pd.DataFrame: Including the running avg cols (raw and normalized).
    """
    gamelogs_ = gamelogs_.sort_values(by='Date', ascending=True)

    team_runs_scored = {team: [] for team in gamelogs_['Visiting Team'].unique()}
    team_runs_allowed = {team: [] for team in gamelogs_['Visiting Team'].unique()}

    # Loop through each row in the dataframe
    running_averages = []

    for index, row in gamelogs_.iterrows():
        visiting_team = row['Visiting Team']
        visiting_team_game_num = row['Visiting Team Game Number']
        home_team = row['Home Team']
        home_team_game_num = row['Home Team Game Number']
        visiting_score = row['Visiting Team Score']
        home_score = row['Home Team Score']
        
        # Update runs for visiting team
        team_runs_scored[visiting_team].append(visiting_score)
        team_runs_allowed[visiting_team].append(home_score)
        visiting_run_avg = running_average(team_runs_scored[visiting_team], window_size=timeframe)
        visiting_avg = running_average(team_runs_scored[visiting_team], window_size=len(team_runs_scored[visiting_team]))
        vis_allow_run_avg = running_average(team_runs_allowed[visiting_team], window_size=timeframe)
        vis_allow_avg = running_average(team_runs_allowed[visiting_team], window_size=len(team_runs_allowed[visiting_team]))

        # Update runs scored for home team
        team_runs_scored[home_team].append(home_score)
        team_runs_allowed[home_team].append(visiting_score)
        home_run_avg = running_average(team_runs_scored[home_team], window_size=timeframe)
        home_avg = running_average(team_runs_scored[home_team], window_size=len(team_runs_scored[visiting_team]))
        home_allow_run_avg = running_average(team_runs_allowed[home_team], window_size=timeframe)
        home_allow_avg = running_average(team_runs_allowed[home_team], window_size=len(team_runs_allowed[home_team]))
        
        # Append running averages to the list
        running_averages.append({
            'Date': row['Date'],
            'Visiting Team': visiting_team,
            'VTRA_S': visiting_run_avg,
            'VTA_S' : visiting_avg,
            'VTRA_A': vis_allow_run_avg,
            'VTA_A' : vis_allow_avg,
            'Home Team': home_team,
            'HTRA_S': home_run_avg,
            'HTA_S' : home_avg,
            'HTRA_A': home_allow_run_avg,
            'HTA_A' : home_allow_avg
        })

    # Convert the running averages list to a dataframe
    running_avg_df = pd.DataFrame(running_averages)
    running_avg_df['HTRA_Norm'] = min_max_norm(running_avg_df,'HTRA_S')
    running_avg_df['VTRA_Norm'] = min_max_norm(running_avg_df,'VTRA_S')

    return running_avg_df

def min_max_norm(data:pd.DataFrame, column_name:str):
    """
    Apply min-max normalization to a specified column in a dataframe.

    Parameters:
    df (pd.DataFrame): The dataframe containing the data.
    column_name (str): The name of the column to normalize.

    Returns:
    pd.Series: The normalized column.
    """
    min_val = data[column_name].min()
    max_val = data[column_name].max()
    #if min_val < 0:
    #    data[column_name] = data[column_name] + abs(min_val)
    normalized_column = (data[column_name] - min_val) / ((max_val - min_val) + 1e-6)
    
    return normalized_column

def calc_total_rpg(gamelogs_:pd.DataFrame):
    """
    Returns a dict of average runs per game, as well
    as runs allowed per game.

    Parameters:
    gamelogs_ (pd.DataFrame): df of a log of all games.

    Returns:
    Dict: average_runs_scored
    Dict: average_runs_allowed
    """
    # Initialize dictionaries to store total runs scored and runs allowed for each team
    runs_scored = {}
    runs_allowed = {}
    games_played = {}

    # Loop through each row in the dataframe
    for index, row in gamelogs_.iterrows():
        visiting_team = row['Visiting Team']
        home_team = row['Home Team']
        visiting_score = row['Visiting Team Score']
        home_score = row['Home Team Score']
        
        # Update runs scored and allowed for visiting team
        if visiting_team not in runs_scored:
            runs_scored[visiting_team] = 0
            runs_allowed[visiting_team] = 0
            games_played[visiting_team] = 0
        
        runs_scored[visiting_team] += visiting_score
        runs_allowed[visiting_team] += home_score
        games_played[visiting_team] += 1
        
        # Update runs scored and allowed for home team
        if home_team not in runs_scored:
            runs_scored[home_team] = 0
            runs_allowed[home_team] = 0
            games_played[home_team] = 0
        
        runs_scored[home_team] += home_score
        runs_allowed[home_team] += visiting_score
        games_played[home_team] += 1

    # Calculate average runs scored and allowed per game for each team
    average_runs_scored = {team: runs_scored[team] / games_played[team] for team in runs_scored}
    average_runs_allowed = {team: runs_allowed[team] / games_played[team] for team in runs_allowed}

    """ # Display the results
    print("Average Runs Scored per Game:")
    for team, avg_runs in average_runs_scored.items():
        print(f"{team}: {avg_runs:.2f}")

    print("\nAverage Runs Allowed per Game:")
    for team, avg_runs in average_runs_allowed.items():
        print(f"{team}: {avg_runs:.2f}") """

    return average_runs_scored, average_runs_allowed

