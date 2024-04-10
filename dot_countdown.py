from sense_emu import SenseHat
from time import sleep

sense = SenseHat()

G = [0, 255, 0]
R = [255, 0, 0]
X = [0, 0, 0]

timer = []

set_pixels = SenseHat

for i in range(64):
    timer.append(X)
    
for i in range(0, 10):
    timer[i] = G
sense.set_pixels(timer)
      
for i in range(0, 10):
    sleep(1)
    timer[i] = R
    sense.set_pixels(timer)
      
for i in range(0, 10):
    sense.clear()
    sleep(0.1)
    sense.set_pixels(timer)
    sleep(0.1)