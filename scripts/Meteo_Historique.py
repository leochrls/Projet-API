from meteostat import Daily, Point  # type: ignore
from datetime import datetime
import pandas as pd  # type: ignore

# Définir les coordonnées de Rennes
rennes = Point(48.1173, -1.6778)

# Définir la période
start_date = datetime(2023, 1, 1)
end_date = datetime.now()  # Aujourd'hui

# Récupérer les données journalières
data = Daily(rennes, start_date, end_date)
data = data.fetch()

# Formatage des données
data['tavg_c'] = data['tavg']  # Température moyenne déjà en °C
data['prcp_mm'] = data['prcp']  # Précipitations moyennes en mm
data.reset_index(inplace=True)  # Réinitialiser l'index pour avoir la colonne 'time'

# Sélection des colonnes à exporter
data_to_save = data[['time', 'tavg_c', 'prcp_mm']]

# Enregistrer les données dans un fichier CSV
output_file = "meteo_rennes.csv"  # Nom du fichier
data_to_save.to_csv(output_file, index=False)

print(f"Les données ont été enregistrées dans le fichier '{output_file}'.")
