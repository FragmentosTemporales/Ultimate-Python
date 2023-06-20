import sqlite3

with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()
    usuarios = [
        (2, "Cristian Rivera"),
        (3, "Dante Amaro")
    ]
    cursor.executemany(
        "insert into usuarios values(?, ?)", 
        usuarios
        
    )