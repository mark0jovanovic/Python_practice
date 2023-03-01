name = input("What is your username: ")
password = input("What is your Password: ")
command = None
input1 = None
input2 = None
while command != "lock":
    command = input("What is your command: ")
while input1 != name:
    input1 = input("What is your username: ")
while input2 != password:
    input2 = input("What is your password: ")
print("Welcome back")