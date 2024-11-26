# **Projet d'Analyse de Données : Impact de Facteurs Externes sur une Activité de Mobilité**

## **Description**
Ce projet analyse comment des facteurs externes influencent l'utilisation des vélos. Ici le facteur externe sera la météo avec deux variables : la température et les précipitations

## **Objectifs**
- **Collecte des données** : Extraction via APIs de mobilité et météo.
- **Pré-analyse** : Nettoyage et exploration des données dans Jupyter Notebook.
- **Stockage** : Base PostgreSQL pour les jointures et analyses.
- **Visualisation** : Tableaux de bord interactifs créés avec Kibana.

## **Visualisations Clés**
### Graphique 1 : Température vs Flux de Vélo
![Ce graphique montre qu’il n’y a pas de corrélation significative entre la température et le flux de vélos. Que les températures soient négatives ou positives, le nombre moyen de vélos utilisés reste stable.
](https://github.com/leochrls/Projet-API/blob/main/Temp%C3%A9rature%20vs%20Flux%20de%20V%C3%A9lo.png)
Ce graphique montre qu’il n’y a pas de corrélation significative entre la température et le flux de vélos. Que les températures soient négatives ou positives, le nombre moyen de vélos utilisés reste stable.


### Heatmap : Température/Précipitations vs Mobilité
![Heatmap Température/Précipitations](https://github.com/leochrls/Projet-API/blob/main/Temp%C3%A9raturePr%C3%A9cipitations%20vs%20Mobilit%C3%A9.png)
 La heatmap révèle que les utilisateurs privilégient les vélos par temps sec, indépendamment de la température. Les précipitations semblent être un facteur déterminant dans l’activité de mobilité.

### Dashboard
![Dashboard](https://github.com/leochrls/Projet-API/blob/main/Dashboard.png)
Le tableau de bord Kibana permet d'explorer les données de mobilité de manière interactive, avec des graphiques dynamiques montrant les tendances clés, les corrélations, et les impacts des facteurs externes comme la météo ou les précipitations.

## **Conclusion**
Les analyses effectuées sur les données de mobilité, en tenant compte des facteurs externes comme la météo et les événements publics, ont révélé des tendances intéressantes. Bien que la température semble avoir peu d'impact sur l'utilisation des vélos, les précipitations ont une influence plus marquée, avec une baisse notable de l'activité de mobilité en cas de pluie. Ces résultats peuvent être utilisés pour optimiser la gestion des services de mobilité urbaine, en ajustant par exemple la disponibilité des vélos, scooters ou trottinettes en fonction des conditions climatiques, ou en prévoyant des campagnes de communication durant les périodes propices à l’utilisation. Les entreprises et les municipalités pourraient également utiliser ces données pour planifier des événements ou ajuster les horaires de services publics en fonction des habitudes de mobilité identifiées.

## **Suite du projet**

Pour améliorer le projet, il faudra trouver un moyen de copntourner l'API Vélo puis créer des DAGs dans Airflow pour une éxécution et une analyse quotidienne.

## **Difficultés rencontrées**
- **Limitations des APIs** : Gestion des quotas.
- **Problèmes de connectivité** : Intégration entre outils.
- **Contraintes de temps** : Travail réalisé seul.
