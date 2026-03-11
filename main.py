import time
import random

arrs = [1,2,3,4,5]
random.shuffle(arrs)
for i in arrs:
    print(i)
    time.sleep(1)