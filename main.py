from flask import Flask, jsonify, request, json
import os
app = Flask(__name__)


@app.route('/acclog', methods=['GET', 'POST'])
def acclog():
    acclog =  json.loads(request.data.decode('utf-8'))
    file_name = acclog['file_name'].replace("/", "_")
    if not os.path.exists("data"):
        os.mkdir("data")

    path="{}/{}.csv".format("./data", file_name)
    writer = open(path, 'w')
    for line in acclog['data']:
        writer.write(line+"\n")

    writer.close()
    return jsonify(msg="success to upload server")


@app.route('/')
def hello_world():
    return 'Voice Service is Running!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
