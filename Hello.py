from flask import Flask
app = Flask(__name__)
import commands

@app.route('/music')
def hello_world():
        (status, output) = commands.getstatusoutput('mplayer rolling\ in\ the\ deep.mp3')
        return output;
