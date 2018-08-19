import ephem

def posToSeconds(pos):
    # converts hours minutes seconds to just seconds
    if pos[0] == "-":
        negative = True
        pos = pos[1:]
    conv = pos.split(':')
    hrs = float(conv[0]) * 60 * 60
    min = float(conv[1]) * 60
    sec = float(conv[2])
    pos_s = hrs + min + sec
    print(pos_s)


mars = ephem.Mars()
mars.compute('2018/08/09')

posToSeconds(str(mars.dec))
