


from loguru import logger
import pandas as pd

def cleaning_data(data, file):
    logger.info("Début du néttoyage des données brutes")
    clean_data = data.copy()
    logger.info("Copie des données brutes efféctué")
    clean_data = clean_data.drop_duplicates(keep='first')
    column_text = ['Nom_Client', 'Prenom_Client', 'Email_Client', 'Produit', 'Region', 'Type_Client'] 
    clean_data[column_text] = clean_data[column_text].apply(lambda x: x.str.strip().str.title())
    column_int = ['Quantité', 'Prix_Unitaire', 'Coût_Unitaire']
    clean_data[column_int] = clean_data[column_int].astype(int)
    clean_data['Bonus_%'] = (
        clean_data['Bonus_%']
        .str.replace('%', '', regex=False)
        .str.replace(' ', '', regex=False)
        .replace('', 0, regex=False)
        .astype(int) / 100
    ).round(2)
    clean_data['Date'] = pd.to_datetime(clean_data['Date'], format='mixed', dayfirst=True, errors='coerce')
    timedelta = pd.to_timedelta(clean_data["Heure_d'achat"], unit='s')
    clean_data["Heure_d'achat"] = (pd.to_datetime('2026-01-01') + timedelta).dt.time 

    logger.success("Néttoyage des données brutes terminé avec succée")
    clean_data.to_csv(file, index=False)
    logger.success(f"Création du fichiers pour les données brutes néttoyés terminé : {file}")
    return clean_data