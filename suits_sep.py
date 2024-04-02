import os
import shutil

card_folder = "Cards/Playing Cards/PNG-cards-1.3"
suits = ['hearts', 'diamonds', 'clubs', 'spades']
for suit in suits:
    os.makedirs(os.path.join(card_folder, suit), exist_ok=True)

# Iterate through card images and move them to respective suit folders
for filename in os.listdir(card_folder):
    if filename.endswith(".png"):
        card_name = os.path.splitext(filename)[0]
        print(card_name.split("_"))# Remove file extension
        suit = card_name.split("_")[2]  # Extract suit from filename
        shutil.move(os.path.join(card_folder, filename), os.path.join(card_folder, suit, card_name.split("_")[0]+".png"))
