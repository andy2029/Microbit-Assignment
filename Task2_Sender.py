# sender
# task 2
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

message = [0]
seq_first = 0
seq_n = 0

display.show(Image('09990:90009:00990:00000:00900:'))
while True:
    if button_a.is_pressed():
        next_message=message[-1]+1
        message.append(next_message)
        packet = str(next_message)
        display.scroll(str(next_message))
        sendWithError(packet, 0)
        display.show(Image.YES)
        sleep(200)
        display.show(Image('09990:90009:00990:00000:00900:'))
        n_message=message[-1]
    if button_b.is_pressed():
        button_a.get_presses()
        display.scroll("n")
        while button_b.was_pressed():
            if seq_n == len(message) - 1 or message == [0]:
                seq_n = 0
            else:
                seq_n += 1
            display.scroll(str(seq_n))
            sleep(200)
            if button_a.get_presses() == 1:
                if not seq_n == 0:
                    n_message = message[-seq_n]
                    packet = str(n_message)
                    sendWithError(packet, 0)
                    display.scroll(n_message)
        display.show(Image('09990:90009:00990:00000:00900:'))
