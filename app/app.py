import logging
import os
from datetime import datetime
from flask import Flask, jsonify, request

logging.basicConfig(level=logging.INFO, format="(asctime)s [%(levelname)s] %(message)s",)

logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.before_request
def log_request():
    logger.info("Incoming request %s %s from %s", request.method, request.path, request.remote_addr)

@app.route("/")
def index():
    return jsonify(
        {
            "service": "cloud-project",
            "status": "ok",
            "message": "Successful connection to container",
            "timestamp": datetime.utcnow().isoformat() + "Z",
        }
    )

@app.route("/admin")
def admin():
    return """
    <h1>Oh no you found my admin page :( </h1>
    <p>Just kidding, there's nothing here. But nice try!</p>
    <img src="https://thumbs.dreamstime.com/b/smiling-yellow-emoticon-cartoon-mascot-character-sunglasses-giving-two-thumbs-up-smiling-yellow-emoticon-cartoon-mascot-182682206.jpg">
    """
    

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)