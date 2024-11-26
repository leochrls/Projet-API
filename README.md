Projet d'Analyse de Données : Impact de Facteurs Externes sur une Activité de Mobilité
Description
Ce projet analyse comment des facteurs externes (météo, événements publics, fermetures de routes, etc.) influencent l'utilisation de moyens de mobilité urbaine comme les vélos, scooters ou trottinettes. L'objectif est d'établir des corrélations et tendances entre ces facteurs et les données de mobilité.

Objectifs
Collecte des données : Utilisation d'APIs pour récupérer des données de mobilité et de contexte (météo, événements, etc.).
Nettoyage et stockage : Centralisation des données dans une base PostgreSQL pour une structure claire et exploitable.
Analyse statistique : Pré-analyse avec Python (matplotlib, pandas) pour détecter des corrélations significatives.
Visualisation : Création de tableaux de bord interactifs sur Kibana.
Architecture du Projet
Récupération des données : Scripts Python pour extraire des données d'APIs.
Pré-analyse : Nettoyage et analyse initiale dans Jupyter Notebook.
Stockage : Centralisation des données dans PostgreSQL pour permettre des jointures et agrégations.
Visualisation : Création de tableaux de bord dynamiques sur Kibana.
Visualisations Clés
Graphique Température vs Flux de Vélo : Aucune corrélation significative trouvée.
Heatmap Température/Précipitations vs Mobilité : Montre que les utilisateurs privilégient les vélos par temps sec, indépendamment de la température.
Difficultés rencontrées
Utilisation initiale de nouveaux outils (ElasticSearch, Kibana, Docker).
Limitations d'APIs et gestion des quotas.
Problèmes de connectivité entre outils.
Contraintes de temps, travail réalisé seul.
Outils Utilisés
Python : pandas, matplotlib, libraries pour interroger des APIs.
Jupyter Notebook : Pré-analyse et exploration des données.
PostgreSQL : Stockage structuré des données.
Kibana : Visualisation et exploration interactive.
