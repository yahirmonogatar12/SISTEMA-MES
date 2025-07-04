from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/tracking')
def tracking():
    return render_template('tracking.html')
