


from datetime import datetime
from pathlib import Path



today = datetime.now().strftime('%d-%m-%Y_%H-%M')
#path_brute_data = Path("data/raw/vente_annuel_2026.csv")
path_brute_data = Path("data/raw/Vente_annuel_2026.csv")
path_brute_data_clean = Path("data/processed")
path_brute_data_clean.mkdir(parents=True, exist_ok=True)

path_excel_file = Path("output") / f"vente_annuel_2026_nettoye_{today}.xlsx"
file_clean_data = path_brute_data_clean / f"vente_annuel_2026_nettoye_{today}.csv"
file_clean_data = path_brute_data_clean / f"vente_annuel_2026_nettoye_{today}.csv"

log_path = Path("logs")
log_path.mkdir(parents=True, exist_ok=True)
log_file = log_path / f"log_vente_annuel_2026_nettoye_{today}.log"


max_retries = 3
delay = 1


VALUE_RED_FORMAT = 0
MIN_ORANGE_FORMAT = 0
MAX_ORANGE_FORMAT = 500
GREEN_FORMAT_MARGE = 0.25

