import time
import datetime
import socket
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():

    timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    line = timestamp + "\t" + socket.gethostname() + "\n"

    file = open("/mnt/log.txt", "a+")
    file.write(line)

    file.seek(0, 0)
    content = file.read()

    file.close()

    return content

if __name__ == "__main__":
    application.run()





