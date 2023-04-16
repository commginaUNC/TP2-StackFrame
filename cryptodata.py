import requests
import configparser
import ctypes
import msl.loadlib
from msl.loadlib import LoadLibrary
import os
#request es una libreria para hacer solicitudes http en python

# leer la clave de API desde el archivo de configuración
config = configparser.ConfigParser()
config.read('config.ini')
api_key = config['coinapi']['api_key']

# definir las criptomonedas de interés
cryptos = ["BTC", "ETH"]

# solicitud a la API de CoinAPI para obtener los precios
url = "https://rest.coinapi.io/v1/exchangerate/{crypto}/USD"
#el header es para enviar la solicitud HTTP a la API de CoinAPI.
headers = {"X-CoinAPI-Key": api_key}
prices = {}
for crypto in cryptos:
    response = requests.get(url.format(crypto=crypto), headers=headers)
    #la respuesta de coinAPI se hace en json
    #el valor del precio en dolares se encuentra en el campo rate del json
    prices[crypto] = float(response.json()["rate"])

    #print(response.json())
    
# mostrar los precios obtenidos
for crypto, price in prices.items():
    print(f"El precio de {crypto} en dolares es: {price}")


lib_path = os.path.abspath('libconvert.so')
libconvert = LoadLibrary(lib_path)
calculadora = libconvert.lib.asm_calculadora


btc_pesos = calculadora(213,int(prices['BTC']))
eth_pesos = calculadora(213,int(prices['ETH']))

btc_euros = calculadora(1.1,int(prices['BTC']))
eth_euros = calculadora(1.1,int(prices['BTC']))


print(f"El precio de BTC en ARS es: {btc_pesos}")
print(f"El precio de ETH en ARS es: {eth_pesos}")
print(f"El precio de BTC en EUR es: {btc_euros}")
print(f"El precio de ETH en EUR es: {eth_euros}")
