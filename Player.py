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
        try:
            while True:
                    GPIO.output(CHANNEL, 1)
                    print('set channel 11 to HIGH')
                    time.sleep(GAP)
                    GPIO.output(CHANNEL, 0)
                    print('set channel 11 to LOW')
                    time.sleep(GAP)
        except KeyboardInterrupt:
            GPIO.cleanup()
            print('clean up...')

if __name__ == "__main__":
    p = Player()
    p.playFlash()
