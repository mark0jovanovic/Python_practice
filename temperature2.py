def print_optons():
    print("Options:")
    print("  'p' print options")
    print("  'c' convert from Celsius")
    print("  'f' convert from Farenheit")
    print("  'q' quit the program")
def celsius_to_fahrenheit(c_temp):
    return 9.0 / 5.0 * c_temp + 32

def fahrenheit_to_celsius(f_temp):
    return (f_temp - 32.0) * 5.0 / 9.0

choice = "p"
while choice != "q":
    if choice == "c":
        c_temp = float(input("Celsius temperature: "))
        print("Fahrenheit: " , celsius_to_fahrenheit(c_temp))
        choice = input("Option: ")
    elif choice == "f":
        f_temp = float(input("Fahrenheit temperatur: "))
        print("Celsius:", fahrenheit_to_celsius(f_temp))
        choice = input("option: ")
    else:
        choice = "p"

        print_optons()
        choice = input("options: ")