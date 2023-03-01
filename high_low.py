number = 7
guess = -1

print("Guess the number!")
while guess != number:
    guess = int(input("Is it.. "))

    if guess == number:
        print("Bravo")
    elif guess < number:
        print("Its bigger..")
    elif guess > number:
        print("Its smaller..")