import random
import time

from pylsl import StreamInfo, StreamOutlet
from numpy.random import normal

info = StreamInfo('Python Stream','Markers',1,0,'string','Test Marker Stream')
outlet = StreamOutlet(info)

print('Now sending markers...')

while True:
    random_data = str(normal(loc=0,scale=4,size=1)[0])
    print(random_data)
    outlet.push_sample([random_data])
    time.sleep(random.random()*3)
