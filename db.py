import pymongo
from football_classes import *

client = pymongo.MongoClient('192.168.112.103')
database = client['22304']
teams = database["korzhuk-teams"]
games = database["korzhuk-games"]

print(database.list_collection_names())


def create_team(name: str, city: str, coach : str, players : list, reserve_players : list) -> None:
    team = {"name": name, "city" : city, "coach": coach, "players": players, "reserve_players": reserve_players}
    teams.insert_one(team)

def create_game(date: str, score: str, cards: list, goals: list, penalties: list, tries: list) -> None:
    game = {"date": date, "score": score, "cards":cards, "goals": goals, "penalties":penalties, "tries": tries}
    games.insert_one(game)

if __name__ == "__main__":
    