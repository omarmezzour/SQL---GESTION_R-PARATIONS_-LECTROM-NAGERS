#MEZZOUR Omar

import sqlite3

# Fonction pour créer la base de données et les tables
def creer_base_de_donnees():
    # Se connecter à la base de données (elle sera créée si elle n'existe pas)
    conn = sqlite3.connect('mydb.db')
    cursor = conn.cursor()

    # Créer la table CLIENTE
    cursor.execute('''CREATE TABLE CLIENTE (
                        IDCli INTEGER PRIMARY KEY,
                        NomCli TEXT,
                        AdrCli TEXT,
                        VilleCli TEXT)''')

    # Créer la table CATEGORIE
    cursor.execute('''CREATE TABLE CATEGORIE (
                        IDCat INTEGER PRIMARY KEY,
                        libCat TEXT,
                        TarifMO REAL)''')

    # Créer la table APPAREIL
    cursor.execute('''CREATE TABLE APPAREIL (
                        IDApp INTEGER PRIMARY KEY,
                        DescApp TEXT,
                        RefConstApp TEXT,
                        MarqueApp TEXT,
                        IDCli INTEGER,
                        IDCat INTEGER,
                        FOREIGN KEY(IDCli) REFERENCES CLIENTE(IDCli),
                        FOREIGN KEY(IDCat) REFERENCES CATEGORIE(IDCat))''')

    # Créer la table PIECE
    cursor.execute('''CREATE TABLE PIECE (
                        IDPiece INTEGER PRIMARY KEY,
                        DescPiece TEXT,
                        PUHT REAL)''')

    # Créer la table ORDREREPARATION
    cursor.execute('''CREATE TABLE ORDREREPARATION (
                        IDOrdre INTEGER PRIMARY KEY,
                        DiagnosticPanne TEXT,
                        NbHeuresMO REAL,
                        IDApp INTEGER,
                        FOREIGN KEY(IDApp) REFERENCES APPAREIL(IDApp))''')

    # Créer la table PIECESACHANGER
    cursor.execute('''CREATE TABLE PIECESACHANGER (
                        IDPiece INTEGER,
                        IDOrdre INTEGER,
                        Quantite INTEGER,
                        PRIMARY KEY (IDPiece, IDOrdre),
                        FOREIGN KEY(IDPiece) REFERENCES PIECE(IDPiece),
                        FOREIGN KEY(IDOrdre) REFERENCES ORDREREPARATION(IDOrdre))''')

    # Commit les changements et fermer la connexion
    conn.commit()
    conn.close()

# Fonction pour ajouter des données aux tables
def ajouter_donnees():
    # Se connecter à la base de données
    conn = sqlite3.connect('mydb.db')
    cursor = conn.cursor()

    # Ajouter des données à la table CLIENTE
    cursor.execute("INSERT INTO CLIENTE (NomCli, AdrCli, VilleCli) VALUES (?, ?, ?)", ('Client1', 'Adresse1', 'Ville1'))
    cursor.execute("INSERT INTO CLIENTE (NomCli, AdrCli, VilleCli) VALUES (?, ?, ?)", ('Client2', 'Adresse2', 'Ville2'))

    # Ajouter des données à la table CATEGORIE
    cursor.execute("INSERT INTO CATEGORIE (libCat, TarifMO) VALUES (?, ?)", ('Catégorie1', 50.00))
    cursor.execute("INSERT INTO CATEGORIE (libCat, TarifMO) VALUES (?, ?)", ('Catégorie2', 60.00))

    # Ajouter des données à la table APPAREIL
    cursor.execute("INSERT INTO APPAREIL (DescApp, RefConstApp, MarqueApp, IDCli, IDCat) VALUES (?, ?, ?, ?, ?)",
                   ('Appareil1', 'Ref1', 'Marque1', 1, 1))
    cursor.execute("INSERT INTO APPAREIL (DescApp, RefConstApp, MarqueApp, IDCli, IDCat) VALUES (?, ?, ?, ?, ?)",
                   ('Appareil2', 'Ref2', 'Marque2', 2, 2))

    # Ajouter des données à la table PIECE
    cursor.execute("INSERT INTO PIECE (DescPiece, PUHT) VALUES (?, ?)", ('Pièce1', 20.00))
    cursor.execute("INSERT INTO PIECE (DescPiece, PUHT) VALUES (?, ?)", ('Pièce2', 25.00))

    # Ajouter des données à la table ORDREREPARATION
    cursor.execute("INSERT INTO ORDREREPARATION (DiagnosticPanne, NbHeuresMO, IDApp) VALUES (?, ?, ?)",
                   ('Panne1', 2.5, 1))
    cursor.execute("INSERT INTO ORDREREPARATION (DiagnosticPanne, NbHeuresMO, IDApp) VALUES (?, ?, ?)",
                   ('Panne2', 3.0, 2))

    # Ajouter des données à la table PIECESACHANGER
    cursor.execute("INSERT INTO PIECESACHANGER (IDPiece, IDOrdre, Quantite) VALUES (?, ?, ?)", (1, 1, 3))
    cursor.execute("INSERT INTO PIECESACHANGER (IDPiece, IDOrdre, Quantite) VALUES (?, ?, ?)", (2, 2, 2))

    # Commit les changements et fermer la connexion
    conn.commit()
    conn.close()

# Appel de la fonction pour créer la base de données et les tables
creer_base_de_donnees()

# Appel de la fonction pour ajouter des données
ajouter_donnees()