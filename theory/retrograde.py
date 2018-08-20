import ephem
from datetime import datetime, timedelta
from math import sin, cos, atan2
import matplotlib.pyplot as plt
from numpy import diff

# generate a separation thing for a year
dates_raw = [datetime.today()+timedelta(days=i) for i in range(0,365*3)]
dates_string = [i.strftime('%Y/%m/%d') for i in dates_raw]

def sphericalToRectangle(pos):
    r = pos.sun_distance
    if r == 0:
        r = pos.earth_distance
    b = pos.hlat
    l = pos.hlon

    x = r*cos(b)*cos(l)
    y = r*cos(b)*sin(l)

    return (x, y)

pos_delta = []
x_pos_earth = []
y_pos_earth = []
x_pos_planet = []
y_pos_planet = []

for date in dates_string:
    pos_earth = sphericalToRectangle(ephem.Sun(date))
    pos_planet = sphericalToRectangle(ephem.Mars(date))

    x_pos_earth.append(pos_earth[0])
    y_pos_earth.append(pos_earth[1])
    x_pos_planet.append(pos_planet[0])
    y_pos_planet.append(pos_planet[1])

    pos_delta.append((pos_planet[0] - pos_earth[0], pos_planet[1] - pos_earth[1], date))

mathed = [(i[2], atan2(i[1], i[0])) for i in pos_delta]
dA = diff([i[1] for i in mathed])
dAnnotate = []
for idx, i in enumerate(dA):
    dAnnotate.append((mathed[idx][0], i))

with open('pos.txt', 'w') as a:
    for line in dAnnotate:
        a.write(str(line[0])+ " " + str(line[1]) + '\n')

# plt.plot(x_pos_earth, y_pos_earth, 'bs', x_pos_planet, y_pos_planet, 'ys')
# plt.show()
