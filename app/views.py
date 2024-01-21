from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
@views.route('/index')
@views.route('/home')
def home():
    return render_template("base.html")