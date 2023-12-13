import pygame
from UnitsList import Unit

# Player Class
class Player:
    def __init__(self):
        #stats
        self.health = 100
        self.level = 1
        self.experience = 0
        self.gold = 0

        #All units the player buys and has on the field
        self.player_units = []

        #checking for round-based Gameplay
        self.is_turn = False

    #Earn gold after every Round, set Amount
    def earn_gold(self, amount):
        self.gold += amount

    #Make it so a Player can spend Gold in the Shop
    def spend_gold(self, amount):
        if self.gold >= amount:
            self.gold -= amount
            return True
        return False
    
    #Make it so that Players have a Way to get experience Points
    def gain_experience(self, amount):
        self.experience += amount
        self.check_level_up()

    #Check if the Player gets a level up after a certain Amount of experience Points
    def check_level_up(self):
        level_up_cost = 5  # Gold cost per experience point
        while self.experience >= self.level * level_up_cost:
            self.level_up()   

    #Level the Player up for 1 level      
    def level_up(self):
        level_up_cost = 5  # Gold cost per experience point
        self.experience -= self.level * level_up_cost
        self.level += 1
        print(f"Leveled up to level {self.level}!")
    
    #Units can be added to the Players own Unit List
    def add_unit(self, Unit):
        self.player_units.append(Unit)

    #Units can be removed from the Players own Unit List
    def remove_unit(self, unit):
        self.player_units.remove(unit)    