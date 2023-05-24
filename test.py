from pprint import pprint
from requests import get

response = get(url="https://api.npoint.io/c790b4d5cab58020d391", timeout=10)
response.raise_for_status()

pprint(response.json())
