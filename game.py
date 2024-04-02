import pygame
import os
import sys

pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
card_folder = "Cards/Playing Cards/PNG-cards-1.3/"
suits = ['hearts', 'clubs', 'spades', 'diamonds']
suit_files = []

size = width, height = 1280, 720
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

speed = [1, 1]

screen = pygame.display.set_mode(size)
card_images = {}
for suit in suits:
    if suit != 'diamonds':
        card_image = pygame.image.load(os.path.join(card_folder, f"{suit}/10.png"))
        card_images[suit] = pygame.transform.scale(card_image, (170, 240))

diamond_cards_folder = "Cards/Playing Cards/PNG-cards-1.3/diamonds"
diamond_card_images = []
for filename in os.listdir(diamond_cards_folder):
    if filename.endswith(".png"):
        card_image = pygame.image.load(os.path.join(diamond_cards_folder, filename))
        diamond_card_images.append(card_image)

shuffling_text = "Shuffling Diamond Cards..."
shuffled = False

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

# Shuffle the cards initially
shuffle_cards()
# Define font
font = pygame.font.SysFont(None, 40)

# Define text box parameters
text_box_width = 300
text_box_height = 100
text_box_color = WHITE
text_box_rect = pygame.Rect((SCREEN_WIDTH - text_box_width) // 2, 120, text_box_width, text_box_height)

# Define text
select_deck_text = "Select Deck"

# Main game loop
selected_deck = None
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button clicked
                mouse_pos = pygame.mouse.get_pos()
                # Check if any card image is clicked
                for suit, card_image in card_images.items():
                    card_rect = card_image.get_rect(topleft=(300 + list(card_images.values()).index(card_image) * 300, 400))
                    if card_rect.collidepoint(mouse_pos):
                        selected_deck = suit.capitalize()
                        print(f"{suit.capitalize()} deck selected")

    # Clear the screen
    screen.fill(BLACK)

    # Draw text box
    pygame.draw.rect(screen, text_box_color, text_box_rect)
    pygame.draw.rect(screen, BLACK, text_box_rect, 2)

    # Draw text
    select_deck_surface = font.render(select_deck_text, True, BLACK)
    select_deck_rect = select_deck_surface.get_rect(center=(SCREEN_WIDTH // 2, 170))
    screen.blit(select_deck_surface, select_deck_rect)

    # Display card images
    for suit, card_image in card_images.items():
        screen.blit(card_image, (270 + list(card_images.values()).index(card_image) * 300, 350))
       # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
