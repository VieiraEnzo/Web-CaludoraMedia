import sqlite3

conn = sqlite3.connect("pf.db")
c = conn.cursor()

a = input("quem deletar: ")

c.execute('''
DELETE FROM alunos WHERE nome = ? ''', (a,) )

b = c.execute("SELECT * FROM alunos").fetchall()



conn.commit()