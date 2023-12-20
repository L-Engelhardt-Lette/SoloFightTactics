import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants for Game
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# Constants for the screen dimensions and grid
GRID_WIDTH = SCREEN_WIDTH - 620  # Reduced width to accommodate two shops
GRID_HEIGHT = SCREEN_HEIGHT - 280
GRID_SIZE = (5, 8)  # 5 rows by 8 columns for both players combined
TILE_SIZE = (GRID_WIDTH // GRID_SIZE[1], GRID_HEIGHT // (GRID_SIZE[0] + 1))  # additional 2 rows for shop and info

# Constants for the shop tiles
SHOP_TILE_WIDTH = 310  # Width of each shop tile
SHOP_TILE_HEIGHT = 800  # Height of each shop tile
SHOP_UNIT_TILE_HEIGHT = SHOP_TILE_HEIGHT / 5
SHOP_UNIT_TILE_WIDTH = SHOP_TILE_WIDTH
SHOP_GRID_COL = 1
SHOP_GRID_ROW = 5

# Constants for the Round Console tiles
ROUND_CONSOLE_TILE_WIDTH = 640
ROUND_CONSOLE_TILE_HEIGHT = 280

# Constants for the Player 1 Info tiles
PLAYER_ONE_INFO_WIDTH = 640
PLAYER_ONE_INFO_HEIGHT = 280

# Constants for the Player 2 Info tiles
PLAYER_TWO_INFO_WIDTH = 640
PLAYER_TWO_INFO_HEIGHT = 280

# Initialize Pygame screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Rectangles Example')

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Create and draw rectangles with different colors
rectangles = [
    pygame.Rect(0, 0, SHOP_TILE_WIDTH, SHOP_TILE_HEIGHT),  # Shop Tile (left side)
    pygame.Rect(SHOP_TILE_WIDTH, 0, GRID_WIDTH, GRID_HEIGHT),  # Game Grid
    pygame.Rect(SCREEN_WIDTH - SHOP_TILE_WIDTH, 0, SHOP_TILE_WIDTH, SHOP_TILE_HEIGHT),  # Shop Tile (right side)
    pygame.Rect(0, GRID_HEIGHT, ROUND_CONSOLE_TILE_WIDTH, ROUND_CONSOLE_TILE_HEIGHT),  # Round Console
    pygame.Rect(ROUND_CONSOLE_TILE_WIDTH, GRID_HEIGHT, PLAYER_ONE_INFO_WIDTH, PLAYER_ONE_INFO_HEIGHT),  # Player 1 Info
    pygame.Rect(SCREEN_WIDTH - PLAYER_TWO_INFO_WIDTH, GRID_HEIGHT, PLAYER_TWO_INFO_WIDTH, PLAYER_TWO_INFO_HEIGHT)  # Player 2 Info
]

# Fill each rectangle with a different color
colors = [BLUE, WHITE, BLUE, GREEN, YELLOW]

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)  # Fill with white

    # Draw rectangles with different colors
    for rect, color in zip(rectangles, colors):
        pygame.draw.rect(screen, color, rect)

    # Draw the grid on the game grid (red part)
    for row in range(GRID_SIZE[0] + 1):
        y = row * TILE_SIZE[1] + SHOP_TILE_HEIGHT % TILE_SIZE[1]
        pygame.draw.line(screen, BLACK, (SHOP_TILE_WIDTH, y), (SHOP_TILE_WIDTH + GRID_WIDTH, y))

    for col in range(GRID_SIZE[1] + 1):
        x = SHOP_TILE_WIDTH + col * TILE_SIZE[0]
        pygame.draw.line(screen, BLACK, (x, SHOP_TILE_HEIGHT % TILE_SIZE[1]), (x, SHOP_TILE_HEIGHT % TILE_SIZE[1] + GRID_HEIGHT))

    #Grid for the shop for player 1
    for row in range(SHOP_GRID_ROW):
        for col in range(SHOP_GRID_COL):
            rect = pygame.Rect(col * SHOP_UNIT_TILE_WIDTH, row * SHOP_UNIT_TILE_HEIGHT, SHOP_UNIT_TILE_WIDTH, SHOP_UNIT_TILE_HEIGHT)
            pygame.draw.rect(screen, BLACK, rect, 1)  # 1 for outline
    #Grid for the shop for player 2

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
