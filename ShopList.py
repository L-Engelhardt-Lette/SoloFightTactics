import pygame
from Game import Game
from PlayerList import Player
from UnitsList import Unit, Warrior, ADC, Assasine, Mage

# Bekommt die unit listen vom Game
class Shop:
    def __init__(self, game):
        self.unitlist = game.unitlist

        #warrior_unitlist = []
        #for warrior in self.unitlist:
            #warrior_unitlist.append(warrior)

        #adc_unitlist = []
        #for adc in self.unitlist:
            #adc_unitlist.append(adc)

    def buy_unit(self, unit, player):
        if player.spend_gold(unit.cost):
            player.add_unit(unit)
            self.unitlist.remove(unit)       

    def sell_unit(self, unit, player):
        player.remove_unit(unit)
        self.unitlist.append(unit)