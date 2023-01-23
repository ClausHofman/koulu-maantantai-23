import time
from time import ctime
from pprint import pformat, pprint

aikaleima = time.time()

# print(aikaleima)

# aikateksti = time.ctime(aikaleima)

# print(aikateksti)

# aika1 = time.time()

# time.sleep(3)

# aika2 = time.time()

# print(time.ctime())

# print(aika1)
# print(aika2)
# print(round(aika2 - aika1))

esimerkki_kuvio = {
    'a':'a1',
    'b':'b1',
    'luotu': ctime(aikaleima),
    'c': [
        {'x': 10, 'y': 20, 'z':30},
        {'x': 10, 'y': 20, 'z':30},
        {'x': 10, 'y': 20, 'z':30},
    ]
}

pprint(esimerkki_kuvio, sort_dicts=False)

esimerkki_kuvio_muotoiltu_teksti = pformat(esimerkki_kuvio, sort_dicts=False)

print("Muotoiltu teksti:\n", esimerkki_kuvio_muotoiltu_teksti.upper())