CREATE DATABASE biblioteca_db ;
USE biblioteca_db ;

CREATE TABLE categoria (
	ID_categoria INT PRIMARY KEY AUTO_INCREMENT ,
    nome_categoria VARCHAR(100) 
) ;

CREATE TABLE libri (
ID_libri INT PRIMARY KEY AUTO_INCREMENT ,
titolo VARCHAR(100) NOT NULL ,
autore VARCHAR(100) NOT NULL ,

ID_categoria INT ,
FOREIGN KEY (ID_categoria ) REFERENCES categoria(ID_categoria) ON DELETE CASCADE 
) ;

CREATE TABLE utenti (
ID_utenti INT PRIMARY KEY AUTO_INCREMENT ,
nome VARCHAR(100) NOT NULL ,
cognome VARCHAR(100) NOT NULL ,
email VARCHAR(100) NOT NULL UNIQUE ,
ruolo VARCHAR(100) CHECK (ruolo IN ('admin', 'utente'))
) ;

CREATE TABLE prestiti (
ID_prestiti INT PRIMARY KEY AUTO_INCREMENT ,
ID_libri INT ,
FOREIGN KEY (ID_libri) REFERENCES libri(ID_libri) ON DELETE CASCADE ,
ID_utenti INT , 
FOREIGN KEY (ID_utenti) REFERENCES utenti(ID_utenti) ON DELETE CASCADE ,
data_prestito DATE NOT NULL,
data_restituzione DATE 
);

