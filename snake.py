
import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
width, height = 640, 480
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Snake initial position and size
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_dir = 'RIGHT'
change_to = snake_dir

# Food position
food_pos = [random.randrange(1, (width//10)) * 10,
            random.randrange(1, (height//10)) * 10]
food_spawn = True

# Score
score = 0

# Game over flag
game_over = False

# FPS controller
fps = pygame.time.Clock()

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Validation of direction
    if change_to == 'UP' and not snake_dir == 'DOWN':
        snake_dir = 'UP'
    if change_to == 'DOWN' and not snake_dir == 'UP':
        snake_dir = 'DOWN'
    if change_to == 'LEFT' and not snake_dir == 'RIGHT':
        snake_dir = 'LEFT'
    if change_to == 'RIGHT' and not snake_dir == 'LEFT':
        snake_dir = 'RIGHT'

    # Moving the snake
    if snake_dir == 'UP':
        snake_pos[1] -= 10
    if snake_dir == 'DOWN':
        snake_pos[1] += 10
    if snake_dir == 'LEFT':
        snake_pos[0] -= 10
    if snake_dir == 'RIGHT':
        snake_pos[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (width//10)) * 10,
                    random.randrange(1, (height//10)) * 10]
    food_spawn = True

    # Draw snake
    display.fill(black)
    for pos in snake_body:
        pygame.draw.rect(display, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))

    # Draw food
    pygame.draw.rect(display, white, pygame.Rect(
        food_pos[0], food_pos[1], 10, 10))

    # Game Over conditions
    if snake_pos[0] < 0 or snake_pos[0] > width - 10:
        game_over = True
    if snake_pos[1] < 0 or snake_pos[1] > height - 10:
        game_over = True

    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over = True

    pygame.display.update()
    fps.tick(15)

# Quit the game
pygame.quit()
