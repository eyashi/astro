import tkinter as tk
import utility as ut
import datetime as dt
import ephem

screen_size = 500

CANVAS_WIDTH = CANVAS_HEIGHT = screen_size

PLANETS = {
    'mars': ephem.Mars(),
    'uranus': ephem.Uranus(),
    'jupiter': ephem.Jupiter()
    }
TODAY = dt.datetime.today().strftime('%Y/%m/%d')

class Planet():
    """Planetoid Unit Initialize"""
    def __init__(self, planet_name):
        # here get info about the planet, like the size etc...
        self.body = PLANETS[planet_name]
        self.body.compute(TODAY)
        self.size = ut.arcSecondToAU(self.body.size, self.body.earth_distance)
        self.x, self.y = ut.sphericalToRectangle(self.body)

        print(self.x, self.y)

    def getPositions(self, num_days):
        # here grab the positions of the planet
        pass

def getScaleOfOrbits(planets, screen_size, border):
    max_au = .1
    for planet in planets:
        if planet.sun_distance > max_au:
            max_au = planet.sun_distance

    return (screen_size-border)/(2*max_au)

# circle starting center coordinates and radius
CIRCLE_X = 50
CIRCLE_Y = 50
CIRCLE_RADIUS = 50

# fix animation rate, time in milliseconds
STEP_TIME = 25
STEP_X = 1
STEP_Y = 1

def move_circle():
    ''' recursive function '''
    canvas.move("orange_circles", STEP_X, STEP_Y)
    x0, y0, x1, y1 = canvas.bbox("orange_circles")
    if x1 > CANVAS_WIDTH:
        return
    canvas.after(STEP_TIME, move_circle)

def circle(x, y, r):
    # form a bounding square using center (x,y) and radius r
    # upper left corner (ulc) and lower right corner (lrc) coordinates of square
    ulc = x-r, y-r
    lrc = x+r, y+r
    # give the circle a tag name for reference
    canvas.create_oval(ulc, lrc, tag="orange_circles", fill='orange')
root = tk.Tk()
root.title("Orbit Visualization")
# ulc position of rootwindow
root.geometry("+{}+{}".format(150, 80))
# create a canvas to draw on
canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='lightblue')
canvas.pack()

circle(CIRCLE_X, CIRCLE_Y, CIRCLE_RADIUS)
circle(CIRCLE_X, CIRCLE_Y-55, CIRCLE_RADIUS/2)

move_circle()

root.mainloop()

p = Planet('mars')
