"""
Here there will be utility functions that can later go into a larger library.
"""
import ephem
from math import sin, cos, atan2
import datetime

def arcSecondToAU(arcseconds, distance):
    """
    Converts diameter given by pyEphem to the static diameter of the body
    Returns in kilometers
    """
    km_in_AU = 149598000
    rad_in_arcsec = 206265
    return distance * arcseconds / rad_in_arcsec * km_in_AU

def generateDates(num_days, format='%Y/%m/%d'):
    """
    Generates dates for a given number of days away from today.
    If you give a negative number here, it will go backwards.

    Format will automatically take the datetimes and convert them to something
    pyEphem understands. Call with None to get the raw Datetimes back.
    """
    days = abs(num_days)
    if num_days > 0:
        dates_raw = [datetime.today()+timedelta(days=i) for i in range(0,days)]
    else:
        dates_raw = [datetime.today()-timedelta(days=i) for i in range(0,days)]

    if format is not None:
        dates_string = [i.strftime(format) for i in dates_raw]
        return dates_string
    else:
        return dates_raw

def sphericalToRectangle(pos):
    """
    Converts spherical coordinates to rectangular coordinates.
    Takes in an object given by ephem package.
    """
    r = pos.sun_distance
    if r == 0:
        r = pos.earth_distance
    b = pos.hlat
    l = pos.hlon

    x = r*cos(b)*cos(l)
    y = r*cos(b)*sin(l)

    return (x, y)

if __name__ == '__main__':
    body = ephem.Jupiter('2018/01/03')
    a = arcSecondToAU(body.size, body.earth_distance)

    print(a)
