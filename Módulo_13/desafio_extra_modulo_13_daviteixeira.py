import sqlite3
import hashlib
from flask import Flask, request, jsonify

app = Flask(__name__)

def init_db():
    con = sqlite3.connect("blog.db")
    cur = con.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL
        )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            conteudo TEXT NOT NULL,
            autor_id INTEGER,
            FOREIGN KEY (autor_id) REFERENCES usuarios(id)
        )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS comentarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            conteudo TEXT NOT NULL,
            post_id INTEGER,
            autor_id INTEGER,
            FOREIGN KEY (post_id) REFERENCES posts(id),
            FOREIGN KEY (autor_id) REFERENCES usuarios(id)
        )
    ''')

    con.commit()
    con.close()

init_db()

def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

@app.route("/cadastrar", methods=["POST"])
def cadastrar_usuario():
    dados = request.get_json()
    nome, email, senha = dados.get("nome"), dados.get("email"), dados.get("senha")

    if not nome or not email or not senha:
        return jsonify({"erro": "Dados inválidos"}), 400

    try:
        con = sqlite3.connect("blog.db")
        cur = con.cursor()
        cur.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)",
                    (nome, email, hash_senha(senha)))
        con.commit()
        con.close()
        return jsonify({"mensagem": "Usuário cadastrado com sucesso!"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"erro": "Email já cadastrado"}), 400

@app.route("/login", methods=["POST"])
def login():
    dados = request.get_json()
    email, senha = dados.get("email"), dados.get("senha")

    con = sqlite3.connect("blog.db")
    cur = con.cursor()
    cur.execute("SELECT id, senha FROM usuarios WHERE email=?", (email,))
    usuario = cur.fetchone()
    con.close()

    if usuario and usuario[1] == hash_senha(senha):
        return jsonify({"mensagem": "Login bem-sucedido", "usuario_id": usuario[0]}), 200
    return jsonify({"erro": "Credenciais inválidas"}), 401

@app.route("/posts", methods=["POST"])
def criar_post():
    dados = request.get_json()
    titulo, conteudo, autor_id = dados.get("titulo"), dados.get("conteudo"), dados.get("autor_id")

    con = sqlite3.connect("blog.db")
    cur = con.cursor()
    cur.execute("INSERT INTO posts (titulo, conteudo, autor_id) VALUES (?, ?, ?)",
                (titulo, conteudo, autor_id))
    con.commit()
    con.close()
    return jsonify({"mensagem": "Post criado com sucesso!"}), 201

@app.route("/posts", methods=["GET"])
def listar_posts():
    con = sqlite3.connect("blog.db")
    cur = con.cursor()
    cur.execute("SELECT id, titulo, conteudo, autor_id FROM posts")
    rows = cur.fetchall()
    con.close()

    posts = [{"id": r[0], "titulo": r[1], "conteudo": r[2], "autor_id": r[3]} for r in rows]
    return jsonify({"posts": posts})

@app.route("/comentarios", methods=["POST"])
def adicionar_comentario():
    dados = request.get_json()
    conteudo, post_id, autor_id = dados.get("conteudo"), dados.get("post_id"), dados.get("autor_id")

    con = sqlite3.connect("blog.db")
    cur = con.cursor()
    cur.execute("INSERT INTO comentarios (conteudo, post_id, autor_id) VALUES (?, ?, ?)",
                (conteudo, post_id, autor_id))
    con.commit()
    con.close()
    return jsonify({"mensagem": "Comentário adicionado com sucesso!"}), 201

@app.route("/comentarios/<int:post_id>", methods=["GET"])
def listar_comentarios(post_id):
    con = sqlite3.connect("blog.db")
    cur = con.cursor()
    cur.execute("SELECT id, conteudo, autor_id FROM comentarios WHERE post_id=?", (post_id,))
    rows = cur.fetchall()
    con.close()

    comentarios = [{"id": r[0], "conteudo": r[1], "autor_id": r[2]} for r in rows]
    return jsonify({"comentarios": comentarios})

if __name__ == "__main__":
    app.run(debug=True)
