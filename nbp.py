import json
import urllib.request as req
import matplotlib.pyplot as plt

# install in the system
# pip matplotlib

adres = "http://api.nbp.pl/api/exchangerates/rates/A/EUR/2021-03-01/2021-03-31?format=json"
# source = req.urlopen(adres)
# data = source.read().decode()
# source.close()
with req.urlopen(adres) as url:
    data = json.loads(url.read().decode())

print(data['currency'])
print(data['rates'])

days = []
mids = []
for el in data['rates']:
    days.append(int( el['effectiveDate'][-2:]))
    mids.append(el['mid'])

print(days)
print(mids)

plt.plot(days,mids, label="Trend")
plt.scatter(days,mids, c='red', label="Dane rzeczywiste")
plt.xlabel("Dni miesiąca")
plt.ylabel("Kurs EURO")
plt.legend()
plt.savefig("out/kurs_euro.png")
plt.show()