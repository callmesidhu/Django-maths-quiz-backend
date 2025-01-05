from flask import Blueprint # type: ignore


leaderboard = Blueprint('leaderboard', __name__)  

@leaderboard.route('/')
def leaderboard_route():
    return 'Quiz Leaderboard'
