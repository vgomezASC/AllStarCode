from Myro import *
Yuno = makePicture("Deadpool.JPG")
show(Yuno)
Pixels=getPixels(Yuno)
ObamaDarkBlue = makeColor(0,51,76)
ObamaRed = makeColor(217, 26, 33)
ObamaBlue = makeColor(112,150,158)
ObamaYellow = makeColor(252, 227, 166)
for i in Pixels:
    greyPixels=getGray(i)
    if greyPixels>180:
        setColor(i,ObamaYellow)
    elif greyPixels>120 and greyPixels<180:
        setColor(i,ObamaBlue)
    elif greyPixels>60 and greyPixels<120:
        setColor(i,ObamaRed)
    else: 
        setColor(i,ObamaDarkBlue)