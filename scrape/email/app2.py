import requests
from bs4 import BeautifulSoup
import re

def extract_emails_from_url(url):
    emails = []
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # Use regular expression to find emails in the HTML content
            pattern = r'^[a-zA-Z0-9.!#$%&\'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$'
            matches = re.findall(pattern, soup.get_text())
            for match in matches:
                emails.append(match)
    except Exception as e:
        print("Error occurred while scraping", url, ":", e)
    return emails

def save_emails_to_text_file(emails, file_path):
    with open(file_path, 'a', encoding='utf-8') as file:  # Specify 'utf-8' encoding
        for email in emails:
            file.write(email + '\n')

# Array of URLs to scrape
urls = [
    'https://adarbepari.com/shaira-garden-resort-narayanganj',
]

# Save extracted emails to a text file
file_path = 'extracted_emails.txt'
for url in urls:
    # Extract emails from the current URL
    emails = extract_emails_from_url(url)
    
    # Save emails to the text file
    save_emails_to_text_file(emails, file_path)

print("Emails extracted from the websites and saved to:", file_path)
