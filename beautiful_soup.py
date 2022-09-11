import requests
from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
                        '(KHTML,like Gecko) Chrome/100.0.4896.75 Safari/537.36'}

usd_eur_change = 'https://www.bloomberg.com/quote/USDEUR:CUR'

coin_list = ['BTC', 'ETH', 'BNB', 'BCH', 'LINK', 'LUNA', 'ATOM', 'SOL', 'USDT', 'EUR']

url = 'https://www.eleconomista.es/cruce/EURUSD'

url_list = {
    'btc_v': 'https://www.binance.com/en/price/bitcoin',
    'eth_v': 'https://www.binance.com/en/price/ethereum',
    'bnb_v': 'https://www.binance.com/en/price/bnb',
    'bch_v': 'https://www.binance.com/en/price/bitcoin-cash',
    'link_v': 'https://www.binance.com/en/price/link',
    'luna_v': 'https://www.binance.com/en/price/luna',
    'atom_v': 'https://www.binance.com/en/price/cosmos',
    'sol_v': 'https://www.binance.com/en/price/solana',
    'usdt_v': 'https://www.binance.com/en/price/tether',
}

a = requests.get(url_list['btc_v'])
soup0 = BeautifulSoup(a.text, 'html.parser')
b = requests.get(url_list['eth_v'])
soup1 = BeautifulSoup(b.text, 'html.parser')
c = requests.get(url_list['bnb_v'])
soup2 = BeautifulSoup(c.text, 'html.parser')
d = requests.get(url_list['bch_v'])
soup3 = BeautifulSoup(d.text, 'html.parser')
e = requests.get(url_list['link_v'])
soup4 = BeautifulSoup(e.text, 'html.parser')
f = requests.get(url_list['luna_v'])
soup5 = BeautifulSoup(f.text, 'html.parser')
g = requests.get(url_list['atom_v'])
soup6 = BeautifulSoup(g.text, 'html.parser')
h = requests.get(url_list['sol_v'])
soup7 = BeautifulSoup(h.text, 'html.parser')
i = requests.get(url_list['usdt_v'])
soup8 = BeautifulSoup(i.text, 'html.parser')
soups = [soup0, soup1, soup2, soup3, soup4, soup5, soup6, soup7, soup8]


r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
#
price_eur_usd = soup.find('span', {'class': "ultimo_321 last-value"}).text[:7]
price0 = price_eur_usd[0:6]
price = float(price0.replace(',', '.'))
price = round(price, 8)
