from flask import Blueprint  # type: ignore

start = Blueprint('start', __name__)  

@start.route('/')
def start_route():
    return 'Quiz Started'
