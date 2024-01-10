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

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 221, 51)
SECOND_COLOR = (102, 127, 255)
SECOND_DARL = (0, 42, 255)
BLACK = (0, 0, 0)

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

# Button dimensions and position
BUTTON_WIDTH = 140
BUTTON_HEIGHT = 60
BUTTON_x = (SCREEN_WIDTH - BUTTON_WIDTH) // 2
BUTTON_y = (SCREEN_HEIGHT - ((ROUND_CONSOLE_TILE_HEIGHT - BUTTON_HEIGHT) // 2))

# Define a font for text blocks
text_font = pygame.font.Font(None, 24)  # You can change the font and size as needed

# Create the Pygame screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('PYGAME SUCKT SO SEHR, ES GIBT KEIN SCHLECHTERES PROGRAMM UM SACHEN ZU MACHEN so halb')

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
colors = [BLUE, WHITE, BLUE, SECOND_COLOR, YELLOW]

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(SECOND_COLOR)  # Fill with white

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

    # Grid for the shop for player 1
    for row in range(SHOP_GRID_ROW):
        for col in range(SHOP_GRID_COL):
            rect = pygame.Rect(col * SHOP_UNIT_TILE_WIDTH, row * SHOP_UNIT_TILE_HEIGHT, SHOP_UNIT_TILE_WIDTH, SHOP_UNIT_TILE_HEIGHT)
            pygame.draw.rect(screen, BLACK, rect, 1)  # 1 for outline

    # Create a button surface
    BUTTON_surface = pygame.Surface((BUTTON_WIDTH, BUTTON_HEIGHT))
    BUTTON_surface.fill(SECOND_DARL)

    # Text to display on the button
    button_text = "NEXT ROUND"  # Change this to your desired text

    # Render the text as a surface
    text_surface = text_font.render(button_text, True, WHITE)

    # Calculate the position to center the text on the button surface
    text_x = (BUTTON_WIDTH - text_surface.get_width()) // 2
    text_y = (BUTTON_HEIGHT - text_surface.get_height()) // 2

    # Clear the button surface and re-fill it with the button color
    BUTTON_surface.fill(SECOND_DARL)

    # Blit the text surface onto the button surface
    BUTTON_surface.blit(text_surface, (text_x, text_y))

    # Draw a black border around the button
    pygame.draw.rect(BUTTON_surface, WHITE, (0, 0, BUTTON_WIDTH, BUTTON_HEIGHT), 3)

    # Blit the button surface onto the screen
    screen.blit(BUTTON_surface, (BUTTON_x, BUTTON_y))

    # Text blocks
    text_block1 = "Player 1 HP:"
    text_block2 = "Player 1 Gold:"
    text_block3 = "Player 2 HP:"
    text_block4 = "Player 2 Gold:"

    text_surface_block1 = text_font.render(text_block1, True, WHITE)
    text_surface_block2 = text_font.render(text_block2, True, WHITE)
    text_surface_block3 = text_font.render(text_block3, True, WHITE)
    text_surface_block4 = text_font.render(text_block4, True, WHITE)

    text_block1_pos = (10, 10)
    text_block2_pos = (10, 40)
    text_block3_pos = (10, 70)
    text_block4_pos = (10, 100)

    screen.blit(text_surface_block1, text_block1_pos)
    screen.blit(text_surface_block2, text_block2_pos)
    screen.blit(text_surface_block3, text_block3_pos)
    screen.blit(text_surface_block4, text_block4_pos)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
