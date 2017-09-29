# -*- coding: utf-8 -*- 

import RPi.GPIO as GPIO
import time
import os

CHANNEL = 11
GAP	= 5

musics = {
        "SUCCESS": "success_zhouxx.mp3",
        "FAILURE": "failure_kxzsn.wav"
        }

class Player:
    def __init__(self):
        self._initMode()
        GPIO.cleanup()

    def _initMode(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(CHANNEL, GPIO.OUT)
    
    def playTimeAlert(self, hour):
        if hour > 24 or hour < 0:
            return
        charList = ['', '一', '二', '三', '四', '五', '六', '七', '八', '九']
        htext = charList[hour % 10]

        if hour / 10 == 1:
            htext = "十" + htext
        elif hour / 10 == 2:
            htext = '二十' + htext
        else:
            pass
        
        if hour == 0:
            htext = '零'
            
        message = "现在是北京时间%s点整" % htext
        print message
        self.playSound(message)

    def playMusic(self, mode='SUCCESS', url = None):
        music = url 

        if not music:
            music = musics[mode]
        os.system('mplayer ' + music)

    def playSound(self, words, accend="xiaoyan"):
        cmd = u"tts temp.wav '%s' %s && mplayer temp.wav && rm temp.wav " % (words, accend)
        print cmd
        os.system(cmd.encode('utf-8'))


    def playFlash(self):
        self._initMode()
        GPIO.output(CHANNEL, 1)
        time.sleep(GAP)
        GPIO.output(CHANNEL, 0)
        GPIO.cleanup()

if __name__ == "__main__":
    p = Player()
    #print "Play Sound Hehe"
    p.playSound("中华人民共和国，今天成立了", "vixqa")
    #p.playMusic(url = "http://58.216.22.56/file3.data.weipan.cn/36050867/40298daf4f7a1af67e9bab1eedcee319e21a8240?ip=1506590827,58.211.225.90&ssig=apb9YRrRBq&Expires=1506591427&KID=sae,l30zoo1wmz&fn=Gee.mp3&skiprd=2&se_ip_debug=58.211.225.90&corp=2&from=1221134&wsiphost=local")
    #p.playTimeAlert(8)
