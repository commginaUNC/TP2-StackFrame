import requests
import configparser
import ctypes
import msl.loadlib
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


libconvert = msl.loadlib.load_library('/libconvert.so')

calculadora = libconvert.asm_calculadora

calculadora.argtypes = [ctypes.c_int, ctypes.c_int]
calculadora.restype = ctypes.c_int


print(calculadora(213,int(prices['BTC'])))