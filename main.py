import json
from tkinter import *
from datetime import datetime, date
from tkinter import ttk
# Fichiers JSON pour stocker les utilisateurs et les stocks
USERS_FILE = "users.json"
STOCKS_FILE = "stocks.json"

# Charger les utilisateurs
def charger_utilisateurs():
    try:
        with open(USERS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Sauvegarder les utilisateurs
def sauvegarder_utilisateurs(users):
    with open(USERS_FILE, "w") as file:
        json.dump(users, file, indent=4)

# Charger les stocks
def charger_stocks():
    try:
        with open(STOCKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Sauvegarder les stocks
def sauvegarder_stocks(stock):
    with open(STOCKS_FILE, "w") as file:
        json.dump(stock, file, indent=4)

# Charger les données au démarrage
users = charger_utilisateurs()
stock = charger_stocks()

# Vérifier les identifiants
def verifier_utilisateur(pseudo, mdp):
    if pseudo in users and users[pseudo]["mdp"] == mdp:
        return users[pseudo]["role"]
    return None

# Création de la fenêtre principale
fenetre = Tk()
fenetre.title("Gestion des Stocks")
fenetre.state("zoomed")

# Frame pour le contenu principal
frame = Frame(fenetre)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# Fonction pour afficher différentes pages
def afficher_page(page):
    for widget in frame.winfo_children():
        widget.destroy()

    if page == "connexion":
        afficher_connexion()
    elif page == "menu_admin":
        afficher_menu_admin()
    elif page == "menu_client":
        afficher_menu_client()
    elif page == "gestion_stocks":
        afficher_gestion_stocks()
    elif page == "gestion_stocks_user":
        afficher_stock("client")
    elif page == "voir_stock":
        afficher_stock("admin")
    elif page == "ajout_produit":
        afficher_ajout_produit()
    elif page == "supp_stock":
        afficher_supprimer_produit()

# Affichage de la page de connexion
def afficher_connexion():
    Label(frame, text="Nom utilisateur: ").pack()
    input_utilisateur = Entry(frame, width=30, justify="center")
    input_utilisateur.pack(pady=5)

    Label(frame, text="Mot de passe: ").pack()
    input_mdp = Entry(frame, width=30, justify="center", show="●")
    input_mdp.pack(pady=5)

    message_label = Label(frame, text="", fg="red")
    message_label.pack(pady=10)

    def connexion():
        pseudo = input_utilisateur.get()
        mdp = input_mdp.get()
        role = verifier_utilisateur(pseudo, mdp)

        if role:
            message_label.config(text=f"Connexion réussie !", fg="green")
            fenetre.after(1000, lambda: afficher_page("menu_admin" if role == "admin" else "menu_client"))
        else:
            message_label.config(text="Identifiants incorrects", fg="red")

    Button(frame, text="Connexion", command=connexion).pack(pady=10)

# Affichage du menu administrateur
def afficher_menu_admin():
    Label(frame, text="=== MENU ADMINISTRATEUR ===", font=("Arial", 14, "bold")).pack(pady=10)

    Button(frame, text="Créer un utilisateur", command=afficher_creation_utilisateur).pack(pady=10)
    Button(frame, text="Afficher les utilisateurs", command=afficher_utilisateurs).pack(pady=10)
    Button(frame, text="Gestion des stocks", command=lambda: afficher_page("gestion_stocks")).pack(pady=10)
    Button(frame, text="Déconnexion", command=lambda: afficher_page("connexion")).pack(pady=10)

# Affichage du menu client
def afficher_menu_client():
    Label(frame, text="=== MENU CLIENT ===", font=("Arial", 14, "bold")).pack(pady=10)
    Label(frame, text="Bienvenue dans votre espace client !").pack(pady=10)
    Button(frame, text="Consulter les stocks", command=lambda: afficher_page("gestion_stocks_user")).pack(pady=10)
    Button(frame, text="Déconnexion", command=lambda: afficher_page("connexion")).pack(pady=10)

# Création d'un utilisateur
def afficher_creation_utilisateur():
    for widget in frame.winfo_children():
        widget.destroy()

    Label(frame, text="Créer un utilisateur").pack()
    Label(frame, text="Pseudo:").pack()
    entry_pseudo = Entry(frame, width=30)
    entry_pseudo.pack()

    Label(frame, text="Mot de passe:").pack()
    entry_mdp = Entry(frame, width=30, show="*")
    entry_mdp.pack()

    Label(frame, text="Rôle:").pack()
    role_var = StringVar(value="client")
    OptionMenu(frame, role_var, "admin", "client").pack()

    message_label = Label(frame, text="")
    message_label.pack()

    def enregistrer_utilisateur():
        pseudo = entry_pseudo.get()
        mdp = entry_mdp.get()
        role = role_var.get()


        if pseudo in users:
            message_label.config(text="Ce pseudo existe déjà.", fg="red")
            return

        users[pseudo] = {"mdp": mdp, "role": role}
        sauvegarder_utilisateurs(users)
        message_label.config(text="Utilisateur créé avec succès.", fg="green")
        return role

    Button(frame, text="Enregistrer", command=enregistrer_utilisateur).pack(pady=10)
    Button(frame, text="Retour", command=lambda: afficher_page("menu_admin")).pack(pady=10)

# Affichage des utilisateurs
def afficher_utilisateurs():
    for widget in frame.winfo_children():
        widget.destroy()

    Label(frame, text="Liste des utilisateurs:").pack()

    for pseudo, info in users.items():
        Label(frame, text=f"{pseudo} - {info['role']}").pack()

    Button(frame, text="Retour", command=lambda: afficher_page("menu_admin")).pack(pady=10)

def supprimer_produit():
    # Nettoyer le frame
    for widget in frame.winfo_children():
        widget.destroy()

    Label(frame, text="=== SUPPRESSION DE PRODUIT ===", font=("Arial", 14, "bold")).pack(pady=10)

    # Créer un dictionnaire {Nom du produit: ID}
    supp_noms = {stock[i].get("nom", f"Produit {i}"): i for i in stock if isinstance(stock[i], dict)}

    # Création du menu déroulant
    combo_var = StringVar()
    combo = ttk.Combobox(frame, textvariable=combo_var, values=list(supp_noms.keys()), state="readonly")
    combo.pack(pady=10)

    message_label = Label(frame, text="", font=("Arial", 11), fg="red")
    message_label.pack(pady=10)

    # Fonction pour supprimer le produit sélectionné
    def supp_deff():
        supp_nom = combo_var.get()  # Nom sélectionné dans la Combobox
        supp_id = supp_noms.get(supp_nom)  # Récupération de l'ID à partir du nom

        if not supp_nom or supp_id is None:
            message_label.config(text="⚠️ Veuillez sélectionner un produit.", fg="red")
            return

        del stock[supp_id]  # Supprimer le produit du dictionnaire
        sauvegarder_stocks(stock)  # Sauvegarder la mise à jour

        message_label.config(text="✅ Produit supprimé avec succès.", fg="green")

    Button(frame, text="Valider", command=supp_deff).pack(pady=10)
    Button(frame, text="Retour", command=lambda: afficher_page("gestion_stocks")).pack(pady=10)

def afficher_supprimer_produit():
    for widget in frame.winfo_children():
        widget.destroy()

    label = Label(frame, text="=== SUPPRIMER UN PRODUIT ===", font=("Arial", 14, "bold")).pack(pady=10)
    supprimer_produit()

# Affichage de la gestion des stocks
def afficher_gestion_stocks():
    for widget in frame.winfo_children():
        widget.destroy()

    Label(frame, text="=== GESTION DES STOCKS ===", font=("Arial", 14, "bold")).pack(pady=10)

    Button(frame, text="Créer un produit", command=lambda: afficher_page("ajout_produit")).pack(pady=10)
    Button(frame, text="Supprimé un produit", command=lambda: afficher_page("supp_stock")).pack(pady=10)
    Button(frame, text="Afficher les produits", command=lambda: afficher_page("voir_stock")).pack(pady=10)
    Button(frame, text="Retour au menu admin", command=lambda: afficher_page("menu_admin")).pack(pady=10)

from tkinter import ttk

def supprimer_perimes():
    """Supprime les produits dont la date de péremption est dépassée."""
    date_du_jour = date.today()
    ids_a_supprimer = []

    for id_produit, info in stock.items():
        date_peremption = datetime.strptime(info["date_peremption"], "%Y-%m-%d").date()
        if date_peremption < date_du_jour:
            ids_a_supprimer.append(id_produit)

    for id_produit in ids_a_supprimer:
        del stock[id_produit]

    sauvegarder_stocks(stock)
    if ids_a_supprimer:
       Label(frame, text="Produits périmés supprimés avec succès.", font=("Arial", 11,), fg="green").pack(pady=10)
    else:
        Label(frame, text="Aucun produit périmés à été trouver.", font=("Arial", 11,), fg="red").pack(pady=10)

def afficher_stock(role):  # Ajout du rôle
    for widget in frame.winfo_children():
        widget.destroy()

    Label(frame, text="=== PRODUITS EN STOCK ===", font=("Arial", 14, "bold")).pack(pady=10)

    # Vérifier si le stock n'est pas vide
    if not stock:
        Label(frame, text="Aucun produit en stock.", fg="red").pack(pady=10)
        Button(frame, text="Retour", command=lambda: afficher_page("gestion_stocks" if role == "admin" else "menu_client")).pack(pady=10)
        return

    # Créer un dictionnaire {Nom du produit: ID}
    produits_noms = {stock[i].get("nom", f"Produit {i}"): i for i in stock if isinstance(stock[i], dict)}

    # Création du menu déroulant (Combobox) avec les noms des produits
    combo_var = StringVar()
    combo = ttk.Combobox(frame, textvariable=combo_var, values=list(produits_noms.keys()), state="readonly")
    combo.pack(pady=10)

    # Label pour afficher les informations du produit sélectionné
    details_label = Label(frame, text="", font=("Arial", 12), justify="left")
    details_label.pack(pady=10)

    # Fonction pour afficher les détails du produit sélectionné
    def afficher_details(event):
        produit_nom = combo_var.get()  # Nom sélectionné dans le menu déroulant
        produit_id = produits_noms.get(produit_nom)  # Récupération de l'ID à partir du nom

        if produit_id and produit_id in stock:
            produit = stock[produit_id]
            details_label.config(text=f"ID: {produit_id}\n"
                                      f"Nom: {produit.get('nom', 'Inconnu')}\n"
                                      f"Quantité: {produit.get('quantité', produit.get('quantite', 'Inconnu'))}\n"
                                      f"Lieu: {produit.get('lieu', 'Inconnu')}\n"
                                      f"Date de péremption: {produit.get('date_peremption', 'Inconnue')}")

    # Associer la fonction au changement de sélection du menu déroulant
    combo.bind("<<ComboboxSelected>>", afficher_details)

    # Retirer les produi périmer
    if role == "admin":
        Button(frame, text="Supprimer les produit périmés", command=lambda: supprimer_perimes()).pack(pady=10)

    # Bouton de retour
    details_label.config(text=f"{role}", font=("Arial", 12), justify="left")
    Button(frame, text="Retour", command=lambda: afficher_page("gestion_stocks" if role == "admin" else "menu_client")).pack(pady=10)

# Création d'un produit
def afficher_ajout_produit():
    for widget in frame.winfo_children():
        widget.destroy()

    Label(frame, text="Créer un produit").pack()
    Label(frame, text="Nom du produit:").pack()
    entry_nom = Entry(frame, width=30)
    entry_nom.pack()

    Label(frame, text="Quantite:").pack()
    entry_quantite = Entry(frame, width=30)
    entry_quantite.pack()

    Label(frame, text="Lieu de stockage:").pack()
    entry_lieu = Entry(frame, width=30)
    entry_lieu.pack()

    Label(frame, text="Date de peremption (YYYY-MM-DD):").pack()
    entry_peremption = Entry(frame, width=30)
    entry_peremption.pack()

    message_label = Label(frame, text="")
    message_label.pack()

    def enregistrer_produit():
        id_produit = str(len(stock) + 1)
        stock[id_produit] = {
            "nom": entry_nom.get(),
            "quantité": entry_quantite.get(),
            "lieu": entry_lieu.get(),
            "date_peremption": entry_peremption.get()
        }
        sauvegarder_stocks(stock)
        message_label.config(text="Produit ajouté avec succès.", fg="green")

    Button(frame, text="Enregistrer", command=enregistrer_produit).pack(pady=10)
    Button(frame, text="Retour", command=lambda: afficher_page("gestion_stocks")).pack(pady=10)

# Lancer l'application
afficher_page("connexion")
fenetre.mainloop()