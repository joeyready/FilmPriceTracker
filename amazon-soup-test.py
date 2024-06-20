from bs4 import BeautifulSoup
import requests

url = "https://www.amazon.com/dp/B00486ANS6"
HEADER = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}
response = requests.get(url, headers=HEADER)
soup = BeautifulSoup(response.text, 'lxml')

title_element = soup.select_one("#productTitle")

title = title_element.text.strip() if title_element else "Title not found"

print(response.text)