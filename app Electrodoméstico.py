from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("tarjeta.html", lights="base")

@app.route("/<tipo>/<int:coeficiente>")
def mostrar_opcion(tipo, coeficiente):
    return f"""
    <h1>Resultado</h1>
    <p>Tipo seleccionado: {tipo}</p>
    <p>Coeficiente: {coeficiente}</p>
    <a href="/">Volver</a>
    """

if __name__ == "__main__":
    app.run(debug=True)
