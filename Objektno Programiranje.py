from math import radians, cos, sin

import risar


class Turtle:
    def __init__(self):
        self.x = risar.maxX / 2
        self.y = risar.maxY / 2
        self.angle = 0
        self.__body = risar.krog(self.x, self.y, 15 , barva=risar.zelena, sirina=3)
        self.__head = risar.krog(self.x, self.y -15, 5,  barva=risar.zelena, sirina=3)
        self._distance = 0
        self.pan_active = True
    def distance(self):
        return  self.distance
    def _update(self):
         self.__body.setPos(self.x, self.y)
         beta = radians(90 - self.angle)
         self.__head.setPos(self.x + 15 * cos(beta), self.y - 15 * sin(beta))
    def forward(self, a):
        beta = radians(90 - self.angle)
        nx = self.x + a * cos(beta)
        ny = self.y - a * sin(beta)
        if self.pen_active:
            risar.crta(self.x, self.y, nx, ny, sirina=2)
        self.x = nx
        self.y = ny
        self._update()
        self._distance += abs(a)





    def turn(self, phi):
        self.angle += phi
        self._update()

    def bacward(self, a):
        self.forward(-a)
        self._update()

    def left(self):
        self.angle -= 90
        self._update()

    def right(self):
        self.angle += 90
        self._update()

    def fly(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self._update()
    def pen_up(self):
        self.pen_active = False

    def pen_down(self):
        self.pen_active = True



ana = Turtle()
ana.fly(400,110,90)
ana.forward(100)
ana.left()
ana.forward(30)
ana.right()
ana.forward(30)
ana.left()
ana.forward(30)
print(ana.distance())





risar.stoj()