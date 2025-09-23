from flask import Flask, render_template

app = Flask(__name__)

# Sample Data
teams = [
    {"name": "Real Madrid", "country": "Spain", "titles": 14},
    {"name": "Manchester United", "country": "England", "titles": 3},
    {"name": "Bayern Munich", "country": "Germany", "titles": 6},
    {"name": "AC Milan", "country": "Italy", "titles": 7},
    {"name": "SIT Team", "country": "Susgaon", "titles": 4},
    {"name": "AIU Team", "country": "Pimpli Saudagar", "titles": 10},
    {"name": "SIU Team", "country": "Baner", "titles": 6}
]

players = [
    {"name": "Lionel Messi", "club": "Inter Miami", "country": "Argentina"},
    {"name": "Cristiano Ronaldo", "club": "Al Nassr", "country": "Portugal"},
    {"name": "Kylian Mbappé", "club": "PSG", "country": "France"},
    {"name": "Erling Haaland", "club": "Manchester City", "country": "Norway"},
    {"name": "ASHU", "club": "SITFC", "country": "India"},
    {"name": "Labdhi", "club": "AIUFC", "country": "India"},
    {"name": "Alan", "club": "FCSIU", "country": "India"}

]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/teams")
def show_teams():
    return render_template("teams.html", teams=teams)

@app.route("/players")
def show_players():
    return render_template("players.html", players=players)

if __name__ == "__main__":
    app.run(debug=True)
