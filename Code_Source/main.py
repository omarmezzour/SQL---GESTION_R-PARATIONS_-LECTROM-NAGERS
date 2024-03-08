#MEZZOUR Omar

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3

# Fonction de connexion à la base de données
def connect_database():
    try:
        conn = sqlite3.connect('mydb.db')
        return conn
    except sqlite3.Error as e:
        messagebox.showerror("Erreur", f"Erreur de connexion à la base de données : {e}")
        return None

# Fonction permettant d'afficher les résultats dans une zone de texte
def display_results(results):
    result_text.delete("1.0", tk.END)
    for result in results:
        result_text.insert(tk.END, result)
        result_text.insert(tk.END, "\n")

# Fonction d'insertion d'un ordre de réparation
def inserer_ordre_reparation():
    # Get data from entry fields
    diagnostic_panne = diag_entry.get()
    nb_heures_mo = float(nb_heures_entry.get())
    id_appareil = int(id_appareil_entry.get())

    # Insérer l'ordre de réparation dans la table ORDREREPARATION
    try:
        cursor.execute("INSERT INTO ORDREREPARATION (DiagnosticPanne, NbHeuresMO, IDApp) VALUES (?, ?, ?)",
                        (diagnostic_panne, nb_heures_mo, id_appareil))
        conn.commit()
        messagebox.showinfo("Confirmation", "L'ordre de réparation a été inséré avec succès.")
    except sqlite3.Error as e:
        messagebox.showerror("Erreur", f"Erreur lors de l'insertion de l'ordre de réparation : {e}")

# Fonction de recherche d'un client par son nom
def rechercher_client():
    # Obtenir le nom du champ d'entrée
    nom_client = nom_client_entry.get()

    # Requête pour rechercher le client par son nom
    try:
        cursor.execute("SELECT * FROM CLIENTE WHERE NomCli=?", (nom_client,))
        results = cursor.fetchall()
        display_results(results)
    except sqlite3.Error as e:
        messagebox.showerror("Erreur", f"Erreur lors de la recherche du client : {e}")

# Fonction permettant de calculer le montant total des commandes de réparation d'un client
def calculer_montant_total():
    # Obtenir le nom du client à partir du champ de saisie
    nom_client = nom_client_entry.get()

    # Requête pour obtenir l'identifiant du client à partir de son nom
    try:
        cursor.execute("SELECT IDCli FROM CLIENTE WHERE NomCli=?", (nom_client,))
        resultats = cursor.fetchall()

        if resultats:
            id_client = resultats[0][0]
            # Requête pour obtenir les ordres de réparation de l'appareil du client
            cursor.execute("SELECT IDOrdre, NbHeuresMO FROM ORDREREPARATION WHERE IDApp IN "
                            "(SELECT IDApp FROM APPAREIL WHERE IDCli=?)", (id_client,))
            ordres = cursor.fetchall()

            if ordres:
                montant_total = sum(2.5 * ordre[1] for ordre in ordres)  # En supposant que le taux de main-d'œuvre est de 2,5 par heure
                montant_total += montant_total * 0.2  # 20% TVA
                messagebox.showinfo("Montant Total de la Facture", f"Montant total de la facture pour '{nom_client}': {montant_total:.2f} €")
            else:
                messagebox.showinfo("Montant Total de la Facture", f"Aucun ordre de réparation trouvé pour '{nom_client}'.")
        else:
            messagebox.showinfo("Montant Total de la Facture", f"Aucun client trouvé avec le nom '{nom_client}'.")
    except sqlite3.Error as e:
        messagebox.showerror("Erreur", f"Erreur lors du calcul du montant total de la facture : {e}")

# Fonction permettant d'afficher les pièces dont le prix est supérieur à un montant donné
def afficher_pieces_superieures():
    # Obtenir le prix d'un champ d'entrée
    prix_donne = float(prix_entry.get())

    # Requête pour obtenir des pièces dont le prix est supérieur au montant donné
    try:
        cursor.execute("SELECT * FROM PIECE WHERE PUHT > ?", (prix_donne,))
        results = cursor.fetchall()
        display_results(results)
    except sqlite3.Error as e:
        messagebox.showerror("Erreur", f"Erreur lors de l'affichage des pièces supérieures : {e}")

# Fonction d'affichage des ordres de réparation sans pièces à changer
def afficher_ordres_sans_pieces():
    # Requête pour obtenir des ordres de réparation sans pièces à changer
    try:
        cursor.execute("SELECT * FROM ORDREREPARATION WHERE IDOrdre NOT IN "
                        "(SELECT IDOrdre FROM PIECESACHANGER WHERE Quantite > 0)")
        results = cursor.fetchall()
        display_results(results)
    except sqlite3.Error as e:
        messagebox.showerror("Erreur", f"Erreur lors de l'affichage des ordres sans pièces à changer : {e}")

# Créer une nouvelle fenêtre
root = tk.Tk()
root.title("Gestion des Réparations d'Appareils")

# Charger l'image de fond
background_image = Image.open("background_image.jpg")  # Specify the path to your image
background_photo = ImageTk.PhotoImage(background_image)

# Définir l'image de fond
background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)

# Créer des cadres
frame_rechercher_client = tk.Frame(root)
frame_rechercher_client.pack(pady=10)

frame_inserer_ordre = tk.Frame(root)
frame_inserer_ordre.pack(pady=10)

frame_calcul_montant = tk.Frame(root)
frame_calcul_montant.pack(pady=10)

frame_afficher_pieces = tk.Frame(root)
frame_afficher_pieces.pack(pady=10)

frame_afficher_ordres = tk.Frame(root)
frame_afficher_ordres.pack(pady=10)

# Connexion à la base de données
conn = connect_database()
if conn:
    cursor = conn.cursor()

# Créer des widgets
nom_client_label = tk.Label(frame_rechercher_client, text="Nom de la Cliente:")
nom_client_label.grid(row=0, column=0)
nom_client_entry = tk.Entry(frame_rechercher_client)
nom_client_entry.grid(row=0, column=1)

result_text = tk.Text(frame_rechercher_client, width=50, height=10)
result_text.grid(row=1, columnspan=2)

rechercher_button = tk.Button(frame_rechercher_client, text="Rechercher Cliente", command=rechercher_client)
rechercher_button.grid(row=0, column=2, padx=10)

diag_label = tk.Label(frame_inserer_ordre, text="Diagnostic de Panne:")
diag_label.grid(row=0, column=0)
diag_entry = tk.Entry(frame_inserer_ordre)
diag_entry.grid(row=0, column=1)

nb_heures_label = tk.Label(frame_inserer_ordre, text="Nombre d'heures de main d'œuvre:")
nb_heures_label.grid(row=1, column=0)
nb_heures_entry = tk.Entry(frame_inserer_ordre)
nb_heures_entry.grid(row=1, column=1)

id_appareil_label = tk.Label(frame_inserer_ordre, text="ID de l'appareil:")
id_appareil_label.grid(row=2, column=0)
id_appareil_entry = tk.Entry(frame_inserer_ordre)
id_appareil_entry.grid(row=2, column=1)

inserer_button = tk.Button(frame_inserer_ordre, text="Insérer Ordre de Réparation", command=inserer_ordre_reparation)
inserer_button.grid(row=3, columnspan=2, pady=10)

montant_label = tk.Label(frame_calcul_montant, text="Montant Total pour le Client:")
montant_label.grid(row=0, column=0)
montant_entry = tk.Entry(frame_calcul_montant)
montant_entry.grid(row=0, column=1)
calculer_button = tk.Button(frame_calcul_montant, text="Calculer Montant Total", command=calculer_montant_total)
calculer_button.grid(row=0, column=2, padx=10)

prix_label = tk.Label(frame_afficher_pieces, text="Prix Supérieur à (€):")
prix_label.grid(row=0, column=0)
prix_entry = tk.Entry(frame_afficher_pieces)
prix_entry.grid(row=0, column=1)
afficher_pieces_button = tk.Button(frame_afficher_pieces, text="Afficher Pièces Supérieures", command=afficher_pieces_superieures)
afficher_pieces_button.grid(row=0, column=2, padx=10)

afficher_ordres_button = tk.Button(frame_afficher_ordres, text="Afficher Ordres Sans Pièces à Changer", command=afficher_ordres_sans_pieces)
afficher_ordres_button.pack()

root.mainloop()