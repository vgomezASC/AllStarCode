from random import randrange
print "hi"
def setup():
    size(500, 500)

def draw():
    noStroke()
    colorMode(RGB, 200)
    for i in range(200):
        for j in range(200):
            stroke(i, j, 0)
            point(i, j)
    x = randrange(5,50)
    y = randrange(5,50)
    ellipse(mouseX, mouseY, x, y)
    stroke
    