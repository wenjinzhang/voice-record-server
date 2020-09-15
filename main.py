from flask import Flask, jsonify, request
from util import cast_command
app = Flask(__name__)


@app.route('/acclog/')
def acclog():
    print("request.data: %s"%request.data)
    return jsonify(msg="success to upload server")


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=False)
