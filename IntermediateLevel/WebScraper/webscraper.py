
# Intermediate Level Task
# Task 1: Web Scraper using BeautifulSoup


# Import required libraries
import requests
from bs4 import BeautifulSoup

# Website URL
url = "https://quotes.toscrape.com/"

# Send request to the website
response = requests.get(url)

# Check if the website is accessible
if response.status_code == 200:

    # Parse the HTML page
    soup = BeautifulSoup(response.text, "html.parser")

    # Print website title
    print("=" * 50)
    print("Website Title")
    print("=" * 50)
    print(soup.title.text)

    # Find all quotes
    quotes = soup.find_all("span", class_="text")

    print("\nQuotes Found")
    print("=" * 50)

    # Print all quotes
    for i, quote in enumerate(quotes, start=1):
        print(f"{i}. {quote.text}")

else:
    print("Failed to connect to the website.")
    