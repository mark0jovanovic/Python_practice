demolist = ["Life", 42, "the universe", 6, "and", 9]
print("demolist = ", demolist)
demolist.append("everything")
print("after 'everything' was appended demolist is now: ")
print(demolist)
print("len demolist: ", len(demolist))
print("demolist.index(42): ", demolist.index(42))
print(demolist[1], 'demolist[1]')
for c in range(len(demolist)):
    print('demolist[',c,"] = ", demolist[c])
del demolist[2]
print("After the universe is removed demolist is now")
print(demolist)
if 'Life' in demolist:
    print("life is found in demolist")
else:
    print("life is not found in demolist")
another_list = [42, 7, 0, 123]
another_list.sort()
print(another_list)

for c, x in enumerate(demolist):
    print("demolist[",c,"] =  ", x)


