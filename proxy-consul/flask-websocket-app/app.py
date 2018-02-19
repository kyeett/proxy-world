import polling
import os


# Monitors a file, calls callback when "Last Changed" time is changed
def monitor_file(filename, callback):
    while True:
        last_change = os.stat(filename).st_mtime
        polling.poll(
            lambda: last_change != os.stat(filename).st_mtime,
            step=1,
            poll_forever=True)

        callback()


def refresh_data(filename):
    print('%s updated. Refresh data.' % filename)


filename = "lol"
monitor_file(filename, lambda: refresh_data(filename))
