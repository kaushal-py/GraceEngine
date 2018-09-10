# Python libraries
import subprocess
import sys

# External libraries
from flask import Flask
from flask import render_template
from flask_socketio import SocketIO
from flask_socketio import send, emit

# Local libraries
sys.path.insert(0, '../')
from engine.hardcode_recognizer import HardCodeRecognizer
import config

# Initialise app 
app = Flask(__name__)
socketio = SocketIO(app)
nl = HardCodeRecognizer()


@app.route('/')
def hello_world():
    return render_template('index.html')    


@socketio.on('nl_event')
def handle_message(data):
    out_data = nl.recognize(data['data'])
    emit('nl_event', '\n'+out_data)


@socketio.on('generate_output')
def compile(data):
    
    with open( config.CODE_FILE ,"w+") as f:
        f.write(data['data'])

    # Execute the python file and get the output
    op = subprocess.Popen(['python', config.CODE_FILE ], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    op = op.communicate()[0].decode("utf-8")
    
    emit('compile','\n'+op)


if __name__ == "__main__":
    socketio.run(app, debug=True)