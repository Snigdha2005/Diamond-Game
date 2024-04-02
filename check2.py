import pygame
import os
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Load diamond card images
diamond_cards_folder = "Cards/Playing Cards/PNG-cards-1.3/diamonds"
diamond_card_images = []
for filename in os.listdir(diamond_cards_folder):
    if filename.endswith(".png"):
        card_image = pygame.image.load(os.path.join(diamond_cards_folder, filename))
        diamond_card_images.append(card_image)

# Function to shuffle the card positions
def shuffle_cards():
    random.shuffle(diamond_card_images)
    for i, card_image in enumerate(diamond_card_images):
        card_image_rect = card_image.get_rect()
        card_image_rect.center = (i * 100 + 50, SCREEN_HEIGHT // 2)
        diamond_card_images[i] = (card_image, card_image_rect)

# Function to pick a random card after shuffling
def pick_random_card():
    return random.choice(diamond_card_images)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shuffling Diamond Cards")

# Define font
font = pygame.font.SysFont(None, 40)

# Define text
shuffling_text = "Shuffling Diamond Cards..."
shuffled = False

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw text
    text_surface = font.render(shuffling_text, True, BLACK)
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text_surface, text_rect)

    if not shuffled:
        # Shuffle the cards
        shuffle_cards()
        shuffled = True

    # Draw the shuffled cards
    for card_image, card_rect in diamond_card_images:
        screen.blit(card_image, card_rect)

    # Update the display
    pygame.display.flip()

    # Wait for a moment before picking a random card
    pygame.time.delay(2000)

    # Pick a random card after shuffling
    picked_card, _ = pick_random_card()
    picked_card_position = picked_card.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    # Clear the screen
    screen.fill(WHITE)

    # Draw the picked card
    screen.blit(picked_card, picked_card_position)

    # Update the display
    pygame.display.flip()

    # Wait for a moment before quitting
    pygame.time.delay(2000)

# Quit Pygame
pygame.quit()

