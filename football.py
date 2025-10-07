import os
from flask import Flask, render_template
from dotenv import load_dotenv

# Load .env file
load_dotenv()

app = Flask(__name__)

# Use environment variable for secret key
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'defaultsecret')

# Sample Data
players = [
    {"name": "Lionel Messi", "club": "Inter Miami", "country": "Argentina"},
    {"name": "Cristiano Ronaldo", "club": "Al Nassr", "country": "Portugal"},
    {"name": "Kylian Mbappé", "club": "PSG", "country": "France"},
    {"name": "Erling Haaland", "club": "Manchester City", "country": "Norway"}
]

teams = [
    {"name": "Real Madrid", "country": "Spain", "titles": 14},
    {"name": "Manchester United", "country": "England", "titles": 3},
    {"name": "Bayern Munich", "country": "Germany", "titles": 6},
    {"name": "AC Milan", "country": "Italy", "titles": 7}
]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/players')
def show_players():
    return render_template("players.html", players=players)

@app.route('/teams')
def show_teams():
    return render_template("teams.html", teams=teams)

if __name__ == "__main__":
    debug_mode = os.getenv('DEBUG', 'False') == 'True'
    app.run(debug=debug_mode)
