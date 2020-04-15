import requests
from fake_headers import Headers
from bs4 import BeautifulSoup

import requests


url = "https://opensky-network.org/api/states/all"


response = requests.request("GET", url)

