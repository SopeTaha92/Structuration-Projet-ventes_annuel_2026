





import pandas as pd
from loguru import logger

def analysis_by_days(file : pd.DataFrame):
    logger.info("Début de l'analyse par jour")

    df_group_days = (
        file.groupby('jour_semaine')
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
    df_group_days['Marge_totaux'] = round((df_group_days['Profit'] / df_group_days['Revenue']), 2).astype(float)
    ordre_jours = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
    df_group_days = df_group_days.reindex(ordre_jours)

    logger.success("l'analyse par jour terminé avec succée ")

    return df_group_days.reset_index()