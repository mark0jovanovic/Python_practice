filmi = [
    ('Poletje v skoljki 2', 6.1),
    ('Ne cakaj na maj', 7.3),
    ('Pod njenim oknom', 7.1),
    ('Kekec', 8.1),
    ('Poletje v skoljki', 7.2),
    ('To so gadi', 7.7),
]
film_7 =[]
for film ,ocena in filmi:
    if ocena >= 7:
        film_7.append(film)
        print(film)
ocene_filmi = []
poprecna_ocena = 0
stevec = 0
for film, ocena in filmi:
    ocene_filmi.append((ocena, film))
    poprecna_ocena += ocena
    stevec +=1

    ocene_filmi.sort()



print(ocene_filmi[-1][1])
print(film_7[0])
print("{:.2f}".format(poprecna_ocena / stevec))
for film, ocena in filmi:
    if '2' in film:
        print(film)


