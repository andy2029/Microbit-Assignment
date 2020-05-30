#receiver
#task 2
from microbit import *
import radio

radio.on()
radio.config(group = 0)
my_address = "S2"
their_address = "S1"
header = my_address + "DE" + their_address
acknowledge_string = "ACK"
acknowledge_packet = header + acknowledge_string
display.show(Image('09990:90009:00990:00000:00900:'))

while True:
    message = radio.receive()
    if message is not None:
        if len(message) >= 5 and message[2:4] == my_address:
            data = message[4:]
            display.show(Image('00900:00900:00900:00000:00900:'))
            sleep(1000)
            display.scroll(data)
        message = None
