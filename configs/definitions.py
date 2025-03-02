import os
ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))

# Retrosheet contains data from teams who have moved/renamed. Therefore, some abbreviations differ from Lahman DB. This dict maps them
renamed_team = {
    'NYN': 'NYM',
    'CHA': 'CHW',
    'SFN': 'SFG',
    'ANA': 'LAA',
    'CHN': 'CHC',
    'TBA': 'TBR',
    'LAN': 'LAD',
    'SDN': 'SDP',
    'WAS': 'WSN',
    'SLN': 'STL',
    'KCA': 'KCR',
    'NYA': 'NYY',
}

game_log_column_headers = [
    "Date",
    "Game Number",
    "Day of Week",
    "Visiting Team",
    "Visiting Team League",
    "Visiting Team Game Number",
    "Home Team",
    "Home Team League",
    "Home Team Game Number",
    "Visiting Team Score",
    "Home Team Score",
    "Length of Game (Outs)",
    "Day/Night Indicator",
    "Park ID",
    "Attendance",
    "Time of Game",
    "Visiting SP",
    "Home SP"
]