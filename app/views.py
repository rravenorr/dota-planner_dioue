from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)

@views.route('/')
@views.route('/index')
@views.route('/home')
def home():
    return render_template("home.html")