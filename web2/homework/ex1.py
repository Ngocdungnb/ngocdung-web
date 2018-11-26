import mlab
from river import River

mlab.connect()

records  = River.objects (continent = "Africa")
for r in records:
    print (r.name)