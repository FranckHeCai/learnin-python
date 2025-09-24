from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
  return render_template("index.html", content = "This is the homepage")

@app.route('/user/<name>')
def user(name):
  return render_template("index.html", content = f"This is the {name} page")

@app.route('/list')
def list():
  return render_template("index.html", list = ["Zuko", "Aang", "Katara"])

app.run(debug=True)