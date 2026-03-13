


from loguru import logger

from config import log_file, path_brute_data, max_retries, delay, file_clean_data, path_excel_file
from config import VALUE_RED_FORMAT, MIN_ORANGE_FORMAT, MAX_ORANGE_FORMAT, GREEN_FORMAT_MARGE

from src import logging_file
from src import extracting_data
from src import cleaning_data
from src import features_add
from src import analysis_by_produit, analysis_by_region, analysis_by_client_type, analysis_by_days, analysis_by_months
from src import excel_repporting




logging_file(log_file)
logger.info("Lancement du scripte de traitement des données")
data_brute = extracting_data(path_brute_data, max_retries, delay)
data_clean = cleaning_data(data_brute, file_clean_data)
complet_data = features_add(data_clean)
analyse_produit = analysis_by_produit(complet_data)
analyse_region = analysis_by_region(complet_data)
analyse_type_de_client = analysis_by_client_type(complet_data)
analyse_mois = analysis_by_months(complet_data)
analyse_jour = analysis_by_days(complet_data)


#   "Données Brutes Néttoyes" : data_clean,

Onglets = {
    "Données Brutes" : data_brute,
    "Données Propre Complét" : complet_data,
    "Données Par Produit" : analyse_produit,
    "Données Par Région" : analyse_region,
    "Données Par Type_Client" : analyse_type_de_client,
    "Données Par Mois" : analyse_mois,
    "Données Par Jour" : analyse_jour
}

excel_repporting(path_excel_file, Onglets, VALUE_RED_FORMAT, MIN_ORANGE_FORMAT, MAX_ORANGE_FORMAT, GREEN_FORMAT_MARGE)

