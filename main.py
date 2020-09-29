from flask import Flask, jsonify, request, json
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "./audio"

@app.route('/acclog', methods=['GET', 'POST'])
def acclog():
    acclog =  json.loads(request.data.decode('utf-8'))
    file_name = acclog['file_name'].replace("/", "_")
    machine_name = acclog['machine']
    save_dir = os.path.join("./data", machine_name)
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)

    path="{}/{}.csv".format(save_dir, file_name)
    writer = open(path, 'w')
    for line in acclog['data']:
        writer.write(line+"\n")

    writer.close()
    return jsonify(msg="success to upload server")

@app.route("/audio", methods=['POST'])
def audio():
    file_storage = request.files.get('audio')
    file_name = request.form.get('name').replace("/", "_")
    machine_name = request.form.get('machine')
    if file_storage != None:
        path = os.path.join(app.config['UPLOAD_FOLDER'], machine_name)
        if not os.path.exists(path):
            os.mkdir(path)
        path = os.path.join(path, file_name)
        file_storage.save(path)

    return jsonify(msg="success to upload server")
@app.route('/')
def hello_world():
    return 'Voice Service is Running!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
