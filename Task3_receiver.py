#receiver
#task 3
from microbit import *
import radio

radio.on()

def checkParity(message):
    return message.count('1') % 2

display.show(Image('09990:90009:00990:00000:00900:'))

while True:
    message = radio.receive()
    if message is not None:
        if checkParity(message) == 0:
            display.show(Image.YES)
        else:
            display.show(Image.NO)
