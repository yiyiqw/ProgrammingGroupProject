pip install pygame
import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Matching Game")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set up the clock
clock = pygame.time.Clock()

# Set up the font
font = pygame.font.SysFont(None, 40)

# Set up the grid
grid_size = 4
card_size = 100
cards = [i // 2 for i in range(grid_size**2)]  # Pairs of numbers
random.shuffle(cards)

# Set up card positions
card_positions = [(x * card_size, y * card_size) for x in range(grid_size) for y in range(grid_size)]

# Set up card state
revealed = [False] * len(cards)
selected = []

# Main game loop
game_over = False
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN and len(selected) < 2:
            x, y = event.pos
            card_x, card_y = x // card_size, y // card_size
            index = card_y * grid_size + card_x

            if not revealed[index]:
                revealed[index] = True
                selected.append(index)

    # Draw the background
    screen.fill(black)

    # Draw the cards
    for i, (x, y) in enumerate(card_positions):
        pygame.draw.rect(screen, white, (x, y, card_size, card_size))

        if revealed[i]:
            text = font.render(str(cards[i]), True, black)
            screen.blit(text, (x + card_size // 3, y + card_size // 3))

    # Check for a match
    if len(selected) == 2:
        index1, index2 = selected
        if cards[index1] != cards[index2]:
            time.sleep(1)  # Delay to show the cards briefly
            revealed[index1] = False
            revealed[index2] = False
        selected = []

    # Check for game over
    if all(revealed):
        game_over_text = font.render("Congratulations! You won!", True, white)
        screen.blit(game_over_text, (width // 4, height // 2))
        pygame.display.flip()
        time.sleep(2)
        game_over = True

    # Refresh the display
    pygame.display.flip()

    # Limit frames per second
    clock.tick(30)

# Quit Pygame
pygame.quit()
