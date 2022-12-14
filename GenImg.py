from PIL import Image, ImageDraw
Resolution = (2560,1440)
Canvas = open("Canvas.txt","r")
Img = Image.new("RGB",(Resolution), color=(50,50,50))
d = ImageDraw.Draw(Img)
pixelwidth = int((Resolution[0])/6)
pixelheight = int(Resolution[1]/10)

LineList = []
for line in Canvas:
    line = line.replace("\n", "")
    List = line.split("<")
    List.pop(0)
    LineList.append(List)




for x in range(0,pixelheight):
  for y in range(0,pixelwidth):
    d.text((y*6,x*10),LineList[x][y], fill=(50,200,255))
Img.save("*Out.png")