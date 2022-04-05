import turtle
import sys
n = int(sys.argv[1])


def make_axiom(iters, axiom, rules):
    if not iters:
        return axiom
    begin = axiom
    end = ""
    for j in range(iters):
        end = "".join(rules[i] if i in rules else i for i in begin)
        begin = end
    return end


def line_moves(t, moves, angle, length):
    for move in moves:
        if move == 'F':
            t.forward(length)
        elif move == '+':
            t.right(angle)
        elif move == '-':
            t.left(angle)


def hilbert_draw(iterations, axiom, rules, angle, length=8, size=2, offset_angle=0):
    inst = make_axiom(iterations, axiom, rules)
    width = height = (4**n)+50
    y_offset = x_offset = -(3**n)/2
    trtle = turtle.Turtle()
    wndow = turtle.Screen()
    wndow.setup(width, height)
    trtle.up()
    trtle.backward(-x_offset)
    trtle.left(90)
    trtle.backward(-y_offset)
    trtle.left(offset_angle)
    trtle.down()
    trtle.speed(0)
    trtle.pensize(size)
    line_moves(trtle, inst, angle, length)
    trtle.hideturtle()
    wndow.exitonclick()


hilbert_draw(n, "L", {"L":"+RF-LFL-FR+", "R":"-LF+RFR+FL-"}, 90)