from pprint import pprint
import re
import polling
import os
import sys
import time
from flask import Flask, render_template, make_response, request

app = Flask(__name__)


# Monitors a file, calls callback when "Last Changed" time is changed
def monitor_file(filename, callback):
    print("Monitoring file '%s'" % filename)

    while True:
        try:
            last_change = os.stat(filename).st_mtime
            polling.poll(
                lambda: last_change != os.stat(filename).st_mtime,
                step=1,
                poll_forever=True)

        except (IOError, FileNotFoundError) as e:
            print("ERROR: No such file: '%s'. Sleeping for 1 second." % filename)
            time.sleep(1)
            continue
        callback()


def refresh_data(filename):
    print('%s updated. Refresh data.' % filename)


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

# TODO: Bug #1: solve this in a nicer way
@app.after_request
def after(response):
  # todo with response
  pprint(request.__dict__)

  print(response.status)
  print(response.headers)
  print(response.get_data())
  return make_response(render_template('index.html',
                           proxy_paths=proxy_paths,
                           base_url=BASE_URL,
                           title=TITLE))


@app.route('/')
def home():
    return render_template('index.html',
                           proxy_paths=proxy_paths,
                           base_url=BASE_URL,
                           title=TITLE)


if __name__ == '__main__':
    # Setup
    PORT = int(os.environ.get('PORT', '5000'))
    BASE_URL = os.environ.get('BASE_URL', '')
    TITLE = os.environ.get('TITLE', '')

    try:
        filename = os.environ['FILENAME']
    except KeyError as e:
        print("ERROR: Must specify environment variable of the file to monitor FILENAME")
        sys.exit(1)

    #monitor_file(filename, lambda: refresh_data(filename))

    proxy_paths = parse_nginx_conf(filename)

    # Start flask app
    app.run(host='0.0.0.0', port=PORT, debug=True)
