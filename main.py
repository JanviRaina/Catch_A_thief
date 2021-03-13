import pygame
import random

pygame.init()

# font = pygame.font.Font('freesansbold.ttf', 32)

# Giving Colors
white=(255,255,255)
yellow = (255, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)
green=(0,255,0)
blue=(0,0,255)

# Creating window here
screen_width = 800
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# text = font.render('Game Over', True, green, blue)
# textRect = text.get_rect()
# textRect.center = (screen_width // 2, screen_height // 2)

pygame.display.set_caption("Catch me if you can")
pygame.display.update()

# Variables in game
exit_game = False
game_over = False
x_police = 45
y_police = 55
velocity_x = 0
velocity_y = 0

thief_velocity_x = 0
thief_velocity_y = 0

thief_x = random.randint(20, screen_width/2)
thief_y = random.randint(20, screen_height/2)
danger_x=random.randint(20, screen_width/2)
danger_y=random.randint(20, screen_width/2)

health_x=random.randint(20, screen_width/2)
health_y=random.randint(20, screen_width/2)

score = 1
init_velocity = 5
police_size = 30
fps = 60

clock = pygame.time.Clock()
t=0
# q=0
# Game Loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = init_velocity
                velocity_y = 0

            if event.key == pygame.K_LEFT:
                velocity_x = - init_velocity
                velocity_y = 0

            if event.key == pygame.K_UP:
                velocity_y = - init_velocity
                velocity_x = 0

            if event.key == pygame.K_DOWN:
                velocity_y = init_velocity
                velocity_x = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP6:
                thief_velocity_x = init_velocity
                thief_velocity_y = 0

            if event.key == pygame.K_KP4:
                thief_velocity_x = - init_velocity
                thief_velocity_y = 0

            if event.key == pygame.K_KP8:
                thief_velocity_y = - init_velocity
                thief_velocity_x = 0

            if event.key == pygame.K_KP2:
                thief_velocity_y = init_velocity
                velocity_x = 0

    x_police = x_police + velocity_x
    y_police = y_police + velocity_y
    thief_x = thief_x + thief_velocity_x
    thief_y = thief_y + thief_velocity_y

    if abs(x_police - danger_x)<6 and abs(y_police - danger_y)<6:
        score =score-3
        print("Score: ", score)
        danger_x = random.randint(20, screen_width / 2)
        danger_y = random.randint(20, screen_height / 2)
    
    if abs(x_police - health_x)<6 and abs(y_police - health_y)<6:
        score =score+3
        print("Score: ", score)
        health_x = random.randint(20, screen_width / 2)
        health_y = random.randint(20, screen_height / 2)


    if abs(x_police - thief_x)<6 and abs(y_police - thief_y)<6:
        score *=5
        print("Score: ", score)
        thief_x = random.randint(20, screen_width / 2)
        thief_y = random.randint(20, screen_height / 2)
    
    if(score<0):
            # gameWindow.blit(text, textRect)
            print("Game Over")
            exit_game = True
    t=t+1
    if(t>1000 and t<2000):
        gameWindow.fill(black)
    elif(t<1000 or t>2000):
        gameWindow.fill(white)

    pygame.draw.rect(gameWindow, green, [thief_x, thief_y, police_size, police_size])
    pygame.draw.rect(gameWindow, red, [danger_x, danger_y, police_size, police_size])
    pygame.draw.rect(gameWindow, yellow, [health_x, health_y, police_size, police_size])
    pygame.draw.rect(gameWindow, blue, [x_police, y_police, police_size, police_size])
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
