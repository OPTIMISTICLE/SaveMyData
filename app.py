from bson import ObjectId
from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import certifi

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

try:
    client = MongoClient("mongodb+srv://mondesir:mondesir123@cluster0.kdd7s4g.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", tlsCAFile=certifi.where())
    db = client.savemydata  # Select database
    collection = db.data  # Select collection
except Exception as e:
    print(e)

@app.route('/save', methods=["POST"])
def save():
    valeur = request.json
    filter_query = {"_id": ObjectId("66424f99f85f46c3d2768f06")}

    # Specify the new nested object for the time entry
    new_time_entry = {
        "source": "NewSource",
        "intensity": 300,
        "voltage": 250
    }

    # Specify the update operation
    update_operation = {
        "$set": {
            f"SiteA.zoneB.2024-01-01.01:00:00": new_time_entry
        }
    }

    # Update the document
    result = collection.update_one(filter_query, update_operation)

    new_save = valeur
    result = collection.insert_one(new_save)

    saved_data = collection.find_one({"_id": result.inserted_id})

    return jsonify({"id": str(saved_data["_id"])})

@app.route('/hello')
def hello_world():
    return "hello world"

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
