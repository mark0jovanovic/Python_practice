ime = "Benjamin"
print(ime.lower())
print(ime.upper())
ime2 = "benjamin"

print(ime.lower() == ime2.lower())
print(ime.count("n"))
print("n" in ime)

print(ime.find('e'))

i = ime.index('n')
ime = ime[:i] + 'r' + ime[i +1:]
print(ime)

print(ime.ljust(15))
ime.splitlines()

