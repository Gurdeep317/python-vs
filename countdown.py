# program to create a countdown timer
# import time
# usig def
# using while loop
import time
def countdown(sec):
    while sec:
        mins,secs=divmod(sec,60)
        time_format="{:2d}:{:2d}".format(mins,secs)
        print(time_format)
        time.sleep(1)
        sec=sec-1
        print("stop")
        countdown(5)