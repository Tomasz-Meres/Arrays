computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V",
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]
sorted_games = sorted(computer_games)
n = 1

while len(sorted_games) - n >= 0:
    print(f'{n}.', end=' ')
    print(sorted_games[n-1])
    n += 1
