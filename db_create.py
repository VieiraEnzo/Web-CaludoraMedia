import sqlite3

conn = sqlite3.connect("pf.db")
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS alunos

''' )

