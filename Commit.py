Out = open("Out.txt","r")
Canvas = open("Canvas.txt","w")

for line in Out:
    Canvas.write(line)

