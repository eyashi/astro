import ephem

mars = ephem.Mars()
mars.compute('2018/08/09')

print(mars.ra, mars.dec)

# Ok this was successful
