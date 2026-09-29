from pprint import pprint

# Premier League Football Match Analysis
# You are a programmer employed in an analytics company (     Omni Sport)
# Your job is to analyze match statistics to provide insights for team managers, sport jornalists, and interested fantasy football players.
# You are required to analyze from the latest game week.
# sport analytics companies use exact techniques to power platforms like FPL, Betting odds, tactical analysis

# The Problem
# We have goal data from 10 PL matches in a game week, and are required to:
# 1. Count how many goals each team scored.
# 2. Find the highest scoring teams and matches
# 3. Calculate goal statistics (average goals per match, most prolific teams)
# 4. Identify teams in good form vs struggling teams
# 5. Generate insights for pundicts and fantasy managers


#Solution breakdown
# data we need to store: Teams, scores

# Manchester United
# Chelsea
# Manchester City
# Arsenal
# Liverpool
# Tottenham
# Everton
# Newcastle
# Aston  Villa
# Brentford

# Home team
# Away team

# Home goals
# Away goals

# How many matches do we need? 10
# what calculations do we need? Maximum(highest scoring match, highest scoring teams), Average, minimum, total goals


matches = [
    {
        "match_id" : 1, 
        "home_team" : "Arsenal", 
        "home_goals" : 4,
        "away_team" : "Brentford",
        "away_goals" : 2
    },

    {
        "match_id" : 2, 
        "home_team" : "Chelsea", 
        "home_goals" : 0,
        "away_team" : "Manchester City",
        "away_goals" : 2
    },

    {
        "match_id" : 3, 
        "home_team" : "Aston villa", 
        "home_goals" : 2,
        "away_team" : "Tottenham",
        "away_goals" : 3
    }, 

    {
        "match_id" : 4, 
        "home_team" : "Newcastle", 
        "home_goals" : 4,
        "away_team" : "Everton",
        "away_goals" : 4
    }, 

    {
        "match_id" : 5, 
        "home_team" : "Liverpool", 
        "home_goals" : 0,
        "away_team" : "Manchester United",
        "away_goals" : 0
    },

    {
        "match_id" : 6, 
        "home_team" : "Brentford", 
        "home_goals" : 2,
        "away_team" : "Arsenal",
        "away_goals" : 2
    },

    {
        "match_id" : 7, 
        "home_team" : "Manchester City", 
        "home_goals" : 3,
        "away_team" : "Chelsea",
        "away_goals" : 2
    },

    {
        "match_id" : 8, 
        "home_team" : "Tottenham", 
        "home_goals" : 2,
        "away_team" : "Aston villa",
        "away_goals" : 1
    },

    {
        "match_id" : 9, 
        "home_team" : "Everton", 
        "home_goals" : 3,
        "away_team" : "Newcastle",
        "away_goals" : 2
    },

    {
        "match_id" : 10, 
        "home_team" : "Manchester United", 
        "home_goals" : 3,
        "away_team" : "Liverpool",
        "away_goals" : 3
    }
]


# pprint(matches)


team_goals = {}
total_goals = []
match_played = {}

for match in matches:
    home_teams = match["home_team"]
    away_teams = match["away_team"]
    home_goals = match["home_goals"]
    away_goals = match["away_goals"]
    
    if home_teams not in team_goals:
        team_goals[home_teams] = 0
    team_goals[home_teams] += home_goals
    


    if away_teams not in team_goals:
        team_goals[away_teams] = 0
    team_goals[away_teams] += away_goals

    home_and_away_goals = home_goals + away_goals
    
    print(home_and_away_goals)
    total_goals.append(home_and_away_goals)
    
pprint(team_goals)
print(total_goals)
sum_of_goals = sum(total_goals)
print(sum_of_goals)
print(len(matches))
average = sum_of_goals / len(matches)
print(average)
print(max(team_goals, key=team_goals.get))

highest_goals = 0
highest_match = None


for match in matches:
    match_goals = match["home_goals"] + match["away_goals"]

    if match_goals > highest_goals:
        highest_goals = match_goals
        highest_match = match
print("Highest scoring match:", 
      highest_match["home_team"],
      highest_match["home_goals"],
      "-",
      highest_match["away_goals"],
      highest_match["away_team"]
    )

highest_team_goals = 0
most_prolific_team = ""

for team, goals in team_goals.items():
    if goals > highest_team_goals:
        highest_team_goals = goals
        most_prolific_team = team
print("Most prolific team:", 
      most_prolific_team)
print("Goals Scored:",
      highest_team_goals)


for match in matches:
    if home_teams not in match_played:
        match_played[home_teams] = 0

    if away_teams not in match_played:
        match_played[away_teams] = 0

        match_played[home_teams] += 1
        match_played[away_teams] += 1



for team, goals in team_goals.items():
    average = goals / match_played[team]
    print(team, average)



