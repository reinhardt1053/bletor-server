from flask import Flask, jsonify, request, abort, render_template
from flask.ext.sqlalchemy import SQLAlchemy

#Application Setup
app = Flask(__name__)
app.config.from_object('settings')

#Database Setup
db = SQLAlchemy(app)  

@app.route('/api/', methods=['GET', 'OPTIONS'])
def index():
  response = jsonify({'status' : 'online'})
  return response
