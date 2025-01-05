from flask import Flask # type: ignore
from routes.start import start  
from routes.leaderboard import leaderboard  
from configs.connection import create_connection

app = Flask(__name__)

@app.route('/')
def index():
    connection = create_connection()
    if connection:
        return "Connected to MySQL database!"
    else:
        return "Failed to connect to the database."

# Register Blueprints with URL prefixes
app.register_blueprint(start, url_prefix='/start')
app.register_blueprint(leaderboard, url_prefix='/leaderboard')

if __name__ == '__main__':
    app.run(debug=True)
