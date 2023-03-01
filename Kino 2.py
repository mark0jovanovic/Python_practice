filmi = ['Poletje v skoljki 2', 'Ne cakaj na maj', 'Pod njenim oknom', 'Kekec', 'Poletje v skoljki', 'To so gadi']
ocene = [6.1, 7.3, 7.1, 8.1, 7.2, 7.7]
nova_lista = []
nova_lista.append(list(zip(filmi, ocene)))
print(nova_lista)
space = " "
for film_zoceno in nova_lista:
    print(film_zoceno)
    for film, ocena in film_zoceno:
        if len(film.split(" "))  == 3:
            print(film, "(",ocena,")")



