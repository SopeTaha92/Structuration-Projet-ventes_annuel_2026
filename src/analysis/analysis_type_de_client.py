








import pandas as pd
from loguru import logger

def analysis_by_client_type(file : pd.DataFrame):
    logger.info("Début de l'analyse par Type de Client")
    analysis_by_client_type = (
        file.groupby('Type_Client')
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
    analysis_by_client_type['Marge_totaux'] = round((analysis_by_client_type['Profit'] / analysis_by_client_type['Revenue']), 2).astype(float)

    logger.success("l'analyse par Type de Client terminé avec succée")

    return analysis_by_client_type
