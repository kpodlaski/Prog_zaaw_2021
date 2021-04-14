import json
import urllib.request as req
import matplotlib.pyplot as plt
from calendar import monthrange
from statistics import mean, median

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

def currency_stats(cur, days, mids):
    stats = { 'currency':cur,
              'max':max(mids), 'min':min(mids),
              'mean':mean(mids), 'median':median(mids)
            }
    print("Waluta", cur)
    print("Maksymalna wartość:",stats['max'])
    print("Minimalna wartość:",stats['min'])
    print("Średnia wartość:",stats['mean'])
    print("Mediana:", stats['median'])
    return stats


currency = "eur"
month = "03"
year = 2021
data  = nbp_currency(currency, month, year)

print(data['currency'])
print(data['rates'])

days = []
mids = []
for el in data['rates']:
    days.append(int( el['effectiveDate'][-2:]))
    mids.append(el['mid'])

#print(days)
#print(mids)
stats = currency_stats(currency,days=days, mids=mids)

plt.plot(days,mids, label="Trend")
plt.plot([days[0],days[-1]],[stats['mean'],stats['mean']], c='green', linestyle='--', label='średnia')
plt.plot([days[0],days[-1]],[stats['median'],stats['median']], c='violet', linestyle=':', label='mediana')
plt.scatter(days,mids, c='red', label="Dane rzeczywiste")
plt.xlabel("Dni miesiąca ")
plt.ylabel("Kurs "+currency)
plt.legend()
plt.savefig("out/kurs_euro.png")
plt.show()

## znaleźć
# min, max, średnią i medianę
# dla wybranej waluty w miesiącu

