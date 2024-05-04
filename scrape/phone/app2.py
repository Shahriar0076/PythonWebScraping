import requests
from bs4 import BeautifulSoup
import re

def extract_numbers_from_url(url):
    numbers = []
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # Use regular expression to find numbers in the HTML content
            matches = re.findall(r'\+?\d{2}\s?\d{3,5}-?\d{5,7}', soup.get_text())
            for match in matches:
                numbers.append(match)
    except Exception as e:
        print("Error occurred while scraping", url, ":", e)
    return numbers

def save_numbers_to_text_file(numbers, file_path):
    with open(file_path, 'a', encoding='utf-8') as file:  # Specify 'utf-8' encoding
        for number in numbers:
            file.write(number + '\n')

# Array of URLs to scrape
urls = [
    'https://basis.org.bd/company-profile/03-09-017',   
]

# Save extracted numbers to a text file
file_path = 'extracted_numbers.txt'
for url in urls:
    # Extract numbers from the current URL
    numbers = extract_numbers_from_url(url)
    
    # Save numbers to the text file
    save_numbers_to_text_file(numbers, file_path)

print("Numbers extracted from the websites and saved to:", file_path)
