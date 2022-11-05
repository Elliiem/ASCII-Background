Resolution = (2560,1440)
pixelwidth = int((Resolution[0])/6)
pixelheight = int(Resolution[1]/10)
Canvas = open("TsT","w")


for Row in range(0,pixelheight):
    Canvas.write("<")
    for Pixel in range(0,pixelwidth):
        Canvas.write(" "+"<")
    Canvas.write("\n")