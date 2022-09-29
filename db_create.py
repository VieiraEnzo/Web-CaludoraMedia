import sqlite3

conn = sqlite3.connect("pf.db")
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS alunos
(dre INTEGER PRIMARY KEY, nome TEXT, senha TEXT)''' )

c.execute('''
CREATE TABLE IF NOT EXISTS notas
(dre INTEGER PRIMARY KEY, curso TEXT, p1 INTEGER, p2 INTEGER, p3 INTEGER)''' )

conn.commit()

