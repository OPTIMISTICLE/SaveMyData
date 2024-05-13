from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

try:
    client = MongoClient('mongodb://localhost:27017/')  # Connect to MongoDB server
    db = client.savemydata  # Select database
    collection = db.data  # Select collection
except Exception as e:
    print(e)

@app.route('/save', methods=["POST"])
def save():
    valeur = request.json['valeur']

    new_save = {"valeur": valeur}
    result = collection.insert_one(new_save)

    saved_data = collection.find_one({"_id": result.inserted_id})

    return jsonify({"id": str(saved_data["_id"])})

@app.route('/hello')
def hello_world():
    return "hello world"

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
