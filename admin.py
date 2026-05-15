def menu_admin(id_admin, conn, cursor):

    while True:
        print("\nMENU ADMIN")
        print("1. Aggiungi libro e categoria")
        print("2. Elimina libro")
        print("3. Modifica libro")
        print("4. Promuovi utente")
        print("5. Visualizza iscritti")
        print("6. Rientro prestiti")
        print("7. Elimina utente")
        print("0. Esci")

        scelta = input("Scelta: ")

        # =========================
        if scelta == "1":

            titolo = input("Titolo: ")
            autore = input("Autore: ")
            id_cat = input("ID categoria: ")

            sql = """
            INSERT INTO libri (titolo, autore, ID_categoria)
            VALUES (%s, %s, %s)
            """

            valori = (titolo, autore, id_cat)

            cursor.execute(sql, valori)
            conn.commit()

            print("Libro aggiunto")

        # =========================
        elif scelta == "2":

            titolo_libro = input("Nome libro da eliminare: ")

            sql = "DELETE FROM libri WHERE titolo = %s"

            cursor.execute(sql, (titolo_libro,))
            conn.commit()

            print("Libro eliminato")

        # =========================
        elif scelta == "3":

            titolo_libro = input("Nome libro da modificare: ")
            nuovo_titolo = input("Nuovo titolo da inserire: ")

            sql = """
            UPDATE libri
            SET titolo = %s
            WHERE titolo = %s
            """

            cursor.execute(sql, (nuovo_titolo, titolo_libro))
            conn.commit()

            print("Libro modificato")

        # =========================
        elif scelta == "4":

            email_utente = input("Email utente da promuovere: ")

            sql = """
            UPDATE utenti
            SET ruolo = 'admin'
            WHERE email = %s
            """

            cursor.execute(sql, (email_utente,))
            conn.commit()

            print("Utente promosso")

        # =========================
        elif scelta=="5":

            print("\nLISTA UTENTI")

            sql = """
            SELECT nome, cognome, email, ruolo
            FROM utenti
            """

            cursor.execute(sql)

            risultati = cursor.fetchall()

            for u in risultati:
                print(u)

        # =========================
        elif scelta == "6":

            id_prestito = input("ID prestito da rientrare: ")

            sql = """
            UPDATE prestiti
            SET data_restituzione = CURDATE()
            WHERE ID_prestiti = %s
            """

            cursor.execute(sql, (id_prestito,))
            conn.commit()

            print("Prestito chiuso")

        # =========================
        elif scelta == "7":

            email_utente = input("Email utente da eliminare: ")

            sql = "DELETE FROM utenti WHERE email = %s"

            cursor.execute(sql, (email_utente,))
            conn.commit()

            print("Utente eliminato")

        # =========================
        elif scelta == "0":
            break

        else:
            print("Scelta non valida")
