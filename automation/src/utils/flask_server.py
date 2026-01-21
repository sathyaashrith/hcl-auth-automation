import subprocess
import time
import requests

def start_flask_server():
    # Start Flask app in a separate process
    process = subprocess.Popen(
        ["python", "run_app.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True
    )

    # Wait until Flask is running
    url = "http://127.0.0.1:5000/login"
    for _ in range(20):
        try:
            r = requests.get(url)
            if r.status_code == 200:
                return process
        except:
            time.sleep(1)

    return process

def stop_flask_server(process):
    if process:
        process.terminate()
