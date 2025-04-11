# Countdown Timer

import time
import sys

def countdown(t):
  while t:
    mins, secs = divmod(t, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    sys.stdout.write(f'\r{timer}')
    sys.stdout.flush()
    time.sleep(1)
    t -= 1
  print('\rTimer completed!')
t = input("Enter the time in seconds:")

countdown(int(t))
