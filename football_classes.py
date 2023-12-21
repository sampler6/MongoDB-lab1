class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position


class Card:
    def __init__(self, color, player_name, time):
        self.color = color
        self.player_name = player_name
        self.time = time


class Kick:
    def __init(self, field_position, time, author, support):
        self.field_position = field_position
        self.time = time
        self.author = author
        self.support = support


