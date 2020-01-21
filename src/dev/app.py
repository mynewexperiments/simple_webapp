import json
from flask import Flask
from flask import request, abort
import os
import hmac
import hashlib

GITHUB_SECRET = os.environ["AUTH_TOKEN"]
app = Flask(__name__, static_url_path='')

@app.route('/')
def api():
    return "hello world"

@app.route("/health")
def health():
        return (
            "ok",
            200,
            {"Content-Type": "text/plain; charset=utf-8", "Cache-Control": "no-cache"},
        )

@app.route('/github', methods=['POST'])
def listener():
    """
    python - flask web application to listen to
    github hooks
    :return: json
    """
    signature = request.headers.get("X-Hub-Signature")
    if not signature or not signature.startswith("sha1="):
        abort(400, "X-Hub-Signature required")

    digest = hmac.new(GITHUB_SECRET.encode(),
                      request.data, hashlib.sha1).hexdigest()

    if not hmac.compare_digest(signature, "sha1=" + digest):
        abort(400, "Invalid signature")

    if request.headers['Content-Type'] == 'application/json':
        # url = os.path.join(os.path.dirname(__file__), "event_store")
        event = json.dumps(request.json)
        print(event)
        return event

if __name__ == "__main__":

    app.run(debug=True)





