teze = [74, 65, 82, 84, 76]
imena = ['ana',
         'benjamin',
         'cilka',
         'dani',
         'ema',]
je_zenska = [True, False, True, False, True]
najveca = 0
for teza in teze:
    if teza > najveca:
        najveca = teza
print(najveca)
sami_lahki = True


for teza in teze:
    if teza >= 80:
        sami_lahki = False
if sami_lahki:

    print("sami lahki")
else:
    print("  saj en je debel")

tocka = 87, 6
print(tocka)
x, y = tocka
print(x, y)


osebe = [
    ("Ana", 74, True),
    ("ema", 65, True),
    ("Dani", 84, False),
    ("Cilka", 82,True),
    ("Benjamin", 76, False),
]
for ime, teza, je_zenaska in osebe:
    if not je_zenaska:
        print(ime, ":", teza)



