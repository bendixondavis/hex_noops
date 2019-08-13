import requests
import json
from colorama import Fore, Back, Style

data = requests.get('https://api.noopschallenge.com/hexbot').text
print(data)

data = json.loads(data)
for color in data['colors']:
    print_str = str(color['value'])
    print(print_str + 'Hello')
