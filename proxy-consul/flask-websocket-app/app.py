import re
import os
import sys
import time
from flask import Flask, render_template
from threading import Thread
import logging
from flask_socketio import SocketIO, send, emit
import eventlet

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


# SOCKETIO
@socketio.on('my event')
def handle_my_custom_event(json):
    json['appendage'] = 'noodle'
    emit('my response', json)


# FLASK
@app.route('/', strict_slashes=False)
def home():
    return render_template('index.html',
                           proxy_paths=proxy_paths,
                           base_url=BASE_URL,
                           title=TITLE)


# OTHER

# Monitors a file, calls callback when "Last Changed" time is changed
def monitor_file(filename, callback, sleep_function=time.sleep):
    logging.info("Monitoring file '%s'" % filename)

    while True:
        try:
            # Poll until file "last changed" is changed
            last_change = os.stat(filename).st_mtime
            while last_change == os.stat(filename).st_mtime:
                sleep_function(1)

        except (IOError, FileNotFoundError) as e:
            logging.error("No such file: '%s'. Sleeping for 1 second." % filename)
            sleep_function.sleep(1)
            continue

        callback(filename)


def refresh_data(filename):
    logging.info('%s updated. Refresh data.' % filename)
    global proxy_paths
    proxy_paths = parse_nginx_conf(filename)
    browser_data = {
        'proxy_paths': proxy_paths
    }
    socketio.send(browser_data)


# Parses an nginx-conf file and returns paths to defined proxies
def parse_nginx_conf(filename):

    proxy_paths = []
    with open(filename) as f:

        for line in f.readlines():
            # Find lines with location-definitons
            match = re.search('(?<=location).*(?={)', line)

            if match:
                proxy_paths.append(match.group(0).strip()[1:])

    return proxy_paths


logging.getLogger().setLevel(logging.DEBUG)
logging.getLogger('requests').setLevel(logging.WARNING)
logging.basicConfig(level=logging.DEBUG)

global proxy_paths
proxy_paths = []

if __name__ == '__main__':
    # Setup
    PORT = int(os.environ.get('PORT', '5000'))
    BASE_URL = os.environ.get('BASE_URL', '')
    TITLE = os.environ.get('TITLE', '')

    try:
        filename = os.environ['FILENAME']
    except KeyError as e:
        logging.error("Must specify environment variable of the file to monitor FILENAME")
        sys.exit(1)

    # Try to read config file once, ignore failure
    try:
        refresh_data(filename)
    except (IOError, FileNotFoundError) as e:
        logging.error("No such file: '%s'." % filename)

    socketio.start_background_task(monitor_file, filename, refresh_data, eventlet.sleep)
#    monitor_file_thread = Thread(target=monitor_file, args=(filename, refresh_data), daemon=True)
#    monitor_file_thread.start()


    # Start flask app
#    app.run(host='0.0.0.0', port=PORT)
    socketio.run(app, host='0.0.0.0', port=PORT)

