format = "Hello, %s. %s enough for ya?"
print(format)
values = ('world',  'Hot')
n1 = format % values
print(n1)

from string import Template
tmpl = Template("Hello, $who! $what enough for ya?")
print(tmpl.substitute(who="Mars", what="Dusty"))


n2 = "{}, {} and {}".format("first", "second", "third")
print(n2)


#foramt je po indeksih.format(0 , 1 , 2 ,3 )
n3 = "{3} {0} {2} {1} {3} {0}".format("be", "or", "not", "to")
print(n3)

from math import  pi
n4 = "{name} is approximately {value:.2f}.".format(value=pi, name="π")
print(n4)

n6 = "{foo} {} {bar} {}".format(1, 2, bar=4, foo=3)
print(n6)
n7 = "{foo} {1} {bar} {0}".format(3, 1, bar=2, foo=0)
print(n7)


