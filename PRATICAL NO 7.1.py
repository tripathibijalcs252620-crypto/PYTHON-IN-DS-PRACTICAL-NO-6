import requests
from bs4 import BeautifulSoup

url = "https://www.wikipedia.org/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")


print("Page Title:", soup.title.get_text(strip=True))

print("\nHeadings:")
for heading in soup.find_all(["h1", "h2"]):
    print("Heading:", heading.get_text(strip=True))

print("\nFirst 5 Links:")
for link in soup.find_all("a", href=True)[:5]:
    print("Link Text:", link.get_text(strip=True))
    print("URL:", link["href"])
    print("S115 BIJAL TRIPATHI ")
