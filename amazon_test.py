from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser
# from dataclasses import dataclass
# from rich import print

class Item:
    def __init__(self, asin, title, price):
        self.asin = asin
        self.title = title
        self.price = price

    def __str__(self):
        return f'Item(asin={self.asin}, title={self.title}, price={self.price})'

def get_html(page, asin):
    url = f"https://www.amazon.com/dp/{asin}"
    page.goto(url)
    html = HTMLParser(page.content())

    if not html.css_first("span#productTitle"):
        print("Captcha detected")
        page.pause()
    return html


def parse_html(html, asin):
    title_element = html.css_first("span#productTitle")
    title = title_element.text(strip=True) if title_element else "Title not found"

    price_element = html.css_first("span#offscreen")
    price = price_element.text(strip=True) if price_element else "Price not found"

    item = Item(
        asin = asin,
        title = title,
        price = price,
    )
    return item


def run():
    asin = "B00486ANS6"
    pw = sync_playwright().start()
    browser = pw.chromium.launch(headless=False)
    page =  browser.new_page()
    html = get_html(page, asin)
    product = parse_html(html, asin)
    print(product)

def main():
    run()

if __name__ == '__main__':
    main()



# from requests_html import HTMLSession
#
#
# #URL = "https://www.amazon.com/Ilford-HP5-36exp-roll-pack/dp/B00486ANS6"
#
# def getPrice(url):
#     s = HTMLSession()
#     r = s.get(url)
#     r.html.render(sleep=1)
#
#     title_element = r.html.xpath('//*[@id="productTitle"]', first=True)
#     title = title_element.text if title_element else "Title not found"
#
#     price_element = r.html.xpath('//*[@id="corePriceDisplay_desktop_feature_div"]', first=True)
#     price = price_element.text if price_element else "Price not found"
#
#     product = {
#         "title": title,
#         "price": price
#     }
#     print(product)
#     return product
#
#getPrice("https://www.amazon.com/Ilford-HP5-36exp-roll-pack/dp/B00486ANS")