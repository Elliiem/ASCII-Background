Canvas = open("Canvas.txt","r")
Out = open("Out.txt","w")
LineList = []
for line in Canvas:
    line = line.replace("\n", "")
    List = line.split("<")
    List.pop(0)
    List.pop(-1)
    LineList.append(List)

def DrawHor(Pos1,Pos2,Row):
    Pos1 = int(Pos1/2-1)
    Pos2 = int((Pos2)/2-1)
    Line = LineList[Row-1]
    Len = int(Pos2-Pos1)
    for x in range(0,Len):
     Pos = int(x+Pos1)
     Line[Pos] = "-"
    Line[Pos1] = "#"
    Line[Pos2] = "#"



def DrawVert(Row1,Row2,Line):
    Line = int(Line/2-1)
    len = int(Row2-Row1)
    for x in range(Row1-1,Row2):
        LineList[x][Line] = "|"
    LineList[Row1-1][Line] = "#"
    LineList[Row2 - 1][Line] = "#"


def ClearLine(Row):
    for x in range(0,len(LineList[Row-1])):
        LineList[Row-1][x] = " "

def ClearVert(Pos):
    Pos = int(Pos/2-1)
    for x in range(0,len(LineList)):
        LineList[x][Pos] = " "

def Save():
 for x in range(0,len(LineList)):
  Out.write("<")
  for y in range(0,len(LineList[x])):
    Out.write(LineList[x][y])
    Out.write("<")
  if x != len(LineList)-1:
   Out.write("\n")





DrawHor(40,50,30)





Save()