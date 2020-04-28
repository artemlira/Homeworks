import turtle

c = turtle.Pen()
c.rt(90)


def cir(radius):
    for a in range(11):
        c.circle(radius)
        radius += 7


cir(7)
c.lt(180)
cir(7)
