import csv
import random
 
# Read in team 1 stats from CSV file
with open('team1.csv') as f:
    reader = csv.DictReader(f)
    team1_stats = list(reader)
 
# Read in team 2 stats from CSV file
with open('team2.csv') as f:
    reader = csv.DictReader(f)
    team2_stats = list(reader)
 
# Simulate an at-bat
def simulate_at_bat(batter_stats, pitcher_stats):
    # Determine the probability of each outcome based on the players' stats
    hit_prob = int(batter_stats['hits']) / int(batter_stats['at_bats'])
    strike_prob = int(pitcher_stats['strikeouts']) / int(pitcher_stats['innings_pitched'])
    walk_prob = int(batter_stats['walks']) / int(batter_stats['plate_appearances'])
    hit_allowed_prob = int(pitcher_stats['hits_allowed']) / int(pitcher_stats['batters_faced'])
    walk_allowed_prob = int(pitcher_stats['walks_allowed']) / int(pitcher_stats['batters_faced'])
    run_allowed_prob = int(pitcher_stats['runs_allowed']) / int(pitcher_stats['innings_pitched'])
 
    # Randomly determine the outcome of the at-bat
    outcome = random.choices(['hit', 'strikeout', 'walk'], [hit_prob, strike_prob, walk_prob])[0]
 
    # Update pitcher stats based on the outcome
    if outcome == 'hit':
        pitcher_stats['hits_allowed'] += 1
        if random.random() < hit_allowed_prob:
            pitcher_stats['runs_allowed'] += 1
    elif outcome == 'walk':
        pitcher_stats['walks_allowed'] += 1
        if random.random() < walk_allowed_prob:
            pitcher_stats['runs_allowed'] += 1
    else:
        if random.random() < run_allowed_prob:
            pitcher_stats['runs_allowed'] += 1
 
    return outcome
 
# Simulate a game
def simulate_game(team1_stats, team2_stats):
    # Set up game state
    inning = 1
    outs = 0
    runs = 0
    team1_score = 0
    team2_score = 0
 
    # Choose starting pitchers
    team1_pitcher = random.choice(team1_stats)
    team2_pitcher = random.choice(team2_stats)
 
    # Simulate each inning
    while inning <= 9:
        # Simulate each at-bat
        while outs < 3:
            # Determine which team is at bat
            if inning % 2 == 1:
                batting_team_stats = team1_stats
                pitching_team_stats = team2_pitcher
            else:
                batting_team_stats = team2_stats
                pitching_team_stats = team1_pitcher
 
            # Choose a batter
            batter = random.choice(batting_team_stats)
 
            # Simulate the at-bat
            outcome = simulate_at_bat(batter, pitching_team_stats)
 
            # Update game state based on the outcome
            if outcome == 'hit':
                runs += 1
            elif outcome == 'strikeout':
                outs += 1
            elif outcome == 'walk':
                runs += 1
 
            # Check for end of inning