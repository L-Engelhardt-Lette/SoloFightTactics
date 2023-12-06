import pygame

# Player Class
class Player:
    def __init__(self, health, player_units):
        self.health = health
        self.player_units = player_units
        self.is_turn = False