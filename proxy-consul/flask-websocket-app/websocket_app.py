from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
import app as APP
from threading import Thread
import logging
import os
import eventlet

logging.getLogger().setLevel(logging.DEBUG)
logging.getLogger('requests').setLevel(logging.WARNING)
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.config.update(
    # DEBUG=True,
    SECRET_KEY='secret!',
)

print
socketio = SocketIO(app)


@socketio.on('message')
def handle_message(message):
    send(message)


@socketio.on('json')
def handle_json(json):
    send(json, json=True)


@socketio.on('my event')
def handle_my_custom_event(json):
    json['appendage'] = 'noodle'
    emit('my response', json)


@app.route('/', strict_slashes=False)
def home():
    return render_template('websocket.html')


@app.route('/test', strict_slashes=False)
def emitter():
    asdf = {
        'custom': "msg"
    }
    socketio.send(asdf)
    return "done"


def custom_emit(dummy):
    logging.debug('custom_emit')
    asdf = {
        'custom': "msg"
    }
    socketio.send(asdf)


def dummy(dummy):
    logging.debug('dumbest')

if __name__ == '__main__':
    filename="lol"
    socketio.start_background_task(APP.monitor_file, filename, custom_emit, eventlet.sleep)
#    monitor_file_thread = Thread(target=APP.monitor_file, args=(filename, custom_emit), daemon=True)
#    monitor_file_thread.start()
    socketio.run(app, port=int(os.environ.get('PORT', '5000')), )
