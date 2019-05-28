from flask import Flask, jsonify, Response
from flask_cors import CORS
from path_file_seeker import get_map_of_files
from load_sql_table import load_sql_table
from loadfile import load_mongo_table
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    #return jsonify(get_map_of_files(path))
    return 'Hello, World!'

@app.route('/filePath/<path>')
def obtain_files_in_path(path):
    print(path)
    print(jsonify(get_map_of_files(path)))
    print(get_map_of_files(path))
    js = jsonify(get_map_of_files(path))
    return js

@app.route('/loadTable/<tableName>/<path>/<thefile>')
def load_table(tableName, path, thefile):
    print(tableName)
    print(path)
    print(thefile)
    #load_sql_table(path + '/' + thefile, tableName)
    load_mongo_table(path + '/' + thefile, tableName)
    print("Complete")
    return jsonify({success: True})
