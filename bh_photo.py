#scrape https://www.bhphotovideo.com/c/search?Ntt=35mm%20film&N=0&InitialSearch=yes&sts=ma&Top+Nav-Search= for film prices
import requests
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
}

url = "https://www.bhphotovideo.com/c/product/24744-REG/Ilford_1574577_HP5_Plus_135_36_Black.html"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())

#function to scrape amazon price from product page
def amazon_price(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    price = soup.find('span', id='aok-offscreen')
    return price

print(amazon_price('https://www.amazon.com/Ilford-HP5-Plus-Black-36-Exposures/dp/B00009R8X9'))


# Assuming 'soup' is your BeautifulSoup object
price_div = soup.find('div', class_='price__9gLfjPSjp')

# Check if the price div was found+
# if price_div:
#     price = price_div.text
#     print(f'Price: {price}')
# else:
#     print('Price div not found')

findall = soup.find_all(attrs={"data-selenium": "pricingPrice"})
output = findall[0].text
print(output)