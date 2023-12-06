import pygame
import sys

# Constants for the game
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
GRID_SIZE = 8  # Assuming an 8x8 grid for the board

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define the rectangles for player info, shop, and grid player board
player_info_rects = [pygame.Rect(0, 0, 100, SCREEN_HEIGHT), pygame.Rect(SCREEN_WIDTH - 100, 0, 100, SCREEN_HEIGHT)]
shop_rects = [pygame.Rect(100, 0, 100, SCREEN_HEIGHT), pygame.Rect(SCREEN_WIDTH - 200, 0, 100, SCREEN_HEIGHT)]
grid_player_board_rect = pygame.Rect(200, 0, SCREEN_WIDTH - 400, SCREEN_HEIGHT)

# Define 'Ready' buttons
ready_buttons = [pygame.Rect(300, SCREEN_HEIGHT - 50, 100, 30), pygame.Rect(SCREEN_WIDTH - 400, SCREEN_HEIGHT - 50, 100, 30)]
ready_status = [False, False]

# Load images for characters, items, etc.

# Main game loop
running = True
while running:
    screen.fill(WHITE)
    
    # Draw the player info areas
    for rect in player_info_rects:
        pygame.draw.rect(screen, BLACK, rect)
    
    # Draw the shop areas
    for rect in shop_rects:
        pygame.draw.rect(screen, GREEN, rect)
    
    # Draw the grid player board
    pygame.draw.rect(screen, BLACK, grid_player_board_rect, 1)
    
    # Draw grid lines for player board
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            cell_rect = pygame.Rect(
                grid_player_board_rect.left + x * (grid_player_board_rect.width / GRID_SIZE),
                grid_player_board_rect.top + y * (grid_player_board_rect.height / GRID_SIZE),
                grid_player_board_rect.width / GRID_SIZE,
                grid_player_board_rect.height / GRID_SIZE
            )
            pygame.draw.rect(screen, BLACK, cell_rect, 1)
    
    # Draw 'Ready' buttons and check if both players are ready
    for index, button in enumerate(ready_buttons):
        pygame.draw.rect(screen, GREEN if ready_status[index] else BLACK, button)
        if button.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                ready_status[index] = True
    
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Check if both players are ready
    if all(ready_status):
        # Proceed to the next round
        print("Both players are ready! Starting the next round...")
        # Reset ready status
        ready_status = [False, False]
    
    # Update the display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
