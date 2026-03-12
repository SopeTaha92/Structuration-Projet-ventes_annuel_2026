


import pandas as pd 
from loguru import logger


def features_add(file : pd.DataFrame):
    logger.info("Début de l'ajout des collnes de calcule supllémentaire les (features)")

    try:

        
        heure = [t.hour for t in file["Heure_d'achat"]]
        file['Moment_journée'] = pd.cut(
            heure,
            bins=[0, 7, 12, 18, 22, 24],
            labels=['Nuit', 'Matin', 'Après-Midi', 'Soirée', 'Nuit_fin'],
            include_lowest=True
            #ordered=False Pour forcer pandas à fusionner les deux nuit sans se trompé 
        )

        file['jour_semaine'] = file['Date'].dt.day_name()#pour voir si c'est lundi ou autre 
    
        # 3. Optionnel : Traduire en français si tu préfères
        jours_fr = {
            'Monday': 'Lundi', 'Tuesday': 'Mardi', 'Wednesday': 'Mercredi',
            'Thursday': 'Jeudi', 'Friday': 'Vendredi', 'Saturday': 'Samedi', 'Sunday': 'Dimanche'
        }
        file['jour_semaine'] = file['jour_semaine'].map(jours_fr)

        file['Mois'] = file['Date'].dt.month_name()
        mois_fr = {
                    'January': 'Janvier',
                    'February': 'Février',
                    'March': 'Mars',
                    'April': 'Avril',
                    'May': 'Mai',
                    'June': 'Juin',
                    'July': 'Juillet',
                    'August': 'Août',
                    'September': 'Septembre',
                    'October': 'Octobre',
                    'November': 'Novembre',
                    'December': 'Décembre'
                }
        file['Mois'] = file['Mois'].map(mois_fr)
        file['Date'] = file['Date'].dt.date

        file['Moment_journée'] = file['Moment_journée'].astype(str).replace('Nuit_Fin', 'Nuit')
        file['Prix_de_vente'] = (file['Quantité'] * file['Prix_Unitaire']).astype(int)
        file['Montant_bonus'] = round((file['Bonus_%'] * file['Prix_de_vente']), 2).astype(float)
        file['Revenue'] = round((file['Prix_de_vente'] - file['Montant_bonus']), 2).astype(float)
        file['Cout'] = (file['Quantité'] * file['Coût_Unitaire']).astype(int)
        file['Profit'] = round((file['Revenue'] - file['Cout']), 2).astype(float)
        file['Marge'] = round((file['Profit'] / file['Revenue']), 2).astype(float)



        #heures = pd.to_timedelta(file["Heure_d'achat"]).dt.components.hours
        #heure_series = pd.to_timedelta(file["Heure_d'achat"], format='%H:%M:%S').dt.hour
        #heure = heure_series.dt.seconds // 3600

        logger.success("Fin de l'ajout des nouvelles colonnes")
    except Exception as e:
        logger.error(f"Erreur rencontré lors de l'ajout des nouvelles colonnes {e}")

    


    return file


