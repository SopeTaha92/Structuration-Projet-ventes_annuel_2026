





import pandas as pd
from loguru import logger

def analysis_by_region(file : pd.DataFrame):
    logger.info("Début de l'analyse par Region")
    analysis_by_region = (
        file.groupby('Region')
        .agg(
            {
                'Quantité' : 'sum',
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
    analysis_by_region['Marge_totaux'] = round((analysis_by_region['Profit'] / analysis_by_region['Revenue']), 2).astype(float)

    logger.success("l'analyse par Region terminé avec succée")

    return analysis_by_region
