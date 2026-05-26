import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def init_db():
    con = sqlite3.connect("usuarios.db")
    cur = con.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    con.commit()
    con.close()

init_db()

@app.route("/saudacao", methods=["GET"])
def saudacao():
    return jsonify({"mensagem": "Olá, seja bem-vindo à nossa API!"})

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    dados = request.get_json()

    if not dados or "nome" not in dados or "email" not in dados:
        return jsonify({"erro": "Dados inválidos. Informe nome e email."}), 400

    nome = dados["nome"]
    email = dados["email"]

    try:
        con = sqlite3.connect("usuarios.db")
        cur = con.cursor()
        cur.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
        con.commit()
        con.close()

        return jsonify({
            "mensagem": "Usuário cadastrado com sucesso!",
            "usuario": {"nome": nome, "email": email}
        }), 201

    except Exception as e:
        return jsonify({"erro": f"Erro ao salvar no banco: {str(e)}"}), 500

@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    con = sqlite3.connect("usuarios.db")
    cur = con.cursor()
    cur.execute("SELECT id, nome, email FROM usuarios")
    rows = cur.fetchall()
    con.close()

    usuarios = [{"id": r[0], "nome": r[1], "email": r[2]} for r in rows]
    return jsonify({"usuarios": usuarios})

if __name__ == "__main__":
    app.run(debug=True)
