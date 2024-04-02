import zipfile
import os

def extract_zip(zip_file, extract_folder):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)

# Example usage:
zip_file = 'Playing Cards.zip'  # Path to the zip file you want to extract
extract_folder = 'Cards'  # Path to the folder where you want to extract the files
extract_zip(zip_file, extract_folder)
