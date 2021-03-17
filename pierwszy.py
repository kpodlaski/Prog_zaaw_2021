'''
v = 13
print(v)
print(type(v))
v = "ABC"
print(v)
print(type(v))
print(v+str(2))
print(3+3.5)
'''

def nazwa_funkcji(a, b=1, c=2):
    x = a*a
    a=x/2
    print('wartość', x, a)
    print('c',c)
    return x, 2*c, b

a = 3
v = nazwa_funkcji(a, c=3, b=13)

print('po funkcji ', a)
print(v, type(v))
print(v[2])

x1, x2, x3 = nazwa_funkcji(2,4,6)
print(x2)

a = (1, 3.4, '33')
print(a, type(a), 'ile tuple ma elemetów', len(a))
print(len('Ala ma kota'))

lista = [1,3,6,2.4]
print(lista, type(lista), len(lista), 'element drugi listy:', lista[1])

lista = [
    [1,3] ,
    [6,2.4]
]
print(lista, type(lista), len(lista), 'element drugi listy:', lista[1])

lista = [1,3,6,2.4]
lista.append(-1)
lista.sort()
print(lista)

# odpowieddnik mapy z c++
mapa = {
    2 : "Alabama",
    'imie': 'Ala',
    'wiek':33
}
print(mapa, mapa['imie'], mapa.keys())

