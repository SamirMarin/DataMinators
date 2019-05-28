from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/filePath')
def obtain_files_in_path(path):
    get_map_of_files(path)
