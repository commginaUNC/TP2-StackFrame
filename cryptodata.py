import requests
import configparser
import subprocess

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
    data = response.json()
    prices[crypto] = float(data["rate"])

# mostrar los precios obtenidos
for crypto, price in prices.items():
    print(f"El precio de {crypto} en dolares es: {price}")



result = subprocess.run(["./calc", str(210), str(prices['BTC'])], stdout=subprocess.PIPE)
print(f"El precio de BTC en ARS es: {result.stdout}")

result = subprocess.run(["./calc", str(210), str(prices['ETH'])], stdout=subprocess.PIPE)
print(f"El precio de BTC en EUROS es: {result.stdout}")

result = subprocess.run(["./calc", str(1.1), str(prices['BTC'])], stdout=subprocess.PIPE)
print(f"El precio de BTC en ARS es: {result.stdout}")

result = subprocess.run(["./calc", str(1.1), str(prices['ETH'])], stdout=subprocess.PIPE)
print(f"El precio de ETH en EUROS es: {result.stdout}")
