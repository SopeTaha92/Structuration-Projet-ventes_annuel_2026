


import pandas as pd
from loguru import logger

def analysis_by_produit(file : pd.DataFrame):
    logger.info("Début de l'analyse par produit")
    analysis_by_produit = (
        file.groupby('Produit')
        .agg(
            {
                'Quantité' : 'sum',
                'Prix_Unitaire' : 'first',
                'Coût_Unitaire' : 'first',
                'Montant_bonus' : 'mean',
                'Revenue' : 'sum',
                'Cout' : 'sum',
                'Profit' : 'sum'
            }
        )
        .round(2)
        .sort_values(by='Revenue', ascending=False)
        .reset_index()
    )
    analysis_by_produit['Marge_totaux'] = round((analysis_by_produit['Profit'] / analysis_by_produit['Revenue']), 2).astype(float)

    logger.success("l'analyse par produit terminé avec succée")

    return analysis_by_produit
