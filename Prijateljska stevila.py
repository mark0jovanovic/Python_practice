x = int(input("Unesi stevilo"))
delitelj =[]
delitelj1 = []
for n in range(1, x):
    if (x % n) == 0:
        delitelj.append(n)
#print(delitelj)
x1 = sum(delitelj)

for z in range(1, x1):
    if (x1 % z) == 0:
        delitelj1.append(z)
#print(delitelj1)
if sum(delitelj1) == x:
    print(sum(delitelj))
else:
    print(x, "nima prijateljev")



