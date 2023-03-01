def hello():
    print('Hello!')

def areaRec(width, height):
    return width * height
def areaScq(width):
    return width ** 2
def areCerc(radius):
    return 3.14 * radius ** 2
def print_welcome(name):
    print('Welcome, ', name)

def positive_input(prompt):
    number = float(input(prompt))
    while number <= 0:
        print("Must be positive number")
        number = float(input(prompt))
    return number
def print_optons():
    print("Options:")
    print("  'p' print options")
    print("  'c' area of the circle")
    print("  's' area of the square")
    print("  'r' area of the rectangle")
    print("  'q' quit the program")

name = input('Your name: ')
hello()
print_welcome(name)
print_optons()
print()

print('To find the area,')
print('enter the info below.')
choice = input("Enter option : ")

while 1 == 1:
    if choice == 's':
        width = float(input("Enter width: "))
        print("Area is: " , areaScq(width))
        break





    elif choice == 'r':
        width = float(input("Enter width: "))
        height = float(input("Enter a height: "))
        print("Area is: " ,areaRec(width,height))
        break


    elif choice == 'c':
        radius = float(input("Enter a radius: "))
        print("Area  is: ", areCerc(radius))
        break

    elif choice == 'q':
        break
    else:
        choice = 'p'
print("Kraj")










