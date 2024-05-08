from flask import Flask, request, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

try:
    db_path = 'mysql+pymysql://root:root@localhost:3306/savemydata'  # Modifier le chemin de la base de données si nécessaire
    engine = create_engine(db_path)
    Session = sessionmaker(bind=engine)
    session = Session()
except Exception as e:
    print(e)
@app.route('/save', methods=["POST"])
def save():

    valeur = request.json['valeur']

    new_save = Data(valeur)
    session.add(new_save)
    session.commit()

    saved_data = session.query(Data).get(new_save.id)

    return jsonify({"id": saved_data.id})

@app.route('/hello')
def hello_world():
    return "hello world"

if __name__ == '__main__':
    app.run()