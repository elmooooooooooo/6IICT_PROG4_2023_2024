import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player properties
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - 2 * player_size
player_speed = 5
jumping = False
jump_count = 10

# Platform properties
platforms = [[50, HEIGHT - 100, 200, 10],
             [300, HEIGHT - 200, 200, 10],
             [500, HEIGHT - 300, 200, 10]]

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Platformer")
clock = pygame.time.Clock()

# Game loop
running = True
score = 0
platform_speed = 5

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # Jumping mechanics
    if not jumping:
        if keys[pygame.K_SPACE]:
            jumping = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            player_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            jumping = False
            jump_count = 10

    # Gravity simulation
    if player_y < HEIGHT - player_size:
        player_y += 5  # Adjust gravity strength as needed

    # Move the platforms and spawn new ones
    for platform in platforms:
        platform[1] -= platform_speed
        if platform[1] + platform[3] < 0:
            score += 1
            platform[1] = HEIGHT
            platform[0] = random.randint(0, WIDTH - platform[2])

    # Check for collisions with platforms
    for platform in platforms:
        if (platform[0] < player_x < platform[0] + platform[2] or
                platform[0] < player_x + player_size < platform[0] + platform[2]) and \
                (platform[1] < player_y + player_size < platform[1] + platform[3] or
                 platform[1] < player_y < platform[1] + platform[3]):
            jumping = False
            jump_count = 10
            player_y = platform[1] - player_size

    # Drawing
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (player_x, player_y, player_size, player_size))

    for platform in platforms:
        pygame.draw.rect(screen, BLUE, platform)

    # Display the score
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, RED)
    screen.blit(text, (10, 10))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
