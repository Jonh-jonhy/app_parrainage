<div align="center">

# 🤝 Application de Parrainage

**Attribue un parrain à chaque filleul, façon gacha.**
Enregistre tes participants, lance le tirage, exporte le résultat en PDF.

![Aperçu de l'application](docs/apercu.png)

</div>

---

## 📑 Sommaire

1. [Présentation](#-présentation)
2. [Ce dont tu as besoin](#-ce-dont-tu-as-besoin)
3. [Installation](#-installation)
4. [Lancer l'application](#-lancer-lapplication)
5. [Utilisation pas à pas](#-utilisation-pas-à-pas)
6. [Réinitialiser le parrainage](#-réinitialiser-le-parrainage)
7. [Problèmes fréquents](#-problèmes-fréquents)
8. [Pour les développeurs](#-pour-les-développeurs)

---

## ✨ Présentation

Cette application web permet de :

- 👥 **Enregistrer** des parrains et des filleuls (nom, prénom, photo)
- 🎰 **Tirer au sort** un parrain pour chaque filleul, avec une petite animation
- 📄 **Exporter en PDF** le tableau final « Filleul → Parrain »
- 🔄 **Recommencer** le parrainage à zéro quand tu le souhaites

Elle fonctionne **sur ton ordinateur**, dans ton navigateur, sans connexion internet une fois installée.

---

## 🧰 Ce dont tu as besoin

| Outil | Version | Comment vérifier |
|---|---|---|
| **Python** | 3.12 ou plus récent | `python --version` |
| **pip** | fourni avec Python | `pip --version` |

> 💡 Python n'est pas installé ? Télécharge-le sur [python.org/downloads](https://www.python.org/downloads/).
> **Sous Windows**, coche bien la case **« Add Python to PATH »** pendant l'installation.

> ℹ️ Selon ton système, la commande peut être `python3` et `pip3` au lieu de `python` et `pip`.

---

## 📦 Installation

Ouvre un **terminal** (PowerShell ou Invite de commandes sous Windows, Terminal sous macOS/Linux) et suis les étapes **dans l'ordre**.

### Étape 1 : Va dans le dossier du projet

Place-toi dans le dossier qui contient le fichier `manage.py` :

```bash
cd chemin/vers/le/dossier/du/projet
```

> 🔎 Pour vérifier que tu es au bon endroit, la commande `ls` (macOS/Linux) ou `dir` (Windows) doit afficher `manage.py` et `requirements.txt`.

### Étape 2 : Crée un environnement virtuel

L'environnement virtuel garde les bibliothèques de ce projet isolées du reste de ton ordinateur.

```bash
python -m venv venv
```

### Étape 3 : Active-le

**Windows (PowerShell) :**
```powershell
venv\Scripts\Activate.ps1
```

**Windows (Invite de commandes) :**
```cmd
venv\Scripts\activate.bat
```

**macOS / Linux :**
```bash
source venv/bin/activate
```

✅ Tu dois voir **`(venv)`** apparaître au début de ta ligne de terminal.

> ⚠️ Sous PowerShell, si une erreur parle de « scripts désactivés », lance d'abord
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, puis recommence.

### Étape 4 : Installe les bibliothèques

```bash
pip install -r requirements.txt
```

Cela installe automatiquement :

| Bibliothèque | Rôle |
|---|---|
| **Django** | Le framework de l'application |
| **Pillow** | Gestion des photos |
| **ReportLab** | Génération du PDF |
| asgiref, sqlparse, tzdata, charset-normalizer | Dépendances nécessaires |

<details>
<summary>📋 Contenu du fichier <code>requirements.txt</code></summary>

```text
asgiref==3.13.0
charset-normalizer==3.5.2
Django==6.1.2
pillow==13.0.0
reportlab==5.1.0
sqlparse==0.6.0
tzdata==2026.5
```

</details>

### Étape 5 : Crée la base de données

```bash
python manage.py migrate
```

Cette commande crée le fichier `db.sqlite3` et toutes les tables nécessaires. Tu verras défiler plusieurs lignes `OK` : c'est normal.

### Étape 6 : Crée ton compte administrateur (Pour Ajouter tes filleuls et parrains)

```bash
python manage.py createsuperuser
```

Le terminal te pose trois questions :

| Question | Que répondre |
|---|---|
| `Username` | Un identifiant de ton choix (ex. `admin`) |
| `Email address` | Ton e-mail (tu peux laisser vide avec Entrée) |
| `Password` | Un mot de passe (rien ne s'affiche quand tu tapes, c'est normal) |

> 🔐 **Retiens bien ces identifiants** : ils te serviront à te connecter à l'administration pour enregistrer tes parrains et filleuls.
> Si Django juge le mot de passe trop simple, il te propose de le garder quand même (réponds `y`).

✅ **L'installation est terminée !**

---

## 🚀 Lancer l'application

À chaque utilisation, depuis le dossier du projet :

**1. Active l'environnement virtuel** (si ce n'est pas déjà fait, voir l'étape 3)

**2. Démarre le serveur :**

```bash
python manage.py runserver
```

**3. Ouvre ton navigateur à l'adresse :**

👉 **http://127.0.0.1:8000/**

Pour **arrêter** l'application : retourne dans le terminal et appuie sur `Ctrl + C`.

---

## 🎮 Utilisation pas à pas

### 1️⃣ Page d'accueil

Tu y trouves deux grands boutons :

| Bouton | Action |
|---|---|
| 🛠️ **Administration** | Ouvre l'espace où tu enregistres tes parrains et filleuls |
| 🎰 **Lancer le parrainage** | Ouvre la page de tirage |

### 2️⃣ Enregistrer les parrains et les filleuls

1. Clique sur **Administration**.
2. Connecte-toi avec le compte créé à l'étape 6.
3. Dans la section **Parrainage**, tu vois **Parrains** et **Filleuls**.
4. Clique sur **Ajouter** à côté de **Parrains** et remplis le formulaire (nom, prénom, photo si tu en as une, capacité si elle existe), puis **Enregistrer**.
5. Fais de même pour chaque **Filleul**.

> 💡 Utilise **« Enregistrer et ajouter un nouveau »** pour saisir plusieurs personnes à la suite sans revenir en arrière.
>
> ⚠️ **Ne touche pas** à la section « Authentification et autorisation » : elle gère les comptes de connexion, pas tes participants.

**Avant de lancer le tirage, vérifie :**
- ✅ Tous tes parrains sont enregistrés
- ✅ Tous tes filleuls sont enregistrés
- ✅ Il y a assez de places chez les parrains pour accueillir tous les filleuls

### 3️⃣ Lancer le parrainage

1. Retourne à l'accueil (ou ouvre `http://127.0.0.1:8000/`).
2. Clique sur **Lancer le parrainage**.
3. La page affiche un filleul à gauche et une carte mystère `?` à droite.
4. Clique sur le grand bouton **Parrainer** : la poignée de main tremble, puis le parrain est révélé.
5. Recommence jusqu'à ce que **tous les filleuls aient un parrain**.

### 4️⃣ Parrainage terminé : le PDF

Quand tout le monde a un parrain, la page **« Parrainage terminé »** s'affiche.

Clique sur **📄 Générer le PDF** pour obtenir un tableau :

| Filleul | Parrain |
|---|---|
| Prénom Nom | Prénom Nom |

Tu peux l'enregistrer ou l'imprimer depuis ton navigateur.

---

## 🔄 Réinitialiser le parrainage

Tu veux **tout recommencer** (nouvelle promotion, nouveau tirage) ? Cette opération **retire le parrain de chaque filleul**. Les parrains et les filleuls **restent enregistrés**, seuls les liens entre eux sont effacés.

> ⚠️ **Cette action est irréversible** : le PDF doit être généré **avant** si tu veux conserver le résultat actuel.

### Méthode rapide (une seule commande)

Depuis le dossier du projet, avec l'environnement virtuel activé :

```bash
python manage.py shell -c "from parrainage.models import Filleul; print(Filleul.objects.exclude(parrain=None).update(parrain=None), 'filleul(s) réinitialisé(s)')"
```

Elle affiche le nombre de filleuls remis à zéro.

### Méthode pas à pas (dans le shell Django)

```bash
python manage.py shell
```

Puis colle ceci :

```python
from parrainage.models import Filleul

for filleul in Filleul.objects.all().exclude(parrain=None):
    filleul.parrain = None
    filleul.save()
    print(filleul.parrain)
```

Appuie **deux fois sur Entrée** après la dernière ligne pour valider. Chaque filleul traité affiche `None`, ce qui confirme qu'il n'a plus de parrain.

Pour quitter le shell : `exit()`.

> Tu peux ensuite relancer un tirage depuis la page d'accueil.

---

## 🆘 Problèmes fréquents

| Symptôme | Cause probable | Solution |
|---|---|---|
| `python : commande introuvable` | Python absent du PATH | Réinstalle Python en cochant « Add to PATH », ou essaie `python3` |
| `No module named django` | Environnement virtuel non activé | Active-le (étape 3), le `(venv)` doit apparaître |
| `No such file: manage.py` | Mauvais dossier | `cd` vers le dossier qui contient `manage.py` |
| `Error: That port is already in use` | Le serveur tourne déjà ailleurs | Ferme l'autre terminal, ou lance `python manage.py runserver 8001` |
| Impossible de se connecter à l'admin | Identifiants oubliés | Relance `python manage.py createsuperuser` (nouveau compte), ou `python manage.py changepassword nom_utilisateur` |
| La page est sans style (pas de couleurs) | Serveur démarré avant la création du dossier `static` | Arrête (`Ctrl+C`) et relance `runserver`, puis `Ctrl+F5` dans le navigateur |
| Les photos ne s'affichent pas | Le serveur doit être en mode développement | Vérifie que `DEBUG = True` dans `settings.py` et que le dossier `media/` existe |
| Le tirage dit qu'il n'y a plus de place | Pas assez de capacité chez les parrains | Ajoute des parrains ou augmente leur capacité dans l'admin |
| Le PDF est vide | Aucun filleul enregistré | Ajoute des filleuls dans l'administration |

---

## 🛠️ Pour les développeurs (Mon Bro Tu n'as pas besoin de lire ca !!)

### Structure du projet

```text
projet/
├── manage.py
├── requirements.txt
├── db.sqlite3                  # créé par « migrate »
├── media/                      # photos téléversées
├── docs/
│   └── apercu.png              # capture d'écran du README
├── config/                     # réglages du projet (settings.py, urls.py)
└── parrainage/
    ├── models.py               # Parrain, Filleul
    ├── views.py                # accueil, tirage, terminé, pdf
    ├── urls.py
    ├── admin.py
    ├── static/parrainage/      # style.css
    └── templates/parrainage/   # base.html, accueil.html, tirage.html, termine.html
```

> Adapte les noms des dossiers (`config/`, `parrainage/`) à ceux de ton projet.

### Technologies

- **Django 6.1** (backend, ORM, administration)
- **SQLite** (base de données, aucun serveur à installer)
- **Pillow** (photos) et **ReportLab** (PDF)
- **HTML / CSS / JavaScript** natifs pour l'interface

### Commandes utiles

```bash
python manage.py runserver        # lancer le serveur
python manage.py makemigrations   # préparer une modification des modèles
python manage.py migrate          # appliquer les modifications à la base
python manage.py createsuperuser  # créer un compte administrateur
python manage.py check            # détecter les erreurs de configuration
python manage.py dbshell          # ouvrir la base en ligne de commande
```

### ⚠️ Avertissement

Cette application est conçue pour un **usage local**. Pour la mettre en ligne, il faudrait au minimum : passer `DEBUG = False`, définir `ALLOWED_HOSTS`, utiliser une `SECRET_KEY` secrète, et faire servir les fichiers statiques et médias par un vrai serveur web.

---

<div align="center">

Fait par KAMDEM Marcel Jonathan avec 🐍 Python et Django

</div>