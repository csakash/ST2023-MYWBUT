superheroes = {}
print(type(superheroes))

superheroes = {"Ironman": 10, "Thor": 9, "Spiderman": 8, "Hulk": 7.5}

print(superheroes["Ironman"])
print(superheroes["Thor"])
print(superheroes["Spiderman"])
print(superheroes["Hulk"])


"""
Team Ironman: Spiderman, Black Widow, War Machine
Team Captain America: Hawkeye, Groot, Antman
"""

teams = {
    "Team Ironman": [
        {"Spiderman": 8},
        {"Black Widow": 7.5},
        {"War Machine": 7}
    ],
    "Team Captain America": [
        {"Hawkeye": 6},
        {"Groot": 6.5},
        {"Antman": 7}
    ]
}

print(teams, type(teams))
print(teams["Team Ironman"], type(teams["Team Ironman"]))
print(teams["Team Ironman"][1], type(teams["Team Ironman"][1]))
print(teams["Team Ironman"][1]["Black Widow"], type(teams["Team Ironman"][1]["Black Widow"]))
print(teams["Team Captain America"])