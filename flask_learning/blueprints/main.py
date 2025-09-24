from flask import Flask, Blueprint, render_template
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from admin.second import second

app = Flask(__name__)
app.register_blueprint(second, url_prefix = "/second/")


@app.route('/')
def home():
  return "Hello"

app.run(debug=True)

