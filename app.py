from flask import Flask, render_template, request
import os
from socket import  AF_INET, SOCK_STREAM
import socket
from datetime import datetime, timedelta

def check_socket(host, portRange):
    hostAddress = host  # loopback address for scanning localhost
      # port scan start time
    data = []  # lists open port strings
    try:
        From,To = portRange.split('-')
    except:
        From=portRange
        To=portRange
    try:   
        for port in range(int(From), int(To)+1):
            sock = socket.socket(AF_INET, SOCK_STREAM)
            sock.settimeout(2)  # scan for 2 secs
            result = sock.connect_ex((hostAddress, port))
            if result == 0:
                data.append(f'Port {port}: OPEN')  # Port __: OPEN
            else:
                data.append(f'Port {port}: NOT OPEN')
            sock.close()
    except OSError as e:
        if e.errno != e.errno.ENOENT:
            print(f'{e}')
            sys.exit()
    return data

app = Flask(__name__)

@app.route('/')
def hello():
    my_hostname = socket.gethostname()
    ip_address = socket.gethostbyname(my_hostname)
    print(my_hostname, ip_address)
    start_time = datetime.now()
    host = request.args.get('host')
    port = request.args.get('port')
    print(host, port)
    result = check_socket(host, port)
    end_time = datetime.now()  # port scan ends: mark time
    duration = end_time - start_time  # port scan duration
    result.append(f'Scan duration: {round(duration.total_seconds(), 2)} secs')
    return render_template('portscan.html', data=result, address=host, my_hostname=my_hostname, ip=ip_address)

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)
    app.run(port=port,host='0.0.0.0',debug=True)
