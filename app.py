from flask import Flask, render_template, request
import json
from datetime import datetime

app = Flask(__name__)

LOG_FILE = "honeypot_logs.json"


def save_log(data):
    try:
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    except:
        logs = []

    logs.append(data)

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)


@app.route("/", methods=["GET", "POST"])
def fake_login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        ip = request.remote_addr

        log = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "username": username,
            "password": password,
            "ip_address": ip,
            "status": "Suspicious Login Attempt",
            "alert": "Unauthorized access attempt detected"
        }

        save_log(log)

        return "<h3>Invalid Credentials</h3>"

    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)