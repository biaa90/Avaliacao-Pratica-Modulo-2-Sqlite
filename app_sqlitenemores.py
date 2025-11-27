import sqlite3

conexão = sqlite3.connect("escola.db")

conexão.execute("""
CREATE TABLE IF NOT EXISTS alunos(
id INTEGER NOT NULL PRIMARY KEY,
nome  TEXT NOT NULL,
idade INTEGER,
email TEXT);

""")

conexão.execute ("""
INSERT INTO alunos (nome, idade, email ) VALUES 
                    ("clarice", "24", "claricediva@gmail.com"),
                    ("luiz", "15", "luiz@gmail.com"  ),
                    ("larissa", "21", "larissa@gmail.com");
""")

lista_alunos = conexão.execute ("SELECT * FROM alunos").fetchall()
print ("alunos: ", lista_alunos)

aluno = conexão.execute("SELECT * FROM alunos WHERE id = 3").fetchone()
print ("Aluno 3", aluno)

conexão.execute("UPDATE alunos SET nome = 'Larissa' WHERE nome = 'Clarice'")

lista_alunos = conexão.execute ("SELECT * FROM alunos").fetchall()
print ("alunos: ", lista_alunos)

conexão.execute("DELETE FROM alunos WHERE id=2 ")