#receiver
from microbit import *
import random
import radio

def sendWithError(message, error):
    generated = random.randint(1, 100)
    if generated > error:
        radio.send(message)
        return True
    return False

radio.on()
radio.config(group = 0)
my_address = "DA"
their_address = "AN"
header = my_address + their_address
acknowledge_string = "ACK"
acknowledge_packet = header + acknowledge_string
display.show(Image('09990:90009:00990:00000:00900:'))

last_received = None
duplicates = 0

while True:
    message = radio.receive()
    if message is not None:
        if len(message) >= 5 and message[2:4] == my_address:
            data = message[4:]
            display.show(Image('00900:00900:00900:00000:00900:'))
            sleep(1000)
            sendWithError(acknowledge_packet, 0)
            display.scroll(data)
            # Send with error
            if data != last_received:
                last_received = data
            else:
                duplicates += 1
        message = None

    if button_b.was_pressed():
        display.scroll(str(duplicates))
