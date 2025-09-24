from flask import Flask, redirect, url_for

app = Flask(__name__)

auth = True

@app.route('/')
def home():
  return "Hello this is the main page! <h1>HELLO</h1>"

@app.route('/user/<name>', methods = ["GET"])
def user(name):
  return f"Hello {name}"

@app.route("/admin/")
def admin():
  if not auth:
    return redirect(url_for("home"))
  
  return redirect(url_for("user", name = "admin"))

app.run()
