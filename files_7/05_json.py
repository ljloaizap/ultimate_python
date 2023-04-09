import json
from pathlib import Path


# # write json
# products = [
#     {"id": 1, "name": "Surfboard"},
#     {"id": 2, "name": "Bicycle"},
#     {"id": 3, "name": "Skate"},
# ]
# data = json.dumps(products)
# Path('files_7/products.json').write_text(data)


# # read json
# data = Path('files_7/products.json').read_text(encoding='utf-8')
# products = json.loads(data)
# print(products)


# modify json
data = Path('files_7/products.json').read_text(encoding='utf-8')
products = json.loads(data)
products[0]['name'] = 'Chanchito feliz'
Path('files_7/products.json').write_text(json.dumps(products))
