# Gestion des Stocks - Application Tkinter

## Présentation

Cette application Python propose un **système complet de gestion des stocks** via une interface graphique développée avec **Tkinter**.

Elle permet :
- La création et la gestion d'utilisateurs (admin/client)
- La connexion par identifiant et mot de passe
- L'ajout, la consultation et la suppression de produits du stock
- La suppression automatique des produits périmés
- Un espace distinct pour les administrateurs et les clients

Les données utilisateurs et stocks sont **stockées localement** sous forme de fichiers **JSON**.

---

## Fonctionnalités

### Gestion des utilisateurs
- **Création** d'un utilisateur avec choix du rôle (`admin` ou `client`)
- **Connexion sécurisée** par mot de passe
- **Affichage de la liste** des utilisateurs (admin uniquement)

### Gestion des stocks
- **Ajout** de nouveaux produits avec nom, quantité, lieu et date de péremption
- **Affichage** de la liste des produits en stock
- **Suppression** de produits manuellement ou automatiquement s'ils sont périmés
- **Consultation** des stocks pour les clients

### Différents accès selon le rôle
- **Admin** : accès complet à toutes les fonctionnalités
- **Client** : consultation uniquement des stocks

---

## Fichiers importants

- `users.json` : contient les identifiants des utilisateurs (pseudo, mot de passe, rôle)
- `stocks.json` : contient tous les produits enregistrés en stock

---

## Informations pour tester

🛠 **Pour tester rapidement l'application :**
- Utilisez les identifiants présents dans le fichier `users.json`.
- Vous pouvez aussi créer de nouveaux utilisateurs via l'interface si vous êtes connecté en tant qu'**admin**.

---

## Installation et Lancement

1. Clonez ce dépôt ou téléchargez les fichiers :
   ```bash
   git clone <URL_DU_DEPOT>
