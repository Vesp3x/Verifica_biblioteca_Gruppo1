import mysql.connector

# Configurazione connessione
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'biblioteca_db'
}

try:
    conn = mysql.connector.connect(**db_config)

    if conn.is_connected():
        print("Connessione riuscita!")

except mysql.connector.Error as err:
    print(f"Errore di connessione: {err}")
    exit()

cursor = conn.cursor()

#inserimento dati categoria
sql = """
INSERT INTO categoria (nome_categoria)
VALUES (%s), (%s), (%s)
"""

valori = ("Fantasy", "Horror", "Romanzo")

cursor.execute(sql, valori)
conn.commit()

print("Categorie inserite")


cursor = conn.cursor()

# inserimento dati libri
sql = """
INSERT INTO libri (titolo, autore, ID_categoria)
ViALUES (%s, %s, %s), (%s, %s, %s), (%s, %s, %s)
"""

valori = (
    "Harry Potter", "J.K Rowling", 1,
    "Dracula", "Bram Stoker", 2,
    "Il Nome della Rosa", "Umberto Eco", 3
)

cursor.execute(sql, valori)
conn.commit()

print("Libri inseriti")


cursor = conn.cursor()

# inserimento dati utenti
sql = """
INSERT INTO utenti (nome, cognome, email, ruolo)
VALUES (%s, %s, %s, %s), (%s, %s, %s, %s)
"""

valori = (
    "Mario", "Rossi", "mario@gmail.com", "admin",
    "Luca", "Bianchi", "luca@gmail.com", "utente"
)

cursor.execute(sql, valori)
conn.commit()

print("Utenti inseriti")


cursor = conn.cursor()

# inserimento dati prestiti
sql = """
INSERT INTO prestiti (ID_libri, ID_utenti, data_prestito, data_restituzione)
VALUES (%s, %s, %s, %s)
"""

valori = (1, 2, "2026-05-10", None)

cursor.execute(sql, valori)
conn.commit()

print("Prestito inserito")


cursor.close()
conn.close()
print("Connessione chiusa")




















