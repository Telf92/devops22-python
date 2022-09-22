# EXTRA - Base class

import random

class Person: # 1.
    def __init__(self, name, year):
        self.name = name # i.
        self.year = year # ii.

class Player(Person):
    def __init__(self, name, year, stats):
        super().__init__(name, year)
        self.stats = stats # 2. i. ii. iii.
    
    def __str__(self):
        return f"{self.name} [{self.year}] - {self.stats}"

class Coach(Person): # 3.
    def __init__(self, name, year, voice):
        super().__init__(name, year)
        self.voice = voice

    def __str__(self):
        return self.name

class Team:
    def __init__(self, players, coach):
        self.players = players # 4. i.
        self.coach = coach # ii.

    def summarize_team(self): # iii.
        team = """
-------------------------------------
-------------- My team --------------
-------------------------------------
"""
        team += f"Coach {self.coach}\n"
        team += "-------------- Players --------------\n"
        team += "\n".join(map(str, self.players))
        return team

def get_random_stats():
    return (
        random.randint(1, 10),
        random.randint(1, 10),
        random.randint(1, 10))

def main():
    coach = Coach("Pelle", 1959, 5)

    players = []
    for name in ["lisa", "eva", "petra", "linda", "amanda", "jonna", "malin", "fredrika", "frida", "jenny"]:
        year = random.randint(1987, 2004)
        players.append(Player(name, year, get_random_stats()))

    team = Team(players, coach)
    print(team.summarize_team())

if __name__ == '__main__':
    main()