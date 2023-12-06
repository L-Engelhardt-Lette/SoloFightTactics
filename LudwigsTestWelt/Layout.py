import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants for Game
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080


# Constants for the screen dimensions and grid
GRID_WIDTH = SCREEN_WIDTH - 310
GRID_HEIGHT = SCREEN_HEIGHT - 280
GRID_SIZE = (5, 8)  # 5 rows by 8 columns for both players combined
TILE_SIZE = (GRID_WIDTH // GRID_SIZE[1], GRID_HEIGHT // (GRID_SIZE[0] + 2))  # additional 2 rows for shop and info

# Constants for the shop tiles
SHOP_TILE_WIDTH = 310  # Width of each shop tile
SHOP_TILE_HEIGHT = 800 # Height of each shop tile
SHOP_UNIT_TILEHEIGHT = SHOP_TILE_HEIGHT / 5
SHOP_UNIT_TILEWIDTH = SHOP_TILE_WIDTH

# Constants for the Round Console tiles
ROUND_CONSOLE_TILE_WIDTH = 640
ROUND_CONSOLE_TILE_HEIGHT = 280

# Constants for the Player 1 Info tiles
PLAYER_ONE_INFO_WIDTH = 640
PLAYER_ONE_INFO_HEIGHT = 280

# Constants for the Player 2 Info tiles
PLAYER_TWO_INFO_WIDTH = 640
PLAYER_ONE_INFO_HEIGHT = 280

