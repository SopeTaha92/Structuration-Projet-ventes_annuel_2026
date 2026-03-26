
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Loguru](https://img.shields.io/badge/Loguru-000000?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![XlsxWriter](https://img.shields.io/badge/XlsxWriter-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)


# Pipeline d'Analyse de Ventes Automatisé (10k-1M lignes)

Ce projet est un pipeline ETL (Extract, Transform, Load) complet développé en Python. Il permet d'extraire des données de ventes massives, de les nettoyer, d'effectuer des analyses multidimensionnelles et de générer un rapport Excel professionnel entièrement automatisé avec des tableaux de bord visuels.

## 🚀 Fonctionnalités

- **Extraction Résiliente** : Système de lecture CSV avec mécanisme de "Retry" et délai exponentiel pour gérer les accès fichiers.
- **Traitement de Données** : Nettoyage, typage et enrichissement des données (calcul de profit, marges, etc.) via Pandas.
- **Reporting Excel Automatisé** : Génération d'un fichier `.xlsx` incluant :
  - Mise en forme conditionnelle (indicateurs de performance Vert/Rouge).
  - Graphiques combinés (Histogrammes de revenus + Courbes de marges sur axe secondaire).
  - Onglets structurés par Produit, Région et Période.
- **Architecture Professionnelle** : Centralisation de la configuration via `config.py` et journalisation complète via `Loguru`.

## 📁 Structure du Projet

├── data/
│   └── ventes_10k.csv           # Échantillon de données brutes (inclus)
├── logs/                        # Journaux d'exécution du pipeline
├── output/                      # Rapports Excel générés
├── src/                         # Code source du pipeline
│   ├── extract.py               # Logique d'extraction avec retry
│   ├── clean_data.py            # Nettoyage des données
│   ├── features.py              # Calcul des indicateurs métiers
│   ├── analysis_*.py            # Scripts d'analyses thématiques
│   └── repport_excel.py         # Moteur de génération du rapport Excel
├── config.py                    # Centralisation des chemins et paramètres
├── main.py                      # Point d'entrée de l'application
└── requirements.txt             # Dépendances du projet
🛠️ Installation et Utilisation

Cloner le dépôt :

Bash

git clone [https://github.com/SopeTaha92/Structuration-Projet-ventes_annuel_2026.git]

cd votre-depot


Installer les dépendances :

Bash

pip install -r requirements.txt


Lancer le pipeline :

Bash

python main.py


📊 Données
Le dépôt inclut un fichier de 10 000 lignes (data/ventes_10k.csv) pour permettre un test immédiat du pipeline. Le code est optimisé et a été testé sur des volumes allant jusqu'à 1 000 000 de lignes.

🛡️ Configuration
Le fichier config.py permet de modifier facilement :

Les chemins d'entrée/sortie.

Les seuils de rentabilité pour le formatage Excel.

Le nombre de tentatives d'extraction (Retry logic).

Projet réalisé dans le cadre d'une montée en compétence sur l'ingénierie de données (Data Engineering).



