#coding:utf-8
import RPi.GPIO as GPIO
import time
import os
import num2chinese

CHANNEL = 11
GAP	= 5

musics = {
        "SUCCESS": "success_zhouxx.mp3",
        "FAILURE": "failure_kxzsn.wav"
        }

class Player:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(CHANNEL, GPIO.OUT)
        GPIO.cleanup()
    
    def playTimeAlert(self, hour):
        htext = num2chinese.num2chinese(hour)
        htext = "十八"
        message = "现在是北京时间%s点整" % htext
        print message
        self.playSound(message)

    def playMusic(self, success=True):
        music = None
        if success:
            music = musics['SUCCESS']
        else:
            music = musics['FAILURE']
        os.system('mplayer ' + music)

    def playSound(self, words, accend="xiaoyan"):
        cmd = "tts temp.wav '%s' %s && mplayer temp.wav && rm temp.wav " % (words, accend)
        print cmd
        os.system(cmd)


    def playFlash(self):
        GPIO.output(CHANNEL, 1)
        time.sleep(GAP)
        GPIO.output(CHANNEL, 0)
        GPIO.cleanup()

if __name__ == "__main__":
    p = Player()
    #print "Play Sound Hehe"
    #p.playSound("中华人民共和国，今天成立了", "vixqa")
    #p.playMusic(False)
    p.playTimeAlert(18)
