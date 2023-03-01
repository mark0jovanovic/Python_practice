lst = [1, 2, 3]
lst.clear()
print(lst)

#------------------

a = [1, 2, 3]
b = a
b[1] = 4
print(b)
print(a)

c = [1, 2, 3]
z = c.copy()
z[1] = 4
print(c)
print(z)


#count
#-----------------------
to_be = ['to', 'be', 'or', 'not', 'to', 'be'].count('to')
print(to_be)

x = [[1, 2], 1, 1, [2, 1, [1, 2]]]
print(x.count(1))
print(x.count([1, 2]))

#extand
#----------------------

a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)

print(a)


#index
#------------------------


knights = ['We', 'are', 'the', 'knights', 'who', 'say', 'ni']
knight = knights[4]

print(knight)
knight_num = knights.index('who')
print(knight_num)

#insert
#---------------------

numbers = [1, 2, 3, 5, 6, 7]
numbers.insert(3, 'four')
print(numbers)

numbers[4:4] = ["Four"]
print(numbers)

#pop
#---------------------
x = [1, 2, 3]
x.pop()
print(x)
x.pop(0)
print(x)

#remove
#----------------------

x = ['to', 'be', 'or', 'not', 'to', 'be']
x.remove('be') #only first mach is deleted
print(x)

#reverse
#---------------------

x = [1, 2, 3]
x.reverse()
print(x)


#sort
#----------------------
x = [4, 6, 2, 1, 7, 9]
print(x.sort())
print(x)

c = [4, 6, 2, 1, 7, 9]
y = sorted(c)
print(y)

x = ['aardvark', 'abalone', 'acme', 'add', 'aerate']
x.sort(key=len)
print(x)


x = [4, 6, 2, 1, 7, 9]
x.sort(reverse=True)
print(x)








