


import pandas as pd
from loguru import logger

def analysis_by_months(file : pd.DataFrame):
    logger.info("Début de l'analyse par Mois")
    df_group_months = (
        file.groupby('Mois')
        .agg(
            {
                'Produit' : 'count',
                'Quantité' : 'sum',
                'Revenue' : 'sum',
                'Cout' : 'sum',
                'Profit' : 'sum'
            }
        )
    )
    df_group_months['Marge_totaux'] = round((df_group_months['Profit'] / df_group_months['Revenue']), 2).astype(float)
    ordre_mois_fr = [
                        'Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 
                        'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre'
                    ]
    df_group_months = df_group_months.reindex(ordre_mois_fr)

    logger.success("l'analyse par Mois terminé avec succée")

    return df_group_months.reset_index()