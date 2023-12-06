import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants for the screen dimensions and grid
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
GRID_SIZE = (5, 8)  # 5 rows by 8 columns for both players combined
TILE_SIZE = (SCREEN_WIDTH // GRID_SIZE[1], SCREEN_HEIGHT // (GRID_SIZE[0] + 2))  # additional 2 rows for shop and info

# Constants for the shop tiles
SHOP_TILE_WIDTH = 300  # Width of each shop tile
SHOP_TILE_HEIGHT = SCREEN_HEIGHT  # Height of each shop tile
SHOP_UNIT_TILEHEIGHT = SHOP_TILE_HEIGHT / 5
SHOP_UNIT_TILEWIDTH = SHOP_TILE_WIDTH

# Create a rect for player 1's shop tile (left side of the screen)
player1_shop_tile = pygame.Rect(0, 0, SHOP_TILE_WIDTH, SHOP_TILE_HEIGHT)

# Create a rect for player 2's shop tile (right side of the screen)
player2_shop_tile = pygame.Rect(SCREEN_WIDTH - SHOP_TILE_WIDTH, 0, SHOP_TILE_WIDTH, SHOP_TILE_HEIGHT)

# Main game loop

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Solo Fight Tactics')

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0,0,255)
RED = (255,0,45)
HIGHLIGHT = (77,225,255)

# Classes and functions to define

class PlayerInfo:
    def __init__(self, health, gold):
        self.health = health
        self.gold = gold
        # Placeholder for profile picture, would be a pygame.Surface object
        self.profile_pic = pygame.Surface((50, 50))  

    def draw(self, surface):
        # Draw the profile picture, health bar, and gold amount
        surface.blit(self.profile_pic, (10, SCREEN_HEIGHT - 60))
        # ... additional drawing code for health and gold

    def update(self, health_change, gold_change):
        self.health += health_change
        self.gold += gold_change

class Shop:
    def __init__(self):
        self.available_units = []  # List of units available in the shop
        self.selected_unit = None  # The unit currently being dragged
        self.unit_rects = []  # Rects where units are drawn for collision detection

    def draw(self, surface):
        # Draw the units in the shop
        for index, unit in enumerate(self.available_units):
            # Assuming each unit has an image attribute that is a Pygame Surface
            rect = unit.image.get_rect(topleft=(100 * index, SCREEN_HEIGHT - 100))
            self.unit_rects.append(rect)
            surface.blit(unit.image, rect.topleft)

    def handle_events(self, event):
        # Handle mouse events for drag and drop
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, rect in enumerate(self.unit_rects):
                if rect.collidepoint(event.pos):
                    self.selected_unit = self.available_units[i]
                    break

        elif event.type == pygame.MOUSEBUTTONUP:
            if self.selected_unit:
                # Check if the unit is being dropped in a valid spot
                # You might need more logic here to determine if the drop is valid
                self.selected_unit = None

        elif event.type == pygame.MOUSEMOTION:
            if self.selected_unit:
                # Move the unit with the mouse
                self.selected_unit.position = event.pos

    def update(self):
        # Update shop state, such as refreshing the list of units
        pass

class GameBoard:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[None for _ in range(cols)] for _ in range(rows)]

    def draw(self, surface):
        for row in range(self.rows):
            for col in range(self.cols):
                pygame.draw.rect(surface, WHITE, (col * TILE_SIZE[0], row * TILE_SIZE[1], TILE_SIZE[0], TILE_SIZE[1]), 1)

def draw_grid(surface, rows, cols, tile_size):
    for row in range(rows):
        for col in range(cols):
            pygame.draw.rect(surface, WHITE, (col * tile_size[0], row * tile_size[1], tile_size[0], tile_size[1]), 1)

def handle_ready_button(event, button_rect):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if button_rect.collidepoint(event.pos):
            print("Ready button clicked!")

def next_round():
    # Logic to start the next round
    print("Starting next round...")

# Game variables
player_info = PlayerInfo(100, 0)  # Initialize with starting health and gold
shop = Shop()
game_board = GameBoard(GRID_SIZE[0], GRID_SIZE[1])

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        shop.handle_events(event)  # Call the handle_events method of the Shop class

    # Game logic goes here
    # ...

    # Clear the screen
    screen.fill(BLACK)
    
    # Draw the game board
    game_board.draw(screen)
    
    # Draw the shop
    shop.draw(screen)
    # Draw the shop tiles for both players
    pygame.draw.rect(screen, (100, 100, 100), player1_shop_tile)  # Player 1's shop tile
    pygame.draw.rect(screen, (100, 100, 100), player2_shop_tile)  # Player 2's shop tile
    
    # Draw the player info
    player_info.draw(screen)
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
