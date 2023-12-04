import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants for the game
SCREEN_WIDTH, SCREEN_HEIGHT = 1152, 648
BG_COLOR = (255, 255, 255)  # White background
GRID_COLOR = (0, 0, 0)  # Black grid
BUTTON_COLOR = (100, 200, 100)  # Green buttons
BUTTON_TEXT_COLOR = (255, 255, 255)  # White text
PLAYER_INFO_WIDTH, PLAYER_INFO_HEIGHT = 150, 648
SHOP_WIDTH, SHOP_HEIGHT = 150, 100
GRID_PLAYER_BOARD_WIDTH, GRID_PLAYER_BOARD_HEIGHT = 852, 448
BUTTON_RADIUS = 30

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Solo Fight Tactics")

# Fonts and text
font = pygame.font.Font(None, 36)

def draw_layout():
    # Draw player info areas
    draw_player_info(0, 0)
    draw_player_info(SCREEN_WIDTH - PLAYER_INFO_WIDTH, 0)

    # Draw shop areas
    draw_shop(PLAYER_INFO_WIDTH, SCREEN_HEIGHT - SHOP_HEIGHT)
    draw_shop(SCREEN_WIDTH - PLAYER_INFO_WIDTH - SHOP_WIDTH, SCREEN_HEIGHT - SHOP_HEIGHT)

    # Draw grid player board
    draw_grid_player_board(PLAYER_INFO_WIDTH, 0)

    # Draw ready buttons
    draw_ready_button(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 50, "Ready")
    draw_ready_button(SCREEN_WIDTH // 2 + 100, SCREEN_HEIGHT - 50, "Ready")

def draw_player_info(x, y):
    pygame.draw.rect(screen, GRID_COLOR, (x, y, PLAYER_INFO_WIDTH, PLAYER_INFO_HEIGHT), 2)

def draw_shop(x, y):
    pygame.draw.rect(screen, GRID_COLOR, (x, y, SHOP_WIDTH, SHOP_HEIGHT), 2)

def draw_grid_player_board(x, y):
    pygame.draw.rect(screen, GRID_COLOR, (x, y, GRID_PLAYER_BOARD_WIDTH, GRID_PLAYER_BOARD_HEIGHT), 2)

def draw_ready_button(x, y, text):
    pygame.draw.circle(screen, BUTTON_COLOR, (x, y), BUTTON_RADIUS)
    text_surface = font.render(text, True, BUTTON_TEXT_COLOR)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Game state variables
player1_ready = False
player2_ready = False

# Game loop
running = True
while running:
    screen.fill(BG_COLOR)
    draw_layout()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            # Calculate distance from the center of the buttons to see if either was clicked
            dist1 = pygame.math.Vector2(mouse_pos).distance_to((SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 50))
            dist2 = pygame.math.Vector2(mouse_pos).distance_to((SCREEN_WIDTH // 2 + 100, SCREEN_HEIGHT - 50))

            if dist1 < BUTTON_RADIUS:
                player1_ready = not player1_ready  # Toggle ready state
            if dist2 < BUTTON_RADIUS:
                player2_ready = not player2_ready  # Toggle ready state

    # Update the screen
    pygame.display.flip()

    # Check if both players are ready
    if player1_ready and player2_ready:
        # This is where you'd transition to the next phase of the game
        print("Both players are ready!")
        # Reset ready states for demonstration
        player1_ready = False
        player2_ready = False
