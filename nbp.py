import json
import urllib.request as req
import matplotlib.pyplot as plt
from calendar import monthrange

# install in the system
# pip matplotlib

def nbp_currency(cur,month, year):
    week, lastday = monthrange(year, int(month))
    adres = "http://api.nbp.pl/api/exchangerates/rates/A/{0}/{1}-{2}-01/{1}-{2}-{3}?format=json".format(cur,year,month,lastday)
    # source = req.urlopen(adres)
    # data = source.read().decode()
    # source.close()
    with req.urlopen(adres) as url:
        data = json.loads(url.read().decode())
    return data

currency = "gbp"
data  = nbp_currency(currency, '03', 2021)

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
plt.xlabel("Dni miesiąca ")
plt.ylabel("Kurs "+currency)
plt.legend()
plt.savefig("out/kurs_euro.png")
plt.show()