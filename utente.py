def menu_utente(id_utente, conn, cursor):

    while True:
        print("MENU UTENTE")
        print("1. Cerca libri")
        print("2. I miei prestiti")
        print("3. Profilo")
        print("0. Esci")

        scelta = input("Scelta: ")

        
        # CERCA LIBRI 
    
        if scelta == "1":
            cursor.execute("""
            SELECT libri.titolo, libri.autore, categoria.nome_categoria
            FROM libri
            JOIN categoria ON libri.ID_categoria = categoria.ID_categoria
            """)

            for l in cursor.fetchall():
                print(l)

    
        # PRESTITI UTENTE
        
        elif scelta == "2":
            cursor.execute("""
            SELECT libri.titolo, prestiti.data_prestito, prestiti.data_restituzione
            FROM prestiti
            JOIN libri ON prestiti.ID_libri = libri.ID_libri
            WHERE prestiti.ID_utenti = %s
            """, (id_utente,))

            for p in cursor.fetchall():
                print(p)

        
        # PROFILO

        elif scelta == "3":
            cursor.execute("""
            SELECT nome, cognome, email, ruolo
            FROM utenti
            WHERE ID_utenti = %s
            """, (id_utente,))

            print(cursor.fetchone())

        elif scelta == "0":
            break

