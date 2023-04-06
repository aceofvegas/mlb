import random
 
# Team stats
team1_stats = {'hits': 1200, 'at_bats': 5000, 'runs': 600, 'innings_pitched':1500, 'plate_appearances':5000, 'strikeouts':1500, 'walks': 1500}
team2_stats = {'hits': 1300, 'at_bats': 5500, 'runs': 650, 'innings_pitched':1500, 'plate_appearances':5000, 'strikeouts':1500, 'walks': 1500}
 
print(team1_stats)
print(team2_stats)

# Simulate an at-bat
def simulate_at_bat(batter_stats, pitcher_stats):
    # Determine the probability of each outcome based on the players' stats
    hit_prob = batter_stats['hits'] / batter_stats['at_bats']
    strike_prob = pitcher_stats['strikeouts'] / pitcher_stats['innings_pitched']
    walk_prob = batter_stats['walks'] / batter_stats['plate_appearances']
    # Normalize the probabilities
    total_prob = hit_prob + strike_prob + walk_prob
    hit_prob /= total_prob
    strike_prob /= total_prob
    walk_prob /= total_prob

    # Randomly determine the outcome of the at-bat
    outcome = random.choices(['hit', 'strikeout', 'walk'], [hit_prob, strike_prob, walk_prob])[0]
    #print(outcome)
    return outcome
 
# Simulate a game
def simulate_game(team1_stats, team2_stats):
    # Set up game state
    inning_num = 1 # Use a different variable name for the inning number
    outs = 0
    inning_runs = 0 # Use a different variable name for the runs scored in each inning
    team1_score = 0
    team2_score = 0
 
    # Simulate each inning
    while inning_num <= 9:
        # Simulate each at-bat
        while outs < 3:
            # Determine which team is at bat
            if inning_num % 2 == 1:
                batting_team_stats = team1_stats
                pitching_team_stats = team2_stats
            else:
                batting_team_stats = team2_stats
                pitching_team_stats = team1_stats
 
            # Simulate the at-bat
            outcome = simulate_at_bat(batting_team_stats, pitching_team_stats)
 
            # Update game state based on the outcome
            if outcome == 'hit':
                inning_runs += 1
            elif outcome == 'strikeout':
                outs += 1
            elif outcome == 'walk':
                inning_runs += 1
            print("outs ==" +str(outs))
            print("inning is "+str(inning_num))
 
            # Check for end of inning
            if outs == 3:
                if inning_num % 2 == 1:
                    team1_score += inning_runs
                else:
                    team2_score += inning_runs
                outs = 0
                inning_runs = 0
        
        # Increment the inning number after each half-inning
                inning_num += 1 # Move this statement outside of the if statement and indent it properly
                break
        print(inning_num)
    print("shit")

    # print scores
    print("Team 1: " + str(team1_score))
    print("Team 2: " + str(team2_score))
 
    # Determine the winner
    if team1_score > team2_score:
        return 'Team 1 wins!'
    elif team2_score > team1_score:
        return 'Team 2 wins!'
    else:
        return 'It\'s a tie!'
 
# Run the simulation
result = simulate_game(team1_stats, team2_stats)
print(result)