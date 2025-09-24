from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

auth = True

@app.route('/')
def home():
  return render_template("index.html")

@app.route('/login', methods = ["GET"])
def login():
  return render_template("login.html")
  
@app.route('/login', methods = ["POST"])
def login_user():
  user = request.form['name']
  return redirect(url_for("user", user = user))

@app.route('/user/<user>')
def user(user):
  return render_template("user.html", user = user)

app.run(debug=True)
