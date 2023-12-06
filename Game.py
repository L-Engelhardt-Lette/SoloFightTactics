import imp
import pygame
import random
from  UnitsList import Unit
from PlayerList import Player
import PlayerList
from ShopList import Shop
import ShopList
# Game-Klasse erstellen und alles in die Game klasse verfrachten so etwas wie die upadte funktion etc.
from pygame.locals import(
    KEYDOWN,
    K_ESCAPE
)
pygame.init()

WIDTH = 1920
HEIGHT = 1080
FPS = 60
white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)

grid_size = 10
cell_size = WIDTH // grid_size

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Auto Battler")


class Game:
    def __init__():
        pass

#Button
class Button:
    def __init__(self, x, y, width, height, text, command):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.command = command
        self.font = pygame.font.Font(None, 36)

    def draw(self):
        pygame.draw.rect(screen, gray, self.rect)
        pygame.draw.rect(screen, black, self.rect, 2)

        text_surface = self.font.render(self.text, True, black)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.command()

grid_player1 = [[0] * grid_size for _ in range(grid_size)]
grid_player2 = [[0] * grid_size for _ in range(grid_size)]

unit_list = [] 
#Eine Unitlist für Alle Units und jeweils nochmal verschiedene für die kosten, den typen der Einheit usw


#Alles nur zum Test wird später wieder gelöscht
player_unit_image = pygame.image.load("images/Ritter.png")
enemy_unit_image = pygame.image.load("images/Baum.png")
bluePlayerunit = Unit("player_unit", 0, 100, 10, 1, 0,"images/Ritter.png")
redPlayerunit = Unit("enemy_unit", 0, 100, 10, 1, 0,"images/Baum.png")
Ritter_image = pygame.image.load("images/Ritter.png")
Baum_image = pygame.image.load("images/Baum.png")

#Alle vom Spieler besessenen Units kommen die die jeweilige Liste
blueplayer1_units = []
redplayer2_units = []
#createplayers
blueplayer1 = Player(blueplayer1_units)
redplayer2 = Player(redplayer2_units)


# Create Rounds for shopping and setting Units
current_round = 1

#Knopf für das Rundenwechseln für die Spieler, wir können in diesen command einbauen, dass wenn beide Player diesen Knopf einmal gedrückt haben der Fight beginnt, wahrscheinlich mit boolean Abfrage
def button1_command():
    global current_round
    print("Button 1 pressed!")
    current_round = 1 + current_round

#Knopf für den Start des Kampfes
def button2_command():
    print("Button 2 pressed")    
    for redplayer_unit in redplayer2_units:
        if blueplayer1_units:
            target = random.choice(blueplayer1_units)
        redplayer_unit.attack(target)
        if target.health <= 0:
            blueplayer1_units.remove(target)

    #for blueplayer_unit in blueplayer1_units:
        #if redplayer2_units:
            #target = random.choice(redplayer2_units)
        #blueplayer_unit.attack(target)
        #if target.health <= 0:
             #redplayer2_units.remove(target)

button1_next_round = Button(50, 50, 200, 80, "Next Round", button1_command)
button2_start_combat = Button(1500, 50, 200, 80, "Start Combat", button2_command)

buttons = [button1_next_round, button2_start_combat]

running = True
clock = pygame.time.Clock()
clicked = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for b in buttons:
        b.handle_event(event)        

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
        mouse_x, mouse_y = pygame.mouse.get_pos()
        grid_x = mouse_x // cell_size
        grid_y = mouse_y // cell_size
        print(grid_x, grid_y)


        # Check if the grid cell is empty
        if current_round % 2 == 1 and grid_player1 [grid_y][grid_x] == 0 and not clicked:
            # Place a unit on the grid
            new_unit = Unit(name="Knight", health=100, cost = 1, attack_damage=20, ability=0, position=(grid_x, grid_y), image_path ="images/Ritter.png")
            blueplayer1_units.append(new_unit)
            grid_player1[grid_y][grid_x] = 1  # Set grid cell to indicate it's occupied
            print(grid_x, grid_y,"player")
        
        elif current_round % 2 != 1 and grid_player2 [grid_y][grid_x] == 0 and not clicked:
            new_unit = Unit(name="Baum",  health=100, cost = 1, attack_damage=20, ability=0, position=(grid_x, grid_y), image_path ="images/Baum.png")
            redplayer2_units.append(new_unit)
            grid_player2[grid_y][grid_x] = 1
            print(grid_x, grid_y, "player2")
            
        clicked = True
    else:
        clicked = False

    if current_round % 2 == 1:  # Odd rounds - player 1's turn
        redplayer2.is_turn = False
        blueplayer1.is_turn = True
        current_player = blueplayer1
        next_player = redplayer2
    else:                        # Even rounds - player 2's turn
        blueplayer1.is_turn = False
        redplayer2.is_turn = True
        current_player = redplayer2
        next_player = blueplayer1
       

    #     if event.type == KEYDOWN:
    #         if event.key == K_ESCAPE:
    #             running = False

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     current_round += 1

    # screen.fill(white)

    # Draw the grid
    screen.fill(white)
    for row in range(grid_size):
        for col in range(grid_size):
            pygame.draw.rect(screen, black, (col * cell_size, row * cell_size, cell_size, cell_size), 1)
    
    for b in buttons:
        b.draw()

    # Draw units on the grid
    for u in blueplayer1_units:
        screen.blit(u.image, (u.position[0] * cell_size, u.position[1] * cell_size))
    for u in redplayer2_units:   
        screen.blit(u.image, (u.position[0] * cell_size, u.position[1] * cell_size)) 

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()