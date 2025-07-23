import requests
from bs4 import BeautifulSoup
import pandas as pd
from textblob import TextBlob

# Step 1: Choose a site to scrape (example: quotes.toscrape.com)
url = "http://quotes.toscrape.com"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 2: Extract all quotes
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')

data = []
for quote, author in zip(quotes, authors):
    text = quote.get_text()
    sentiment = TextBlob(text).sentiment.polarity  # -1 (negative) to 1 (positive)
    data.append({"quote": text, "author": author.get_text(), "sentiment": sentiment})

# Step 3: Save results to a CSV
df = pd.DataFrame(data)
df.to_csv('quotes_sentiment.csv', index=False)

print("Scraped", len(data), "quotes. Saved to quotes_sentiment.csv")
