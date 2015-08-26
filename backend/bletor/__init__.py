from flask import Flask, jsonify
from flask.ext.sqlalchemy import SQLAlchemy

#Application Setup
app = Flask(__name__)
app.config.from_object('settings')

#Database Setup
db = SQLAlchemy(app)  

@app.route('/api/', methods=['GET'])
def index():
  return jsonify({'status' : 'online'})
