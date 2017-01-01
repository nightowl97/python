from PIL import Image, ImageDraw

size = 2000

def stats_my_raws(rawfile):
    # get the datas
    f = open(rawfile)
    filedatas = f.read()
    f.close()
    raw_datas = filedatas.split('\n')

    for column in range(5):
        stats = {}
        for index, line in enumerate(raw_datas[:-1]):
            line = line.split(':')
            if line[column] in stats:
                stats[line[column]] += 1
            else:
                stats[line[column]] = 1
        # Print result
        print "Column %i stats :" % column
        for i in sorted(stats, key=stats.__getitem__, reverse=True):
            print "%s : %.02f %% - [%i]" % (i, 100.0 * stats[i] / len(raw_datas), stats[i])

def do_point(pos, draw, clr, size=2):#Print a point in the picture
    for x in range(size):
        for y in range(size):
            draw.point([pos[0]+x,pos[1]+y], fill=clr)

def resolv(filepath):
    # get the datas
    f = open(filepath)
    filedatas = f.read()
    f.close()
    raw_datas = filedatas.split('\n')

    # Create a Black/White image
    img = Image.new("L", (size, size), 0)  # Yep, a big one just to be sure
    draw = ImageDraw.Draw(img)
    pos = [3 * size / 4,  size / 4]  # We start at the center of it

    # Just to know the max size we really need
    min_pos = [size / 2, size / 2]
    max_pos = [size / 2, size / 2]

    for index, line in enumerate(raw_datas[:-1]):  # last value is '\n'. we don't need that
        print line
        datas = line.split(':')

        if len(datas) == 4: # just to filter bad input
            mouse_click = int(datas[0], 16)  # Fourth row is our "right click button"
            left_click = int(datas[3], 16)
            # Get the movments. it's signed 2bytes integer, so minus 0x100 if over 0x7f
            x_movement = int(datas[1], 16)
            if x_movement > 0x7f: x_movement -= 0x100
            y_movement = int(datas[2], 16)
            if y_movement > 0x7f: y_movement -= 0x100
            #
            pos[0] -= (x_movement) 
            pos[1] += (y_movement / 16.0) #y coordinates seemed to be multiples of 8
            # registering min/max value
            if pos[0] > max_pos[0]: max_pos[0] = pos[0]
            if pos[1] > max_pos[1]: max_pos[1] = pos[1]
            if pos[0] < min_pos[0]: min_pos[0] = pos[0]
            if pos[1] < min_pos[1]: min_pos[1] = pos[1]
            print "%s - %i:%i - %i:%i" % (line, x_movement, y_movement, pos[0], pos[1])

            if mouse_click != 00:  # if button is held down, we are writing
                do_point(pos, draw, 255, 5)
            if left_click == 0xff:
                do_point(pos, draw, 250, 5)
        else:
            print "error on line :%i - %s" % (index, line)
    # img.show()
    img.save('im2.png')
    print "Min max positions : ", min_pos, max_pos

######### EXECUTION CODE ##########
# stats_my_raws('out.txt')

resolv('out.txt')