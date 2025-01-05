from flask import Blueprint

start = Blueprint('start', __name__)  # Define the 'start' blueprint, not a function

@start.route('/')
def start_route():
    return 'Quiz Started'
