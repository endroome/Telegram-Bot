import os
from dotenv import load_dotenv, find_dotenv
import requests

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_KEY = os.getenv("API_KEY")
DEFAULT_COMMANDS = (
    "/start", "Начать диалог",
    "/low", "Вывод информации по минимальным показателям поиска.",
    "/high", "Вывод информации по максимальным показателям поиска.",
    "/custom", "Вывод информации показателей по пользовательскому вводу.",
    "/history", "История запросов пользователей",
)

command = {}


def get():
    url = API_KEY
    products = []
    result = requests.get(url).json()
    products_row = result.get('data', {}).get('products', None)

    if products_row is not None and len(products_row) > 0:
        for elem in products_row:
            products.append({
                'brand': elem.get('brand', None),
                'name': elem.get('name', None),
                'sale': elem.get('sale', None),
                'priceU': float(elem.get('priceU', None)) / 100 if elem is not None else None,
                'salePriceU': float(elem.get('salePriceU', None)) / 100 if elem is not None else None,
                'supplier': elem.get('supplier', None),
                'supplierRating': float(elem.get('supplierRating', None)),
                'id': elem.get('id', None)
            })
    return products


result_get = get()
sorted_low = sorted(result_get, key=lambda x: x['salePriceU'])
sorted_high = sorted(result_get, key=lambda x: x['salePriceU'], reverse=True)
