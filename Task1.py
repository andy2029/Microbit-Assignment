#sender
from microbit import *
import random
import radio

radio.on()

def sendWithError(message, error):
    global packets_sent
    generated = random.randint(1, 100)
    if generated > error:
        radio.send(message)
        packets_sent += 1
        return True
    return False

def waitForAck():
    global received_ack
    start_time = running_time()
    while running_time() < start_time + 3000:
            state = "busy"
            message = radio.receive()
            if message is not None:
                if message[2:4] == my_address and message[4:] == "ACK":
                    received_ack = True
                    display.show(Image.YES)
                else:
                    received_ack = False
my_address = "AN"
their_address = "DA"
header = my_address + their_address
packets_lost = 0
packets_sent = 0
number = 1
received_ack = False
state = "idle"

display.show(Image('09990:90009:00990:00000:00900:'))
while True:
    if button_a.is_pressed() and state == "idle":
        if received_ack:
            received_ack = False
            number += 1
        packet = header + str(number)
        display.scroll(str(number))
        sendWithError(packet, 0)
        # 10 second timeout
        waitForAck()
        if received_ack == False:
            packets_lost += 1
            display.show(Image.NO)
        state = "idle"
    if button_b.is_pressed() and not packets_sent == 0:
        display.scroll(str(int((packets_lost / packets_sent) * 100)) + "%")
