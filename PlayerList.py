import pygame

# Player Class
class Player:
    def __init__(self, player_units):
        #stats
        self.health = 100
        self.level = 1
        self.experience = 0
        self.gold = 0

        #All units the player buys and has on the field
        self.player_units = player_units
        #checking for round-based Gameplay
        self.is_turn = False

    def earn_gold(self, amount):
        self.gold += amount

    def spend_gold(self, amount):
        if self.gold >= amount:
            self.gold -= amount
            return True
        return False
    
    def gain_experience(self, amount):
        self.experience += amount
        self.check_level_up()

    def check_level_up(self):
        level_up_cost = 5  # Gold cost per experience point
        while self.experience >= self.level * level_up_cost:
            self.level_up()   
             
    def level_up(self):
        level_up_cost = 5  # Gold cost per experience point
        self.experience -= self.level * level_up_cost
        self.level += 1
        print(f"Leveled up to level {self.level}!")
        