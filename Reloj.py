from datetime import datetime
import time

for s in range(25):
    dt = datetime.now()
    print("Son las {}:{}:{}".format(dt.hour, dt.minute, dt.second))
    time.sleep(1)

#comentario adicional
