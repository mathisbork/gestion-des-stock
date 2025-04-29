import json
import random
from datetime import datetime, timedelta

# Définition des produits avec des lieux de stockage cohérents
produits = [
    {"nom": "Lait frais", "lieu": "Frigo"},
    {"nom": "Yaourt", "lieu": "Frigo"},
    {"nom": "Fromage", "lieu": "Frigo"},
    {"nom": "Beurre", "lieu": "Frigo"},
    {"nom": "Poulet", "lieu": "Congélateur"},
    {"nom": "Poisson", "lieu": "Congélateur"},
    {"nom": "Frites congelées", "lieu": "Congélateur"},
    {"nom": "Glace", "lieu": "Congélateur"},
    {"nom": "Pain", "lieu": "Placard"},
    {"nom": "Farine", "lieu": "Placard"},
    {"nom": "Sucre", "lieu": "Placard"},
    {"nom": "Huile d'olive", "lieu": "Placard"},
    {"nom": "Céréales", "lieu": "Placard"},
    {"nom": "Pâtes", "lieu": "Placard"},
    {"nom": "Riz", "lieu": "Placard"},
    {"nom": "Tomates", "lieu": "Placard"},
    {"nom": "Pommes", "lieu": "Placard"},
    {"nom": "Carottes", "lieu": "Placard"},
    {"nom": "Chocolat", "lieu": "Placard"},
    {"nom": "Biscuits", "lieu": "Placard"}
]

# Génération des stocks avec des quantités et des dates de péremption valides
stocks = {}

for i, produit in enumerate(produits, start=1):
    quantite = random.randint(5, 100)  # Quantité entre 5 et 100

    # Génération d'une date de péremption future (entre aujourd'hui et 2 ans)
    jours_avance = random.randint(7, 31)  # Entre 1 semaine et 2 ans
    date_peremption = (datetime.today() + timedelta(days=jours_avance)).strftime("%Y-%m-%d")

    # Ajout au stock
    stocks[str(i)] = {
        "nom": produit["nom"],
        "quantité": quantite,
        "lieu": produit["lieu"],
        "date_peremption": date_peremption
    }

# Sauvegarde dans un fichier JSON
fichier_stocks = "stocks.json"
with open(fichier_stocks, "w") as file:
    json.dump(stocks, file, indent=4, ensure_ascii=False)

# Affichage du fichier généré
print(f"Fichier {fichier_stocks} généré avec succès.")
