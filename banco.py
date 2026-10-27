import sqlite3
from pathlib import Path

CAMINHO_BANCO =Path(__file__).with_name("financeiro.db")

def conectar():
    return sqlite3.connect(CAMINHO_BANCO)

def inicializar_banco():
    conexao = conectar()

    conexao.execute("""
    CREATE TABLE IF NOT EXISTS transacoes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL,
        valor REAL NOT NULL,
        tipo TEXT NOT NULL,
        categoria TEXT NOT NULL)
    """)
    conexao.commit()
    conexao.close()


def adicionar_transacao(descricao, valor, tipo, categoria):
    conexao = conectar()

    sql = """
        INSERT INTO transacoes (descricao, valor, tipo, categoria)
        VALUES (?, ?, ?, ?)
    """

    parametros = (descricao, valor, tipo, categoria)

    conexao.execute(sql, parametros)
    conexao.commit()
    conexao.close()



def listar_transacoes():
    conexao = conectar()
    conexao.row_factory = sqlite3.Row
    cursor = conexao.execute("""
    SELECT ID, descricao,valor,tipo,categoria
    FROM  transacoes
    ORDER BY id DESC
    """)
    transacoes = [dict(linha) for linha in cursor.fetchall()]

    conexao.close()

    return transacoes



def excluir_transacao(id_transacao):
    conexao = conectar()

    conexao.execute(
        "DELETE FROM transacoes WHERE id = ?",
        (id_transacao,)
    )

    conexao.commit()
    conexao.close()


def atualizar_transacao(id_transacao, descricao, valor, tipo, categoria):
    conexao = conectar()

    sql = """
        UPDATE transacoes
        SET descricao = ?, valor = ?, tipo = ?, categoria = ?
        WHERE id = ?
    """

    parametros = (descricao, valor, tipo, categoria, id_transacao)

    conexao.execute(sql, parametros)
    conexao.commit()
    conexao.close()
