from flask import Flask
import logging
import os

app = Flask(__name__)

# Ensure /logs exists
os.makedirs("/logs", exist_ok=True)

# Set up logging to file
log_file_path = "/logs/flask.log"
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

@app.route("/")
def home():
    app.logger.info("Home page accessed")
    return "Hello from Flask!"

@app.route("/feature_1")
def fail():
    try:
        print(1/0)
    except Exception as e:
        app.logger.error("Something went wrong!")
        raise Exception("Simulated error for testing")

@app.route("/logs")
def get_logs():
    try:
        with open(log_file_path, "r") as f:
            return "<pre>" + f.read() + "</pre>", 200
    except Exception as e:
        return f"Error reading log file: {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
