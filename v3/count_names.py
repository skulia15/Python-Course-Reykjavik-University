from urllib.request import urlopen
from urllib.parse import urlencode
import json

def count_names(start):
    url = "https://mooshak.ru.is/~python/names.json"
    resp = urlopen(url)
    first = 0
    second = 0
    data = json.loads(resp.read().decode('utf-8'))
    res = [x for x in data if str(x['Nafn']).startswith(start)]
    for x in res:
        first += x.get('Fjoldi1')
        second += x.get('Fjoldi2')
    ans = (first, second)
    return ans
x = count_names("Theodóra Hanna")
print(x)