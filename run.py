from flask import Flask
from routes.start import start  # Importing the 'start' blueprint from routes/start.py
from routes.leaderboard import leaderboard  # Importing the 'leaderboard' blueprint from routes/leaderboard.py

app = Flask(__name__)

@app.route('/')
def backend():
    return 'Flutter Quiz App Backend'

# Register Blueprints with URL prefixes
app.register_blueprint(start, url_prefix='/start')
app.register_blueprint(leaderboard, url_prefix='/leaderboard')

if __name__ == '__main__':
    app.run(debug=True)
