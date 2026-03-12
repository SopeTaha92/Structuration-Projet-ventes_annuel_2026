

from datetime import time
import sys

from loguru import logger
import pandas as pd





def extracting_data(path_data : str, max_retries : int, delay : int):
    for retry in range(max_retries):
        try:
            brute_data = pd.read_csv(path_data)
            logger.info(f"Extraction réussie : {len(brute_data)} lignes chargées.")
            return brute_data
        except FileNotFoundError as e:
            logger.error(f"Fichier introuvable à l'adresse : {e}")
            if retry < max_retries - 1:
                logger.error(f"Erreur {retry} / {max_retries}")
                logger.info(f"Nouvelle tentative dans {delay} secondes ...")
                time.sleep(delay)
                delay *= 2

    logger.critical(f"Echec Total après {max_retries} tentatives")
    sys.exit("Arret du programme :  impossible de chargé la source de donnée")
    














