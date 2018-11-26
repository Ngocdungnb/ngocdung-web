import mlab
from river import River

mlab.connect()

records  = River.objects (continent = "S. America", length__gt = 1000)
for r in records:
    print (r.name)