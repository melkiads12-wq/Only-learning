from flask import Flask, request, redirect
import sqlite3

app = Flask(__name__)

# Criar banco e tabela se não existir
def init_db():
    conn = sqlite3.connect("meubanco.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto TEXT NOT NULL,
            vencimento TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

@app.route("C:\\Study\\HTML\\SalvFormValid.py", methods=["POST"])
def salvar():
    produto = request.form["produto"]
    vencimento = request.form["vencimento"]

    conn = sqlite3.connect("meubanco.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (produto, vencimento) VALUES (?, ?)", (produto, vencimento))
    conn.commit()
    conn.close()

    return "Dados salvos com sucesso!"

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
