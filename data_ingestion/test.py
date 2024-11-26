import psycopg2 # type: ignore

try:
    print("Tentative de connexion...")
    connection = psycopg2.connect(
        host="localhost",
        port=5432,
        database="Projet API Velo",
        user="postgres",
        password=""
    )
    print("Connexion réussie")
except psycopg2.Error as e:
    print("Erreur de connexion :", e)
finally:
    # Vérifiez si 'connection' est défini avant de tenter de le fermer
    if 'connection' in locals() and connection is not None:
        connection.close()
        print("Connexion fermée")