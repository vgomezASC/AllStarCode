from Processing import *
x = 300
y = 460
bulletY=460
def setup():
    window(650,650)
    background(0,0,0)
    fill(0,0,0)
setup()
def draw():
    fill(255,255,255)
    rect(x,y,100,20)
    fill(255,255,255)
    ellipse(50,50,50,50)
    fill(255,255,255)
    ellipse(200,50,50,50)
    fill(255,255,255)
    ellipse(350,50,50,50)
    fill(255,255,255)
    ellipse(500,50,50,50)
draw()

    
     
## while left < 400:
## while True:
##     if isKeyPressed() == True:
##         print( 'key pressed is ' + str(key(leftKey)) + ' and has code ' + str( keyCode(left) ) )
##     delay(5)

while True:
    global x
    global bulletY
    if isKeyPressed() == True:
        if keyCode()=='Left':
            if (x-3)> 0:
                x=x-3
            background(0,0,0)
            draw()
            delay(10)
        elif keyCode() == 'Right':
            if (x+3)<550:       
                x=x+3
            background(0,0,0)
            draw()
            delay(10)
        elif keyCode() == 'a':
            bulletY = 460
            while bulletY>0: 
                fill(255)
                ellipse(x+50,bulletY,10,10)
                bulletY=bulletY-10
                delay(10)
                background(0,0,0)
                draw()    
       
                
        