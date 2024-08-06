from flask import Flask
import os
import socket
from contextlib import closing
from flask import request

def check_socket(host, port):
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        if sock.connect_ex((host, port)) == 0:
            return ("is open")
        else:
            return ("is not open")
app = Flask(__name__)

@app.route('/')
def hello():
    host = request.args.get('host')
    port = request.args.get('port')
    print(host, port)
    result = check_socket(host, int(port))
    return "  {} : {} {}".format(host, port, result)

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)
    app.run(port=port,host='0.0.0.0')
