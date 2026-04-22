from flask import Flask, render_template

server = Flask(__name__)

pokemons = {
    "Squirtle": {
        "nombre": "Squirtle",
        "imagen": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png",
        "tipo": "Agua",
        "hp": "56",
        "ataque": "94",
        "defensa": "65",
        "velocidad": "50"
    }
}

@server.route("/")
def index():
    return render_template("tarjeta.html", datos = pokemons)

if __name__ == "__main__":
    server.run(debug=True)
