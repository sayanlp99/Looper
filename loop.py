initial=0                #start with this integer value
amount=10                #number of times the increment will occur
time_difference=3        #time difference between two instance   


from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

initial=initial-1

for i in range(0, amount):
    initial=initial+1
    keyboard.type(str(initial))
    keyboard.type("\n")
    time.sleep(time_difference)
