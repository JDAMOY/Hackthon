#coding:utf-8
from flask import Flask, request
import urllib

app = Flask(__name__)
import Player
p = Player.Player();
@app.route('/music')
def play_music():
        mode = request.args.get('mode')
        music = request.args.get('music')
        p.playMusic(mode, music);
        return 'OK'

@app.route('/sound')
def play_sound():
        words = urllib.unquote(request.args.get('words'))
        print ("received words: " + words)
        accend = request.args.get('accend')
        p.playSound(words, accend)
        return 'OK'

@app.route('/flash')
def play_flash():
        p.playFlash();
        return 'OK'

@app.route('/timealert/<int:hour>')
def play_timealert(hour):
        p.playTimeAlert(hour);
        return 'OK'

if __name__ == '__main__':
    app.run(port=5000)
