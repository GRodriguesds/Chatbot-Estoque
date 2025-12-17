import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "estoque.db"

def buscar_produtos():
    conn = sqlite3.connect("estoque.db")
    cursor = conn.cursor()

    cursor.execute("SELECT nome, quantidade FROM estoque")
    resultados = cursor.fetchall()

    conn.close()

    return [
        {"nome": nome.lower(), "quantidade": quantidade}
        for nome, quantidade in resultados
    ]
