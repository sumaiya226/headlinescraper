import requests
from bs4 import BeautifulSoup
import csv

# URL of the page to scrape
url = 'https://www.bbc.com/news/live/uk-politics-69098963'

# Fetch the content from URL
response = requests.get(url)
html = response.content

# Parse HTML content
soup = BeautifulSoup(html, 'html.parser')

# Find elements containing headlines
headlines = soup.find_all('h3')

# Create a CSV file and write the data
with open('headlines.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Headline', 'URL'])

    # Extract headlines text and URL
    for headline in headlines:
        headline_text = headline.text.strip()
        writer.writerow([headline_text])

print("Data scraping complete and saved to headlines.csv")
