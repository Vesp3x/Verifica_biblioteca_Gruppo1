import mysql.connector
import utente
import admin


# CONNESSIONE DATABASE

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'biblioteca_db'
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()


email = input("Inserisci email: ")

cursor.execute("""
SELECT ID_utenti, nome, cognome, email, ruolo
FROM utenti
WHERE email = %s
""", (email,))

dati = cursor.fetchone()

if dati is None:
    print("Utente non trovato")
    exit()

ID_utenti, nome, cognome, email_db, ruolo = dati

print(f"\n Benvenuto {nome} {cognome}")


if ruolo == "admin":
    admin.menu_admin(ID_utenti, conn, cursor)
else:
    utente.menu_utente(ID_utenti, conn, cursor)

# CHIUSURA FINALE

cursor.close()
conn.close()
