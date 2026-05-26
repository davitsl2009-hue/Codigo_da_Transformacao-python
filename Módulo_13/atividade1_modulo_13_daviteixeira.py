from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/saudacao", methods=["GET"])
def saudacao():
    return jsonify({"mensagem": "Olá, seja bem-vindo à nossa API!"})

if __name__ == "__main__":
    app.run(debug=True)
