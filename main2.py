from flask import Flask, jsonify, request, json
from werkzeug.utils import secure_filename
from pydub.utils import mediainfo

import os

app = Flask(__name__, static_folder="server_audio")
app.config['AUDIO_FOLDER'] = "./audio"
app.config['ACCELEROMETER_FOLDER'] = "./accelerometer data"
app.config['SERVER_ADUIO'] = "./server_audio"
app.config['recording']  = False
app.config['machine'] = ""


def check_path(path):
    if not os.path.exists(path):
        os.mkdir(path)


@app.route("/audiolist", methods=['GET'])
def audio_list():
    base_path = app.config['SERVER_ADUIO']
    check_path(base_path)
    audio_list = []
    paths = sorted(os.listdir(base_path))
    for file_name in paths:
        if file_name == ".DS_Store":
            continue
        path = os.path.join(base_path, file_name)
        length = get_length(path)
        audio_list.append({"name":file_name, "len":length})

    return jsonify(audio_list)

def get_length(path):
    # print(path)
    info = mediainfo(path)
    # print(info)
    length = int(float(info["duration"])* 1000)
    return length

@app.route('/acclog', methods=['GET', 'POST'])
def acclog():
    check_path(app.config['ACCELEROMETER_FOLDER'])
    acclog = request.form.get('acclog');
    file_name = request.form.get('name')
    machine_name = request.form.get('machine')
    save_dir = os.path.join(app.config['ACCELEROMETER_FOLDER'], machine_name)
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)

    path="{}/{}.csv".format(save_dir, file_name)
    writer = open(path, 'w')
    writer.write(acclog)
    writer.close()
    return jsonify(msg="success to upload server")


@app.route("/audio", methods=['POST'])
def audio():
    check_path(app.config['AUDIO_FOLDER'])
    print(request.files)
    file_storage = request.files.get('audio')
    file_name = request.form.get('name')
    machine_name = request.form.get('machine')
    if file_storage != None:
        path = os.path.join(app.config['AUDIO_FOLDER'], machine_name)
        if not os.path.exists(path):
            os.mkdir(path)
        path = os.path.join(path, file_name)
        file_storage.save(path)

    return jsonify(msg="success to upload server")


@app.route("/syncrecording", methods=['POST'])
def syncrecording():
    play = int(request.form.get('recording'))
    app.config['machine'] = request.form.get('machine')
    app.config['recording'] = (play > 0)
    return jsonify(msg="success to update status")
    

@app.route("/recording", methods=['GET'])
def getrecording():
    return jsonify(recording=app.config['recording'], machine = app.config['machine'])



@app.route('/')
def hello_world():
    return 'Voice Service is Running!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
