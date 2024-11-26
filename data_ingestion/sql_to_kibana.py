import psycopg2 # type: ignore
from elasticsearch import Elasticsearch # type: ignore


# Connexion PostgreSQL
host = "localhost"
port = 5432
database = "Projet API Velo"
user = "postgres"
password = ""

# Connexion Elasticsearch
es = Elasticsearch("http://localhost:9200")

# Connexion à PostgreSQL
connection = psycopg2.connect(
    host=host,
    port=port,
    database=database,
    user=user,
    password=password
)

try:
    # Connexion à la base de données PostgreSQL
    cursor = connection.cursor()

    # Nom de la table météo avec guillemets pour respecter la casse exacte dans PostgreSQL
    table_meteovelo = 'public."velo_meteo"'  # Remplacez par le nom réel de votre table météo

    # Récupération des données de la table météo
    query = f"SELECT * FROM {table_meteovelo};"
    cursor.execute(query)

    # Récupération des résultats
    data = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]  # Récupère les noms des colonnes

    # Conversion des résultats en liste de dictionnaires
    data_dict = [dict(zip(columns, row)) for row in data]

    # Nom de l'index Elasticsearch
    index_name = table_meteovelo.split('.')[-1].strip('"').replace(' ', '_').lower()  # Utilisation du nom de la table pour l'index, sans les guillemets
    print(f"Envoi des données de la table {table_meteovelo} vers Elasticsearch...")

    # Envoi des données à Elasticsearch
    for doc in data_dict:
        es.index(index=index_name, body=doc)

    print("Données de la table météo envoyées à Elasticsearch avec succès")

except Exception as e:
    print("Erreur :", e)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("Connexion PostgreSQL fermée")
