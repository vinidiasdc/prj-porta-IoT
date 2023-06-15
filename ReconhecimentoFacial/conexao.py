import sqlite3
from datetime import datetime

def CriarTabelaDeImagens():
    conn = sqlite3.connect("bancoImagens.db")
    cursor = conn.cursor()

    comando_criacao_tabela_sql =  """
        CREATE TABLE IF NOT EXISTS imagens_usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            foto BLOB NOT NULL,
            registro DATETIME
        )
    """

    cursor.execute(comando_criacao_tabela_sql)

    conn.commit()
    cursor.close()
    conn.close()

CriarTabelaDeImagens()

def CriarImagensPessoasAutorizadas():
    conn = sqlite3.connect("bancoImagens.db")
    cursor = conn.cursor()

    sql = "SELECT foto FROM imagens_usuarios"

    cursor.execute(sql)
    i = 0
    qtdImagens = []
    for row in cursor.fetchall():
        dados_imagem = row[0]
        i = i + 1
        nome_arquivo = f"imagem_user_{i}.jpg"

        with open(nome_arquivo, 'wb') as arquivo:
            arquivo.write(dados_imagem)
        
        qtdImagens.append(i)

    cursor.close()
    conn.close()

    return qtdImagens

def ConverterImagemEmBlob(caminho_imagem):
    with open(caminho_imagem, 'rb') as arquivo_imagem:
        blob_imagem = arquivo_imagem.read()
    return blob_imagem

def SalvarImagemNoBanco(imagem):
    conn = sqlite3.connect("bancoImagens.db")
    cursor = conn.cursor()

    blob_imagem = ConverterImagemEmBlob(imagem)
    datetime_atual = datetime.now()
    data_formatada = datetime_atual.strftime('%Y-%m-%d %H:%M:%S')

    sql = "INSERT INTO imagens_usuarios (foto, registro) VALUES(?, ?);"

    cursor.execute(sql, (blob_imagem, data_formatada))

    conn.commit()
    cursor.close()
    conn.close()
