from Processing import *
size (500,500)
background (152,245,255)
x = 25
y = 250
xdirection = "positive"
ydirection = "positive"
ellipse (x,y,50,50)
while True:
    ellipse (x,y,50,50)
    if x > 475:
        xdirection = "negative"
    elif x < 0:
        xdirection = "positive"    
    if y > 475:
        ydirection = "negative"
    elif y < 0:
        ydirection = "positive"
    if xdirection == "positive": 
        x = x + 1
    else: 
        x = x - 1
    if ydirection == "positive":
        y = y + 1
    else: 
        y = y - 1
    delay(1)         
        
          
#Make Ball move in random direction








#