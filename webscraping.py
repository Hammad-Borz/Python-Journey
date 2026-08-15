import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

response = requests.get(url)

print(response.status_code)
soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.text)
quote = soup.find("span", class_="text")

print(quote.text)