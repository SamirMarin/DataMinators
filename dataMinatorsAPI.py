from flask import Flask, jsonify, Response
from flask_cors import CORS
from path_file_seeker import get_map_of_files
from load_sql_table import load_sql_table, load_sql_table_with_delimiter
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    #return jsonify(get_map_of_files(path))
    return 'Hello, World!'

@app.route('/filePath/<path>')
def obtain_files_in_path(path):
    path_mod = path.replace('+', '/')
    print(path_mod)
    print(jsonify(get_map_of_files(path_mod)))
    print(get_map_of_files(path_mod))
    js = jsonify(get_map_of_files(path_mod))
    return js

@app.route('/loadTable/<tableName>/<path>/<thefile>')
def load_table(tableName, path, thefile):
    print(tableName)
    print(path)
    print(thefile)
    load_sql_table(path.replace('+', '/') + '/' + thefile, tableName)
    print("Complete")
    return jsonify({'success': True})

@app.route('/loadTableWithDelimiter/<tableName>/<path>/<thefile>/<delimiter>')
def load_table_with_delimiter(tableName, path, thefile, delimiter):
    print(tableName)
    print(path)
    print(thefile)
    print(delimiter)
    load_sql_table_with_delimiter(path.replace('+', '/'), thefile, tableName, delimiter)
    print("Complete")
    return jsonify({'success': True})
