from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "test"
app.permanent_session_lifetime = timedelta(minutes= 2)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
auth = True

db = SQLAlchemy(app)

class users(db.Model):
  _id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(100))
  email = db.Column(db.String(100))

  def __init__(self, name, email):
    self.name = name
    self.email = email

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

  found_user = users.query.filter_by(name = user).first()

  if found_user :
    session["email"] = found_user.email
  else:
    new_user = users(user, None)
    db.session.add(new_user)
    db.session.commit()

  flash("Logged Sucessfully!", "info")
  return redirect(url_for("user", user = user))

@app.route('/user/', methods = ["GET", "POST"])
def user():
  email = None
  if "user" in session:
    user = session["user"]
    if request.method == "POST":
      flash("Email saved!")
      email = request.form["email"]
      session["email"] = email
      found_user = users.query.filter_by(name = user).first()
      found_user.email = email
      db.session.commit()
    else:
      if "email" in session:
        email = session["email"]
    return render_template("user.html", user = user, email = email)
  else:
    return redirect(url_for("login"))
@app.route('/users')
def get_users():
  return render_template("users.html", values = users.query.all())

@app.route('/logout')
def logout():
  if "user" in session:
    user = session["user"]
    flash(f"{user} Logged out successfully!", "info")
  session.pop("user", None)
  session.pop("email", None)
  return redirect(url_for("login"))

with app.app_context():
  db.create_all()
app.run(debug=True)

