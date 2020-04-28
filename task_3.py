import turtle

s = turtle.Pen()


def function (n, side):
    s.lt(side)
    for _ in range(n):
        s.fd(100)
        s.lt(360/n)


function(8, 50)
