import PIL
from PIL import Image, ImageDraw

#########FILE MANAGEMENT#######
fpath = 'flag.txt'
f = open(fpath)
l = f.readlines()
lines = []
for i in l:
    lines.append(i[:-1].split(','))

lines = [[int(s) for s in sublist] for sublist in lines]

#########IMAGE DRAWING#######
sizex = 656
sizey = 100

def iterate():
    glob = 0
    y = 0
    while (glob < len(lines)) and (y < sizey):
        x = 0
        y += 1
        while x <= sizex:
            if glob < len(lines):
                draw.point([x, y], tuple(lines[glob]))
            x += 1
            glob += 1
    print 'done'

print 'images printing'


img = Image.new("RGB", (sizex, sizey))
draw = ImageDraw.Draw(img)
iterate()
img.save('img.png')

print 'done'
