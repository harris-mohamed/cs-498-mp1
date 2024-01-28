from flask import Flask, request

from multiprocessing import Pool
from multiprocessing import cpu_count
import time
import socket
import subprocess

app = Flask(__name__)

seed = 0

@app.post('/')
def seedPost():
    global seed
    subprocess.Popen(["python3", "stress_cpu.py"])
    return f""

@app.get('/')
def seedGet():
    global seed
    return f"{socket.gethostname()}"