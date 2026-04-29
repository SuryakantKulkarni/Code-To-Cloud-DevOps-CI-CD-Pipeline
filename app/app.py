from flask import Flask, render_template
import socket
import datetime
import psutil

app = Flask(__name__)

@app.route('/')
def home():
    return render_template(
        "index.html",
        hostname=socket.gethostname(),
        time=datetime.datetime.now(),
        cpu=psutil.cpu_percent(),
        memory=psutil.virtual_memory().percent
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)