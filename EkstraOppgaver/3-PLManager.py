import random

teams = {
    "Arsenal": {
        "players": {
            "Pierre-Emerick Aubameyang": {"position": "Forward", "goals": 0},
            "Bukayo Saka": {"position": "Forward", "goals": 0},
            "Thomas Partey": {"position": "Midfield", "goals": 0},
            "Kieran Tierney": {"position": "Defense", "goals": 0},
            "Ben White": {"position": "Defense", "goals": 0},
            "Bernd Leno": {"position": "Goalkeeper", "goals": 0},
            "Hector Bellerin": {"position": "Defense", "goals": 0},
            "Granit Xhaka": {"position": "Midfield", "goals": 0},
            "Emile Smith Rowe": {"position": "Midfield", "goals": 0},
            "Gabriel Magalhães": {"position": "Defense", "goals": 0},
            "Albert Sambi Lokonga": {"position": "Midfield", "goals": 0}
        },
        "victories": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_against": 0,
        "difference": 0,
        "points": 0,
        },

    "Aston Villa": {
        "players": {
            "Ollie Watkins": {"position": "Forward", "goals": 0},
            "Emiliano Buendia": {"position": "Midfield", "goals": 0},
            "Tyrone Mings": {"position": "Defense", "goals": 0},
            "Matt Targett": {"position": "Defense", "goals": 0},
            "Emiliano Martinez": {"position": "Goalkeeper", "goals": 0},
            "John McGinn": {"position": "Midfield", "goals": 0},
            "Danny Ings": {"position": "Forward", "goals": 0},
            "Ezri Konsa": {"position": "Defense", "goals": 0},
            "Ashley Young": {"position": "Midfield", "goals": 0},
            "Douglas Luiz": {"position": "Midfield", "goals": 0},
            "Leon Bailey": {"position": "Forward", "goals": 0},
            },
        "victories": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_against": 0,
        "difference": 0,
        "points": 0,
        },

    "Brentford": {
        "players": {
            "Ivan Toney": {"position": "Forward", "goals": 0},
            "Said Benrahma": {"position": "Forward", "goals": 0},
            "Christian Norgaard": {"position": "Midfield", "goals": 0},
            "Pontus Jansson": {"position": "Defense", "goals": 0},
            "David Raya": {"position": "Goalkeeper", "goals": 0},
            "Mathias Jensen": {"position": "Midfield", "goals": 0},
            "Mads Bech Sorensen": {"position": "Defense", "goals": 0},
            "Sergi Canos": {"position": "Forward", "goals": 0},
            "Charlie Goode": {"position": "Defense", "goals": 0},
            "Josh Dasilva": {"position": "Midfield", "goals": 0},
            "Rico Henry": {"position": "Defense", "goals": 0},
        },
        "victories": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_against": 0,
        "difference": 0,
        "points": 0,
        },

    "Brighton & Hove Albion": {
        "players": {
            "Neal Maupay": {"position": "Forward", "goals": 0},
            "Leandro Trossard": {"position": "Forward", "goals": 0},
            "Yves Bissouma": {"position": "Midfield", "goals": 0},
            "Adam Webster": {"position": "Defense", "goals": 0},
            "Robert Sánchez": {"position": "Goalkeeper", "goals": 0},
            "Lewis Dunk": {"position": "Defense", "goals": 0},
            "Joel Veltman": {"position": "Defense", "goals": 0},
            "Solly March": {"position": "Midfield", "goals": 0},
            "Pascal Groß": {"position": "Midfield", "goals": 0},
            "Tariq Lamptey": {"position": "Defense", "goals": 0},
            "Enock Mwepu": {"position": "Midfield", "goals": 0},
        },
        "victories": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_against": 0,
        "difference": 0,
        "points": 0,
    },
    "Burnley": {
        "players": {
            "Chris Wood": {"position": "Forward", "goals": 0},
            "Ashley Westwood": {"position": "Midfield", "goals": 0},
            "Ben Mee": {"position": "Defense", "goals": 0},
            "James Tarkowski": {"position": "Defense", "goals": 0},
            "Nick Pope": {"position": "Goalkeeper", "goals": 0},
            "Josh Brownhill": {"position": "Midfield", "goals": 0},
            "Erik Pieters": {"position": "Defense", "goals": 0},
            "Dwight McNeil": {"position": "Midfield", "goals": 0},
            "Matt Lowton": {"position": "Defense", "goals": 0},
            "Jay Rodriguez": {"position": "Forward", "goals": 0},
            "Charlie Taylor": {"position": "Defense", "goals": 0},
        },
        "victories": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_against": 0,
        "difference": 0,
        "points": 0,
    },

    "Chelsea": {
        "players": {
            "Romelu Lukaku": {"position": "Forward", "goals": 0},
            "Kai Havertz": {"position": "Forward", "goals": 0},
            "N'Golo Kanté": {"position": "Midfield", "goals": 0},
            "Andreas Christensen": {"position": "Defense", "goals": 0},
            "Édouard Mendy": {"position": "Goalkeeper", "goals": 0},
            "Mason Mount": {"position": "Midfield", "goals": 0},
            "César Azpilicueta": {"position": "Defense", "goals": 0},
            "Jorginho": {"position": "Midfield", "goals": 0},
            "Ben Chilwell": {"position": "Defense", "goals": 0},
            "Thiago Silva": {"position": "Defense", "goals": 0},
            "Timo Werner": {"position": "Forward", "goals": 0},
        },
        "victories": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_against": 0,
        "difference": 0,
        "points": 0,
    },

    "Crystal Palace": {
        "players": {
            "Wilfried Zaha": {"position": "Forward", "goals": 0},
            "Eberechi Eze": {"position": "Midfield", "goals": 0},
            "Cheikhou Kouyaté": {"position": "Midfield", "goals": 0},
            "Joel Ward": {"position": "Defense", "goals": 0},
            "Vicente Guaita": {"position": "Goalkeeper", "goals": 0},
            "Connor Gallagher": {"position": "Midfield", "goals": 0},
            "Marc Guehi": {"position": "Defense", "goals": 0},
            "Christian Benteke": {"position": "Forward", "goals": 0},
            "Luka Milivojevic": {"position": "Midfield", "goals": 0},
            "Tyrick Mitchell": {"position": "Defense", "goals": 0},
            "Odsonne Édouard": {"position": "Forward", "goals": 0},
        },
        "victories": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_against": 0,
        "difference": 0,
        "points": 0,
    },

    "Everton": {
        "players": {
            "Dominic Calvert-Lewin": {"position": "Forward", "goals": 0},
            "Richarlison": {"position": "Forward", "goals": 0},
            "Abdoulaye Doucouré": {"position": "Midfield", "goals": 0},
            "Michael Keane": {"position": "Defense", "goals": 0},
            "Jordan Pickford": {"position": "Goalkeeper", "goals": 0},
            "Andros Townsend": {"position": "Midfield", "goals": 0},
            "Yerry Mina": {"position": "Defense", "goals": 0},
            "Gylfi Sigurðsson": {"position": "Midfield", "goals": 0},
            "Mason Holgate": {"position": "Defense", "goals": 0},
            "Demarai Gray": {"position": "Midfield", "goals": 0},
            "Ben Godfrey": {"position": "Defense", "goals": 0},
        },
        "victories": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_against": 0,
        "difference": 0,
        "points": 0,
    },

    "Fulham": {
        "players": {
            "Aleksandar Mitrović": {"position": "Forward", "goals": 0},
            "Ivan Cavaleiro": {"position": "Forward", "goals": 0},
            "Tom Cairney": {"position": "Midfield", "goals": 0},
            "Tosin Adarabioyo": {"position": "Defense", "goals": 0},
            "Alphonse Areola": {"position": "Goalkeeper", "goals": 0},
            "Kenny Tete": {"position": "Defense", "goals": 0},
            "Harrison Reed": {"position": "Midfield", "goals": 0},
            "Ademola Lookman": {"position": "Forward", "goals": 0},
            "Joe Bryan": {"position": "Defense", "goals": 0},
            "Michael Hector": {"position": "Defense", "goals": 0},
            "Antonee Robinson": {"position": "Defense", "goals": 0},
        },
        "victories": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_against": 0,
        "difference": 0,
        "points": 0,
    },

    "Liverpool": {
        "players": {
            "Mohamed Salah": {"position": "Forward", "goals": 0},
            "Sadio Mané": {"position": "Forward", "goals": 0},
            "Roberto Firmino": {"position": "Forward", "goals": 0},
            "Diogo Jota": {"position": "Forward", "goals": 0},
            "Fabinho": {"position": "Midfield", "goals": 0},
            "Jordan Henderson": {"position": "Midfield", "goals": 0},
            "Andy Robertson": {"position": "Defense", "goals": 0},
            "Virgil van Dijk": {"position": "Defense", "goals": 0},
            "Joe Gomez": {"position": "Defense", "goals": 0},
            "Trent Alexander-Arnold": {"position": "Defense", "goals": 0},
            "Alisson Becker": {"position": "Goalkeeper", "goals": 0}
        },
        "victories": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_against": 0,
        "difference": 0,
        "points": 0,
    },

    "Luton": {
        "players": {
            "James Collins": {"position": "Forward", "goals": 0},
            "Harry Cornick": {"position": "Forward", "goals": 0},
            "Pelly-Ruddock Mpanzu": {"position": "Midfield", "goals": 0},
            "Sonny Bradley": {"position": "Defense", "goals": 0},
            "Simon Sluga": {"position": "Goalkeeper", "goals": 0},
            "Matty Pearson": {"position": "Defense", "goals": 0},
            "Elijah Adebayo": {"position": "Forward", "goals": 0},
            "Jordan Clark": {"position": "Midfield", "goals": 0},
            "Kal Naismith": {"position": "Defense", "goals": 0},
            "Kiernan Dewsbury-Hall": {"position": "Midfield", "goals": 0},
            "Tom Lockyer": {"position": "Defense", "goals": 0},
        },
        "victories": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_against": 0,
        "difference": 0,
        "points": 0,
    },

    "Manchester City": {
        "players": {
            "Kevin De Bruyne": {"position": "Midfield", "goals": 0},
            "Raheem Sterling": {"position": "Forward", "goals": 0},
            "Ruben Dias": {"position": "Defense", "goals": 0},
            "Ederson": {"position": "Goalkeeper", "goals": 0},
            "Phil Foden": {"position": "Midfield", "goals": 0},
            "John Stones": {"position": "Defense", "goals": 0},
            "Jack Grealish": {"position": "Midfield", "goals": 0},
            "Aymeric Laporte": {"position": "Defense", "goals": 0},
            "Riyad Mahrez": {"position": "Forward", "goals": 0},
            "Kyle Walker": {"position": "Defense", "goals": 0},
            "Rodri": {"position": "Midfield", "goals": 0},
        },
        "victories": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_against": 0,
        "difference": 0,
        "points": 0,
    },

    "Manchester United": {
        "players": {
            "Cristiano Ronaldo": {"position": "Forward", "goals": 0},
            "Marcus Rashford": {"position": "Forward", "goals": 0},
            "Mason Greenwood": {"position": "Forward", "goals": 0},
            "Bruno Fernandes": {"position": "Midfield", "goals": 0},
            "Paul Pogba": {"position": "Midfield", "goals": 0},
            "Scott McTominay": {"position": "Midfield", "goals": 0},
            "Luke Shaw": {"position": "Defense", "goals": 0},
            "Harry Maguire": {"position": "Defense", "goals": 0},
            "Raphael Varane": {"position": "Defense", "goals": 0},
            "Aaron Wan-Bissaka": {"position": "Defense", "goals": 0},
            "David de Gea": {"position": "Goalkeeper", "goals": 0}
        },
        "victories": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_against": 0,
        "difference": 0,
        "points": 0,
    },

    "Newcastle": {
        "players": {
            "Callum Wilson": {"position": "Forward", "goals": 0},
            "Allan Saint-Maximin": {"position": "Forward", "goals": 0},
            "Jonjo Shelvey": {"position": "Midfield", "goals": 0},
            "Jamal Lewis": {"position": "Defense", "goals": 0},
            "Martin Dubravka": {"position": "Goalkeeper", "goals": 0},
            "Isaac Hayden": {"position": "Midfield", "goals": 0},
            "Jamaal Lascelles": {"position": "Defense", "goals": 0},
            "Miguel Almirón": {"position": "Midfield", "goals": 0},
            "Ryan Fraser": {"position": "Midfield", "goals": 0},
            "Federico Fernández": {"position": "Defense", "goals": 0},
            "Ciaran Clark": {"position": "Defense", "goals": 0},
        },
        "victories": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_against": 0,
        "difference": 0,
        "points": 0,
    },

    "Nottingham Forest": {
        "players": {
            "Lewis Grabban": {"position": "Forward", "goals": 0},
            "Joe Lolley": {"position": "Forward", "goals": 0},
            "Ryan Yates": {"position": "Midfield", "goals": 0},
            "Joe Worrall": {"position": "Defense", "goals": 0},
            "Brice Samba": {"position": "Goalkeeper", "goals": 0},
            "Cafú": {"position": "Midfield", "goals": 0},
            "Scott McKenna": {"position": "Defense", "goals": 0},
            "Filip Krovinović": {"position": "Midfield", "goals": 0},
            "Alex Mighten": {"position": "Forward", "goals": 0},
            "Carl Jenkinson": {"position": "Defense", "goals": 0},
            "Loic Mbe Soh": {"position": "Defense", "goals": 0},
        },
        "victories": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_against": 0,
        "difference": 0,
        "points": 0,
    },
    "Sheffield United": {
        "players": {
            "Rhian Brewster": {"position": "Forward", "goals": 0},
            "John Fleck": {"position": "Midfield", "goals": 0},
            "John Egan": {"position": "Defense", "goals": 0},
            "Aaron Ramsdale": {"position": "Goalkeeper", "goals": 0},
            "George Baldock": {"position": "Defense", "goals": 0},
            "David McGoldrick": {"position": "Forward", "goals": 0},
            "Ethan Ampadu": {"position": "Midfield", "goals": 0},
            "Enda Stevens": {"position": "Defense", "goals": 0},
            "Sander Berge": {"position": "Midfield", "goals": 0},
            "Chris Basham": {"position": "Defense", "goals": 0},
            "Oliver Norwood": {"position": "Midfield", "goals": 0},
        },
        "victories": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_against": 0,
        "difference": 0,
        "points": 0,
    },
    "Tottenham": {
        "players": {
            "Harry Kane": {"position": "Forward", "goals": 0},
            "Heung-Min Son": {"position": "Forward", "goals": 0},
            "Dele Alli": {"position": "Midfield", "goals": 0},
            "Sergio Reguilón": {"position": "Defense", "goals": 0},
            "Hugo Lloris": {"position": "Goalkeeper", "goals": 0},
            "Eric Dier": {"position": "Defense", "goals": 0},
            "Lucas Moura": {"position": "Midfield", "goals": 0},
            "Davinson Sánchez": {"position": "Defense", "goals": 0},
            "Pierre-Emile Højbjerg": {"position": "Midfield", "goals": 0},
            "Giovani Lo Celso": {"position": "Midfield", "goals": 0},
            "Serge Aurier": {"position": "Defense", "goals": 0},
        },
        "victories": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_against": 0,
        "difference": 0,
        "points": 0,
    },

    "West Ham": {
        "players": {
            "Michail Antonio": {"position": "Forward", "goals": 0},
            "Declan Rice": {"position": "Midfield", "goals": 0},
            "Craig Dawson": {"position": "Defense", "goals": 0},
            "Łukasz Fabiański": {"position": "Goalkeeper", "goals": 0},
            "Jarrod Bowen": {"position": "Midfield", "goals": 0},
            "Vladimír Coufal": {"position": "Defense", "goals": 0},
            "Pablo Fornals": {"position": "Midfield", "goals": 0},
            "Ben Johnson": {"position": "Defense", "goals": 0},
            "Manuel Lanzini": {"position": "Midfield", "goals": 0},
            "Issa Diop": {"position": "Defense", "goals": 0},
            "Andriy Yarmolenko": {"position": "Forward", "goals": 0},
        },
        "victories": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_against": 0,
        "difference": 0,
        "points": 0,
    },

    "Wolverhampton": {
        "players": {
            "Raúl Jiménez": {"position": "Forward", "goals": 0},
            "Adama Traoré": {"position": "Forward", "goals": 0},
            "Rúben Neves": {"position": "Midfield", "goals": 0},
            "Rui Patrício": {"position": "Goalkeeper", "goals": 0},
            "Pedro Neto": {"position": "Midfield", "goals": 0},
            "Conor Coady": {"position": "Defense", "goals": 0},
            "João Moutinho": {"position": "Midfield", "goals": 0},
            "Nelson Semedo": {"position": "Defense", "goals": 0},
            "Daniel Podence": {"position": "Forward", "goals": 0},
            "Willy Boly": {"position": "Defense", "goals": 0},
            "Leander Dendoncker": {"position": "Midfield", "goals": 0},
        },
        "victories": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_against": 0,
        "difference": 0,
        "points": 0,
    },
}
available_teams = list(teams.keys())
all_teams = list(teams.keys())


def table():
    def custom_sort_key(team):
        return -team[1]["points"], team[1]["points"] - team[1]["goals_for"] + team[1]["goals_against"], team[1][
            "goals_for"], team[0]

    # Sorting the teams using the custom sorting key
    sorted_teams = sorted(teams.items(), key=custom_sort_key)

    table_str = "\nLeague Table:"
    table_str += f"\n{'Pos':<4}{'Team':<25}{'GP':<4}{'W':<4}{'D':<4}{'L':<4}{'GF':<4}{'GA':<4}{'GD':<4}{'Pts':<4}"

    for i, (team_name, stats) in enumerate(sorted_teams, start=1):
        games_played = stats['victories'] + stats['draws'] + stats['losses']
        table_str += (f"\n{i:<4}{team_name:<25}{games_played:<4}{stats['victories']:<4}"
                      f"{stats['draws']:<4}{stats['losses']:<4}"
                      f"{stats['goals_for']:<4}{stats['goals_against']:<4}"
                      f"{stats['goals_for'] - stats['goals_against']:<4}{stats['points']:<4}")

    return table_str


def display_table():
    print(table())


def pick_user_team():
    print("Select your team:")
    for i, team_name in enumerate(available_teams, start=1):
        print(f"{i}. {team_name}")

    while True:
        try:
            choice = int(input("Enter the number of your chosen team: "))
            if 1 <= choice <= len(available_teams):
                user_team = available_teams.pop(choice - 1)  # Remove and store the selected team
                return user_team
            else:
                print("Invalid team choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def pick_opponent():
    opponent = random.choice(available_teams)
    return opponent


def play_game(user_team, user_opponent):
    print(f"Match: {user_team} vs {user_opponent}")

    # Set up initial variables
    user_score = 0
    opponent_score = 0
    match_events = []
    time = 1  # Start at the first minute

    # Simulate the match
    while time <= 90:
        # Skip a random number of minutes (between 5 and 10 minutes)
        skip_minutes = random.randint(5, 10)
        time += skip_minutes

        if time > 90:
            break  # Stop the game if it's past 90 minutes

        # Simulate events (e.g., shots, goals, saves, etc.) here
        event_team = random.choice([user_team, user_opponent])
        event = random.choice(["missed", "hits the post", "saved", "scored"])
        player = random.choice(list(teams[event_team]["players"].keys()))

        # Check if the player's position is "goalkeeper"
        if teams[event_team]["players"][player]["position"] == "goalkeeper":
            event = "saved"  # Goalkeepers can only save, not score

        if event == "scored":
            if teams[event_team]["players"][player]["position"] != "goalkeeper":
                goalscorer = player
                teams[event_team]["players"][player]["goals"] += 1
                if event_team == user_team:
                    user_score += 1
                else:
                    opponent_score += 1
                match_events.append(f"{time}' {goalscorer} scored!")
        else:
            match_events.append(f"{time}' {player} {event}.")

    # Calculate the match result
    result = "draw"
    if user_score > opponent_score:
        result = "win"
    elif user_score < opponent_score:
        result = "loss"

    # Print match events
    print("\nMatch Updates:")
    for event in match_events:
        print(event)

    # Print final score
    print(f"\nFinal Score: {user_team} {user_score}-{opponent_score} {user_opponent}")

    # Update team statistics and points
    teams[user_team]["goals_for"] += user_score
    teams[user_team]["goals_against"] += opponent_score
    teams[user_opponent]["goals_for"] += opponent_score
    teams[user_opponent]["goals_against"] += user_score

    if result == "win":
        teams[user_team]["victories"] += 1
        teams[user_opponent]["losses"] += 1
    elif result == "loss":
        teams[user_team]["losses"] += 1
        teams[user_opponent]["victories"] += 1
    else:
        teams[user_team]["draws"] += 1
        teams[user_opponent]["draws"] += 1

    # Update points based on the match result
    if result == "win":
        teams[user_team]["points"] += 3
    elif result == "draw":
        teams[user_team]["points"] += 1
        teams[user_opponent]["points"] += 1
    else:
        teams[user_opponent]["points"] += 3


def simulate_game_result():
    # Simulate a game result
    home_goals = random.randint(0, 5)
    away_goals = random.randint(0, 5)
    return home_goals, away_goals


def simulate_remaining_games():
    # Calculate the total number of rounds needed for all teams to play the same number of games
    max_games = max([stats['victories'] + stats['draws'] + stats['losses'] for stats in teams.values()])
    total_rounds = max_games // 2

    # Simulate games for each round
    for round_num in range(total_rounds):
        # Create a list of matchups for this round
        matchups = []
        for i in range(1, len(teams) + 1):
            for j in range(i + 1, len(teams) + 1):
                matchups.append((i, j))

        # Simulate games for this round
        for matchup in matchups:
            home_team_num, away_team_num = matchup
            home_team = teams[home_team_num]
            away_team = teams[away_team_num]

            home_goals, away_goals = simulate_game_result()

            update_team_stats(home_team_num, home_goals, away_goals, away_team_num)

    print("All games simulated.")


def top_scorers():
    # Create a list of all players and their goal counts
    all_players = []
    for team_name, team_data in teams.items():
        for player_name, player_stats in team_data["players"].items():
            all_players.append((team_name, player_name, player_stats["goals"]))

    sorted_players = sorted(all_players, key=lambda x: x[2], reverse=True)

    print("\nTop Goal-Scorers:")
    print(f"{'Rank':<5}{'Player':<30}{'Goals'}")
    for rank, (team_name, player_name, goals) in enumerate(sorted_players[:20], start=1):
        print(f"{rank:<5}{player_name} ({team_name}): {goals}")


def player_stats():
    print("Select a team to view player stats:")
    for idx, team_name in enumerate(teams, start=1):
        print(f"{idx}. {team_name}")

    while True:
        try:
            choice = int(input("Enter the number of the team: "))
            if 1 <= choice <= len(teams):
                team_name = list(teams.keys())[choice - 1]
                break
            else:
                print("Invalid choice. Please select a valid team number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    team = teams[team_name]
    players = team["players"]
    print(f"Player stats for {team_name}:")
    print(f"{'Player':<25}{'Position':<15}{'Goals':<5}")
    for player, data in players.items():
        print(f"{player:<25}{data['position']:<15}{data['goals']:<5}")


def update_team_stats(home_team_num, home_goals, away_goals, away_team_num):
    teams[home_team_num]["victories"] += 1 if home_goals > away_goals else 0
    teams[home_team_num]["draws"] += 1 if home_goals == away_goals else 0
    teams[home_team_num]["losses"] += 1 if home_goals < away_goals else 0
    teams[home_team_num]["goals_for"] += home_goals
    teams[home_team_num]["goals_against"] += away_goals
    teams[home_team_num]["points"] = teams[home_team_num]["victories"] * 3 + teams[home_team_num]["draws"]

    teams[away_team_num]["victories"] += 1 if away_goals > home_goals else 0
    teams[away_team_num]["draws"] += 1 if away_goals == home_goals else 0
    teams[away_team_num]["losses"] += 1 if away_goals < home_goals else 0
    teams[away_team_num]["goals_for"] += away_goals
    teams[away_team_num]["goals_against"] += home_goals
    teams[away_team_num]["points"] = teams[away_team_num]["victories"] * 3 + teams[away_team_num]["draws"]


def simulate_remaining_matches(user_team_num, user_opponent_num):
    print("Simulating the remaining matches...")
    team_count = len(teams)

    for team_num in range(team_count):
        if team_num != user_team_num and team_num != user_opponent_num:
            home_goals, away_goals = simulate_game_result()
            update_team_stats(team_num, home_goals, away_goals, user_team_num)

    print("All remaining matches simulated.")


def main():
    print("Welcome to Premier League 2021 Manager!")

    user_team = pick_user_team()

    while True:
        choice = input(
            "Choose your next action: (P)lay a match, (S)imulate rest, (G)oal-scorers, (T)able,"
            " (I)ndividual Team Stats, (Q)uit: ").upper()

        if choice == 'P':
            user_opponent = pick_opponent()
            play_game(user_team, user_opponent)
        elif choice == 'S':
            user_team_num = pick_user_team()
            user_opponent_num = pick_opponent()
            simulate_remaining_matches(user_team_num, user_opponent_num)
        elif choice == 'G':
            top_scorers()
        elif choice == 'T':
            display_table()
        elif choice == 'I':
            player_stats()
        elif choice == 'Q':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
