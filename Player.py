import RPi.GPIO as GPIO
import time
import subprocess

CHANNEL = 11
GAP	= 5

class Player:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(CHANNEL, GPIO.OUT)

    def playMusic(self):
        pass

    def playSound(self, words, accend="xiaoyan"):
        cmd = "tts temp.wav '%s' %s && mplayer temp.wav && rm temp.wav " % (words, accend)
        print cmd
        subprocess.call(cmd)

    def playFlash(self):
        GPIO.output(CHANNEL, 1)
        time.sleep(GAP)
        GPIO.output(CHANNEL, 0)
        GPIO.cleanup()

if __name__ == "__main__":
    p = Player()
    p.playSound("Hehe", "xiaoxin")
