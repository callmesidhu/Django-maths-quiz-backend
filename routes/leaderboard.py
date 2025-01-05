from flask import Blueprint

leaderboard = Blueprint('leaderboard', __name__)  # Define the 'leaderboard' blueprint, not a function

@leaderboard.route('/')
def leaderboard_route():
    return 'Quiz Leaderboard'
