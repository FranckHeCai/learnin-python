from flask import render_template, Blueprint

second = Blueprint("second", __name__, template_folder="../templates")

@second.route('/home')
@second.route('/')
def home():
  return "Hello from second"

