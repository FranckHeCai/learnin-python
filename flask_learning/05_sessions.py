from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "test"
app.permanent_session_lifetime = timedelta(days= 2)

auth = True

@app.route('/')
def home():
  return render_template("index.html")

@app.route('/login', methods = ["GET"])
def login():
  if "user" in session:
    flash("Already Logged in!", "info")
    return redirect("user")
  else:
    return render_template("login.html")
  
@app.route('/login', methods = ["POST"])
def login_user():
  user = request.form['name']
  session.permanent = True
  session["user"] = user
  flash("Logged Sucessfully!", "info")
  return redirect(url_for("user", user = user))

@app.route('/user/')
def user():
  if "user" in session:
    user = session["user"]
    return render_template("user.html", user = user)
  else:
    redirect(url_for("login"))

@app.route('/logout')
def logout():
  if "user" in session:
    user = session["user"]
    flash(f"{user} Logged out successfully!", "info")
  session.pop("user", None)
  return redirect(url_for("login"))
app.run(debug=True)
