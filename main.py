matches = [
    ["Real Madrid", "Athletic Club", 4, 2],
    ["Sevilla", "Real Madrid", 0, 1],
    ["Real Madrid", "Real Oviedo", 2, 0],
    ["Real Betis", "Real Madrid", 1, 1],
    ["Real Madrid", "Deportivo Alavés", 2, 1],
    ["Real Madrid", "Getafe", 0, 1]
]

team = "Real Madrid"


def analyze_team(matches, team):
    wins = 0
    draws = 0
    losses = 0
    goals_for = 0
    goals_against = 0

    for match in matches:
        home_team = match[0]
        away_team = match[1]
        home_goals = match[2]
        away_goals = match[3]

        if home_team == team:
            goals_for += home_goals
            goals_against += away_goals

            if home_goals > away_goals:
                wins += 1
            elif home_goals == away_goals:
                draws += 1
            else:
                losses += 1

        elif away_team == team:
            goals_for += away_goals
            goals_against += home_goals

            if away_goals > home_goals:
                wins += 1
            elif away_goals == home_goals:
                draws += 1
            else:
                losses += 1

    total_matches = wins + draws + losses
    points = wins * 3 + draws
    goal_difference = goals_for - goals_against

    win_rate = (wins / total_matches) * 100
    average_goals = goals_for / total_matches
    average_conceded = goals_against / total_matches

    return {
        "matches": total_matches,
        "wins": wins,
        "draws": draws,
        "losses": losses,
        "goals_for": goals_for,
        "goals_against": goals_against,
        "goal_difference": goal_difference,
        "points": points,
        "win_rate": win_rate,
        "average_goals": average_goals,
        "average_conceded": average_conceded
    }


stats = analyze_team(matches, team)


print("=" * 35)
print("       SPORTS DATA ANALYZER")
print("=" * 35)

print("Team:", team)
print("Matches:", stats["matches"])
print("Wins:", stats["wins"])
print("Draws:", stats["draws"])
print("Losses:", stats["losses"])
print("Goals for:", stats["goals_for"])
print("Goals against:", stats["goals_against"])
print("Goal difference:", stats["goal_difference"])
print("Points:", stats["points"])
print("Win rate:", round(stats["win_rate"], 2), "%")
print("Average goals:", round(stats["average_goals"], 2))
print("Average conceded:", round(stats["average_conceded"], 2))

print("=" * 35)