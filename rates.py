from beautiful_soup import price, soups, coin_list
import json


lista_valores = []
for s in soups:
    s = s.find('div', {'class': 'css-12ujz79'}).text[2:]
    lista_valores.append(s)

lista_valores_ok = []
for e in lista_valores:
    if ',' in e:
        e = e.replace(',', '')
        n = float(e)
        n = round(n/price, 8)
        lista_valores_ok.append(n)
    else:
        n = float(e)
        n = round(n/price, 8)
        lista_valores_ok.append(n)

lista_valores_ok.append(1.00)
# print(lista_valores_ok)

#Precios en EUR por 1 cripto
coin_values_EUR = dict(zip(coin_list, lista_valores_ok))
for key, value in coin_values_EUR.items():
    value1 = float(value)

#Precios de cada cripto por 1 EUR
coin_values_1EUR = []
for key, value in coin_values_EUR.items():
    v = float(value)
    va = 1 / value
    coin_values_1EUR.append(va)
    eur_values = dict(zip(coin_list, coin_values_1EUR))

#Precios de cada cripto por 1 BTC
coin_values_1BTC = []
for key, value in coin_values_EUR.items():
    b = float(value)
    bit = coin_values_EUR['BTC'] / value
    coin_values_1BTC.append(bit)
    btc_values = dict(zip(coin_list, coin_values_1BTC))

#Precios de cada cripto por 1 ETH
coin_values_1ETH = []
for key, value in coin_values_EUR.items():
    b = float(value)
    bit = coin_values_EUR['ETH'] / value
    coin_values_1ETH.append(bit)
    eth_values = dict(zip(coin_list, coin_values_1ETH))

#Precios de cada cripto por 1 BNB
coin_values_1BNB = []
for key, value in coin_values_EUR.items():
    b = float(value)
    bit = coin_values_EUR['BNB'] / value
    coin_values_1BNB.append(bit)
    bnb_values = dict(zip(coin_list, coin_values_1BNB))

#Precios de cada cripto por 1 BCH
coin_values_1BCH = []
for key, value in coin_values_EUR.items():
    b = float(value)
    bit = coin_values_EUR['BCH'] / value
    coin_values_1BCH.append(bit)
    bch_values = dict(zip(coin_list, coin_values_1BCH))

#Precios de cada cripto por 1 LINK
coin_values_1LINK = []
for key, value in coin_values_EUR.items():
    b = float(value)
    bit = coin_values_EUR['LINK'] / value
    coin_values_1LINK.append(bit)
    link_values = dict(zip(coin_list, coin_values_1LINK))

#Precios de cada cripto por 1 LUNA
coin_values_1LUNA = []
for key, value in coin_values_EUR.items():
    b = float(value)
    bit = coin_values_EUR['LUNA'] / value
    coin_values_1LUNA.append(bit)
    luna_values = dict(zip(coin_list, coin_values_1LUNA))

#Precios de cada cripto por 1 ATOM
coin_values_1ATOM = []
for key, value in coin_values_EUR.items():
    b = float(value)
    bit = coin_values_EUR['ATOM'] / value
    coin_values_1ATOM.append(bit)
    atom_values = dict(zip(coin_list, coin_values_1ATOM))

#Precios de cada cripto por 1 SOL
coin_values_1SOL = []
for key, value in coin_values_EUR.items():
    b = float(value)
    bit = coin_values_EUR['SOL'] / value
    coin_values_1SOL.append(bit)
    sol_values = dict(zip(coin_list, coin_values_1SOL))

#Precios de cada cripto por 1 USDT
coin_values_1USDT = []
for key, value in coin_values_EUR.items():
    b = float(value)
    bit = coin_values_EUR['USDT'] / value
    coin_values_1USDT.append(bit)
    usdt_values = dict(zip(coin_list, coin_values_1USDT))


keys_dict = ['BTC', 'ETH', 'BNB', 'BCH', 'LINK', 'LUNA', 'ATOM', 'SOL', 'USDT', 'EUR']
values_dict = [btc_values, eth_values, bnb_values, bch_values, link_values, luna_values, atom_values,
            sol_values, usdt_values, eur_values]



dict_final = dict(zip(keys_dict, values_dict))
dictionary = json.dumps(dict_final, indent=4)

