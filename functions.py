def hello():
    print("Hello!")
def area(width, heght):
    return width * heght
def print_welcome(name):
    print("Welcome", name)

hello()
hello()

print_welcome("Marko")
w = 4
h = 5
print("width = ", w, "height = ", h, "area = ", area(w,h))
