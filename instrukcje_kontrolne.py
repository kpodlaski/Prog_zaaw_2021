elements = ['Adam', 'Alicja', 'Olaf', 'Elżbieta']

for x in elements:
    print(x)

for x in range(2,5):
    print(x)

for x in range(len(elements)):
    print(x, elements[x])

print(range(6), type(range(6)))

my_range = list(range(6))
print(my_range, type(my_range))

cond = True
i =1
while cond:
    print(cond)
    # i++ nie ma inkrementacji w pythonie
    i+=1
    if i>3:
        cond = False
    #elif warunek:
    else:
        print("dalej")

mapa = {
    2 : "Alabama",
    'imie': 'Ala',
    'wiek':33
}

for index in mapa.keys():
    print(index, '->', mapa[index])

zbior = {'Ala', "Alan", "Ala", "Tomasz"}
print(zbior, type(zbior))