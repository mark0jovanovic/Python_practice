x = int(input("Unesi stevilo"))
svota = 0
for n in range(1, x +1):
    if (x % n) == 0:
        svota += n

svota -= x
if svota == x:
    print("Stevilo je popolno")