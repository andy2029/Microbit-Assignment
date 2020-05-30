# sender
# task 3
from microbit import *
import random
import radio

radio.on()

def sendWithError(message, error):
    global packets_sent
    generated = random.randint(1, 100)
    if generated > error:
        radio.send(message)
        return True
    return False

def checkParity(message):
    return message.count('1') % 2

message = "01000001 01001110"

display.show(Image('09990:90009:00990:00000:00900:'))
while True:
    if button_a.is_pressed():
        display.show(Image.YES)
        sendWithError(message, 0)
        display.scroll(message)
        sleep(500)
        display.show(Image('09990:90009:00990:00000:00900:'))
    if button_b.is_pressed():
        simulateError = message.replace('1', '0', 1)
        sendWithError(simulateError, 0)
        display.scroll(simulateError)
