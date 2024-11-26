#!/bin/bash

set -e

# Si requirements.txt existe, installe les dépendances
if [ -e "/opt/airflow/requirements.txt" ]; then
  python -m pip install --upgrade pip
  pip install -r /opt/airflow/requirements.txt
fi

# Si la base de données n'est pas initialisée, initialise-la
if [ ! -f "/opt/airflow/airflow.db" ]; then
  airflow db init
fi

# Création de l'utilisateur admin si nécessaire
if ! airflow users list | grep -q "admin"; then
  airflow users create \
    --username admin \
    --firstname admin \
    --lastname admin \
    --role Admin \
    --email admin@example.com \
    --password admin
fi

# Mise à jour de la base de données pour s'assurer qu'elle est à jour
airflow db upgrade

# Lancer le webserver
exec airflow webserver
