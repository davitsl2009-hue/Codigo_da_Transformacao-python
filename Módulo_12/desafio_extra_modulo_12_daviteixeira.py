from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/ping")
def ping():
    return jsonify({"message": "pong"})

@app.route("/soma/<int:a>/<int:b>")
def soma(a, b):
    return jsonify({"resultado": a + b})

@app.route("/dividir/<int:a>/<int:b>")
def dividir(a, b):
    if b == 0:
        return jsonify({"erro": "Divisão por zero"}), 400
    return jsonify({"resultado": a / b})

if __name__ == "__main__":
    app.run(debug=True)
