import RPi.GPIO as GPIO
import time

CHANNEL = 11
GAP	= 5

class Player:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(CHANNEL, GPIO.OUT)

    def playMusic(self):
        pass

    def playFlash(self):
        GPIO.output(CHANNEL, 1)
        time.sleep(GAP)
        GPIO.output(CHANNEL, 0)
        GPIO.cleanup()

if __name__ == "__main__":
    p = Player()
    p.playFlash()
