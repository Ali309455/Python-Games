import pygame
pygame.init()

# creating display
gameWindow = pygame.display.set_mode((1200, 500))
pygame.display.set_caption('My First Game')

# Initiallizing Variables
exit_game = False
game_over = False

# Creating A Game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
# Handling each and every event
        if event.type ==  pygame.KEYDOWN:  # it is used to assign value to keydown
            if event.key == pygame.K_0:
                print("You have pressed Right arrow key")

pygame.quit()
exit()