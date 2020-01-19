import json
from flask import Flask
from flask import request, abort, send_from_directory
import os
import hmac
import hashlib


GITHUB_SECRET = os.environ["GITHUB_TOKEN"]
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

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)


@app.route('/github', methods=['POST'])
def listener():
    """

    :return:
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
        return event

if __name__ == "__main__":

    app.run(debug=True)



