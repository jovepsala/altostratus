import time
import datetime
import socket
from flask import Flask
from flask import Response
import os

application = Flask(__name__)

@application.route("/")
def hello():

    os.remove("/mnt/log.txt")

    timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    line = socket.gethostname() + "\t" + timestamp + "\n"

    file = open("/mnt/log.txt", "a+")
    file.write(line)

    file.seek(0, 0)
    content = file.read()

    file.close()

    return Response(content, mimetype="text/plain")

if __name__ == "__main__":
    application.run()





