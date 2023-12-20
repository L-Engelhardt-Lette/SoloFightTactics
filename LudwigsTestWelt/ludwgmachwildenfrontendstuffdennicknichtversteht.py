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

#
#   CLASS
#

# Shop class to represent each shop
class Shop:
    def __init__(self, player, characters, position):
        self.player = player
        self.characters = characters  # List of characters available in the shop
        self.position = position      # Position of the shop on the screen

    def draw(self, screen):
        for i, character in enumerate(self.characters):
            # Assuming each character has a 'sprite' attribute for the image
            # and 'traits' attribute for the traits
            character_sprite = character.sprite
            character_traits = character.traits

            # Calculate position for each character in the shop
            x = self.position[0] + i * TILE_SIZE[0]
            y = self.position[1]

            # Draw character sprite
            screen.blit(character_sprite, (x, y))

            # Draw traits (icons and text)
            # This is a placeholder, adjust according to how traits are represented
            for j, trait in enumerate(character_traits):
                trait_icon = trait.icon
                trait_text = trait.text
                screen.blit(trait_icon, (x, y + j * 20))  # Example positioning
                # Render and draw trait text
                trait_font = pygame.font.SysFont(None, 24)
                trait_label = trait_font.render(trait_text, True, (255,255,255))
                screen.blit(trait_label, (x + 20, y + j * 20))

# Example of creating two shops
# This is a placeholder, adjust according to the actual game structure
player1_characters = [Character1(), Character2(), Character3(), Character4(), Character5()]
player2_characters = [Character6(), Character7(), Character8(), Character9(), Character10()]

shop1 = Shop(player1, player1_characters, (100, SCREEN_HEIGHT - 100))  # Positioning for player 1's shop
shop2 = Shop(player2, player2_characters, (SCREEN_WIDTH - 600, SCREEN_HEIGHT - 100))  # Positioning for player 2's shop

# In the game loop, you would call shop1.draw(screen) and shop2.draw(screen) to display the shops

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

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()


