from bs4 import BeautifulSoup
import requests

def crawl_nvidia_stock():
    url = 'https://finance.yahoo.com/quote/NVD/'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        stock_price = soup.find('fin-streamer', {'data-field': 'regularMarketPrice'}).text
        stock_price_change_today = soup.find('fin-streamer', {'data-field': 'regularMarketChangePercent'}).text

        return {
            'stock_price': stock_price,
            'stock_price_change_today': stock_price_change_today
        }
    else:
        return None

print(crawl_nvidia_stock())