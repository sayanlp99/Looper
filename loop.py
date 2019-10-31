initial=int(input("Enter initial value"))
amount=int(input("Enter number of times the increment will occur:"))
time_difference=int(input("Enter time difference between two instance in seconds:"))


from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

print("Loop initialized from "+str(initial)+" to "+str(initial+amount)+".\nStarting witihin 5seconds.\n")
time.sleep(5)
initial=initial-1
amount=amount+1
for i in range(0, amount):
    initial=initial+1
    keyboard.type(str(initial))
    keyboard.type("\n")
    time.sleep(time_difference)
print("Loop completed.")
