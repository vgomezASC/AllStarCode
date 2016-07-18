from Processing import *
window (500,500)
rectMode(CORNER)
fill(0, 0, 255)
rect(0, 0, 166.66, 150)
fill(255,0,0)
rect(167,0,166.66,150)
fill(0,255,0)
rect(333,0,166.66,150)



def doMouseDragged():
   line(pmouseX(), pmouseY(), mouseX(), mouseY())
   blue = fill(0,0,255)
   stroke(blue)
   red = fill(255,0,0)
   green = fill(0,255,0)

onMouseDragged += doMouseDragged

def doMouseClicked():
    print( 'mouse clicked at ' + str(mouseX()) + ', ' + str(mouseY()) )
    x = mouseX() 
    y = mouseY()
    if x <= 166.66:
        print ("hi")
    if y <= 150:
        print ("hi1")
onMouseClicked += doMouseClicked
