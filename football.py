from flask import Flask, render_template

app = Flask(__name__)

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
    app.run(debug=True)
