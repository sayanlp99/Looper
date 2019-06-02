initial=0                #start with this integer value
amount=5                 #number of times the increment will occur
time_difference=1        #time difference between two instance   


from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

print("Loop initialized from "+str(initial)+" to "+str(initial+amount)+".\n")
initial=initial-1
amount=amount+1
for i in range(0, amount):
    initial=initial+1
    keyboard.type(str(initial))
    keyboard.type("\n")
    time.sleep(time_difference)
print("Loop completed.")
