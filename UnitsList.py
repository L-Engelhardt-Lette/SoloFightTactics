import imp
from tkinter import image_types
from typing import Any
import pygame
import random
# import Game

grid_size = 10
cell_size = 1920 // grid_size

# Unit Class
class Unit:
    def __init__(self, name, health, cost, attack_damage, ability, position, image_path):
        self.name = name
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (cell_size, cell_size))
        #self.rect = image.get_rect()
        self.cost = cost
        self.position = position

        #combat stats
        self.health = health
        self.mana = 0
        self.attack_damage = attack_damage
        self.ability = ability

        #Am Anfang sind die Units immer am Leben
        self.is_alive = True

    def move(self, new_position):
        self.position = new_position   

    def attack(self, target):
        if self.mana == 100:
            return self.ability
        else :
            self.attack_damage
            self.mana += 5
        target.take_damage(self.attack_damage)
        if not self.is_alive:
            return

    def take_damage(self, damage):
        self.health -= damage
        if self.health <=0:
            self.is_alive = False
    
    def __call__(self, target_position) :
        self.move(target_position)

class Warrior(Unit):
    def __init__(self, name, health, cost, attack_damage, ability, position, image_path):
        super().__init__(name, health, cost, attack_damage, ability, position, image_path)

class Mage(Unit):
    def __init__(self, name, health, cost, attack_damage, ability, position, image_path):
        super().__init__(name, health, cost, attack_damage, ability, position, image_path)

class Tank(Unit):
    def __init__(self, name, health, cost, attack_damage, ability, position, image_path):
        super().__init__(name, health, cost, attack_damage, ability, position, image_path)

class ADC(Unit):
    def __init__(self, name, health, cost, attack_damage, ability, position, image_path):
        super().__init__(name, health, cost, attack_damage, ability, position, image_path)

class Healer(Unit):
    def __init__(self, name, health, cost, attack_damage, ability, position, image_path):
        super().__init__(name, health, cost, attack_damage, ability, position, image_path)

#warrior_list = []
#for i in range(10):
    #warrior_list.append(Warrior(name, health, cost, attack_damage, ability, position, image_path))

