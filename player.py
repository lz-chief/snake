import pygame
from utilities import *
import random

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
LIGHT_RED = (232, 72, 72)

# setting up
pygame.init()
window_width, window_height = (450, 450)
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake")

score_font = pygame.font.SysFont('comicsans', 15, True)
clock = pygame.time.Clock()



def drawGameWindow(win):
    win.fill(BLACK)
    fruit.draw(win, LIGHT_RED)
    text = score_font.render("Score: " + str(score), 1, RED)
    win.blit(text, (10, 10))
    snake.draw(win, WHITE)
    pygame.display.update()


# checks for game over
def cornerCase():
    if snake.y < snake.vel - snake.height:
        return True
    if snake.y > window_height - snake.height:
        return True
    if snake.x < snake.vel - snake.width:
        return True
    if snake.x > window_width - snake.width:
        return True
    for segment in snake.body[1:]:
        if snake.x == segment[0] and snake.y == segment[1]:
            return True
    return False


moveLoop = 0
running = True
game_over = False

# main game loop
while True:
    # creating structures
    block_size = 15
    block_speed = 15
    snake = Snake(225, 225, block_size, block_size, block_speed)
    for i in range(3):
        snake.grow()

    fruit_x = int(random.randrange(0, window_width, block_size))
    fruit_y = int(random.randrange(0, window_height, block_size))
    fruit = Fruit(fruit_x, fruit_y, block_size, block_size)
    score = 0

    # gameplay loop
    while running:
        clock.tick(25)
        if moveLoop > 0:
            moveLoop += 1
        if moveLoop > 3:
            moveLoop = 0
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        keys = pygame.key.get_pressed()
        # manages direction
        if moveLoop == 0:
            if keys[pygame.K_UP] and snake.dir != "down":
                snake.dir = "up"
            elif keys[pygame.K_DOWN] and snake.dir != "up":
                snake.dir = "down"
            elif keys[pygame.K_LEFT] and snake.dir != "right":
                snake.dir = "left"
            elif keys[pygame.K_RIGHT] and snake.dir != "left":
                snake.dir = "right"

        # moves snake one step
        if moveLoop == 0:
            snake.move()
            moveLoop = 1

        if snake.x == fruit.x and snake.y == fruit.y:
            score += 1
            # fruit.eat(window_width, window_height)
            while True:
                fruit.eat(window_width, window_height)
                if fruit.dim not in snake.body:
                     break
            snake.grow() 
        
        # checks for gameover
        if cornerCase():
            running = False
            game_over = True
        drawGameWindow(window)

    while game_over:
        end_font = pygame.font.SysFont('comicsans', 30, True)
        text = end_font.render("Game Over", 1, RED)
        restart = end_font.render("press spacebar to replay", 1, RED)
        final_score = end_font.render("Score: " + str(score), 1, RED)
        window.blit(text, (20, window_height - 80))
        window.blit(restart, (20, window_height - 50))
        window.blit(final_score, (20, window_height - 20))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                window.fill(BLACK)
                game_over = False
                running = True
                break
        pygame.display.update()
pygame.quit()
