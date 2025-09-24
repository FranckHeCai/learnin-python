from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
  return render_template("index.html", content = "This is the homepage")

@app.route('/user/')
def user():
  return render_template("user.html", user = "Zuko")

app.run(debug=True)