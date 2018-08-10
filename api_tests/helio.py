from sunpy.net import hek
client = hek.HEKClient()

tstart = '2011/08/09 07:23:56'
tend = '2011/08/09 12:40:29'
event_type = 'FL'
result = client.search(hek.attrs.Time(tstart,tend),hek.attrs.EventType(event_type))

print(result)

# cool the flares are all here.
