import sqlite3
conn = sqlite3.connect('database.db')
print("BD otwarta")
cur = conn.cursor()

conn.execute('CREATE TABLE uzytkownicy (login TEXT, haslo TEXT)')

print("tabela utworzona")

print(cur.fetchall())
conn.close()