from sense_emu import SenseHat
from time import sleep

sleep(1)

sense_emulator = SenseHat()
G = [0, 255, 0]
sense_emulator.show_letter('9', G)

for counter in range(9, 0, -1):
    sleep(1)
    G[0] += 20
    G[1] -= 10
    sense_emulator.show_letter(str(counter), G)

sleep(1)

sense_emulator = SenseHat()
G = [140, 32, 60]
sense_emulator.show_letter('0', G)