number = float(input("Tell me the number: "))
if number % 2 == 0:
    print(int(number), "is even")
elif number % 2 == 1:
    print(int(number), "is odd")
else:
    print(number, "is very strange")