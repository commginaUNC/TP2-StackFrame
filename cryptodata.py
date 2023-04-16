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
url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
#el header es para enviar la solicitud HTTP a la API de CoinAPI.
headers = {"X-CMC_PRO_API_KEY": api_key}
params = {"symbol": ",".join(cryptos)}
response = requests.get(url, headers=headers, params=params)
data = response.json()
prices = {}

for crypto, info in data["data"].items():
    prices[crypto] = float(info["quote"]["USD"]["price"])

# mostrar los precios obtenidos
for crypto, price in prices.items():
    print(f"El precio de {crypto} en dolares es: {price}")




result = subprocess.run(["./calc", str(210), str(prices['BTC'])], stdout=subprocess.PIPE)
print(f"El precio de BTC en ARS es: {result.stdout}")

result = subprocess.run(["./calc", str(210), str(prices['ETH'])], stdout=subprocess.PIPE)
print(f"El precio de BTC en ARS es: {result.stdout}")

result = subprocess.run(["./calc", str(1.1), str(prices['BTC'])], stdout=subprocess.PIPE)
print(f"El precio de BTC en EUROS es: {result.stdout}")

result = subprocess.run(["./calc", str(1.1), str(prices['ETH'])], stdout=subprocess.PIPE)
print(f"El precio de ETH en EUROS es: {result.stdout}")
