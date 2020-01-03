import numpy as np
import pickle
import hashlib
import json
import re

from bson import json_util
from flask import Flask, request, jsonify, render_template, abort
from flask_pymongo import PyMongo 
from flask_cors import CORS, cross_origin

mongo = PyMongo()

app = Flask(__name__)

app.config["MONGO_URI"] = 'connection string goes here'
#Example_____________
#app.config["MONGO_URI"] = 'mongodb+srv://<user>:<password>@strainercluster-igrpg.azure.mongodb.net/test?retryWrites=true&w=majority'
CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

mongo.init_app(app)

@app.route('/')
@cross_origin()
def home():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
@cross_origin()
def query():
    if not request.json or not 'queryId' in request.json:
        abort(400)
    queryToInsert = {
        'queryId': request.json['queryId'],
        'field1': request.json['field1'],
        'field2': request.json['field2'],
        'field3': request.json['field3']
    }
    query_collection = mongo.db.queries
    query_collection.insert(queryToInsert)
    return jsonify({'query': request.json['queryId'],'message': 'Query added successfully'}), 201

@app.route('/get/<id>', methods=['GET'])
@cross_origin()
def get(id):
    try:
        queryId = int(id)
    except:
        return jsonify({'message': 'Not a valid Id'}), 400
    
    query_collection = mongo.db.queries
    result = json.dumps(list(query_collection.find({'queryId' : queryId},{ "_id": 0, "field1": 1, "field2": 1, "field3": 1 })), default=json_util.default)
    if result == "[]":
        return jsonify({'queryId': queryId, 'message': 'No query is available for Id ' + id + ', rechek and try again!'}), 400
    return result, 200

if __name__ == "__main__":
    app.run(debug=True)