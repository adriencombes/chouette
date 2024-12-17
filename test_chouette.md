# Test technique Chouette
*Le but de ce test technique est de tester votre capacité à écrire du code Python, à gérer la récupération et le stockage de données ainsi qu'à d'utiliser les technologies liées au machine learning.*

*Vous serrez attendu.e.s sur votre capacité à répondre à un cahier des charges en produisant du code clair et performant ainsi que sur votre aptitude à faire des choix techniques et à les argumenter.*

*Les performances des réseaux de neurones entrainés ne seront pas déterminantes.*

## Présentation du test
Le but de ces exercices est de développer un pipeline d'entrainement et de stockage et d'inférence de réseaux de neurones. 

Ces réseaux de neurones serviront à la classification de d'images selon 3 classes : "*vigne*", "*terre*" et "*herbe*".

Les entrainements de ces réseaux dépendent principalement de deux choses :
- Le dataset d'entrainement 
- La version du réseau

Chaque couple (dataset, réseau) pour donner lieu à l'entrainement d'un nouveau réseau.

### Datasets d'entrainement
Les images et les classes d'entrainement de ces réseaux seront à récupérer utilisant une API que nous vous fournissons.

Ces images peuvent être filtrée par date. Un dataset correspond à un choix de filtre sur cette API.

Cette API peut être appelée avec les paramètres suivants :

*URL* :  `api.staging.chouette.vision/api/jobs/get-images/`

*Credentials* :
user_name = job-testing@chouette.vision
password = ***

*Filtre* :

## Description  
Cet endpoint permet de récupérer une liste d'images associées à une catégorie (`tag`) et correspondant à une plage de dates définie (`start_date` et `end_date`).


## Méthode HTTP  
`GET`


## Paramètres de requête  

### `tag` *(obligatoire)*  
- **Description** : Filtre les images par leur catégorie.  
- **Valeurs possibles** :  
  - `vine` : Images liées à des vignes.  
  - `ground` : Images liées au sol.  
  - `grass` : Images liées à l'herbe.  
- **Exemple** : `?tag=vine`


### `start_date` *(obligatoire)*  
- **Description** : Définit la date de début pour filtrer les images (inclusif).  
- **Format attendu** : `YYYY-MM-DD` (par exemple, `2020-01-01`).  
- **Exemple** : `?start_date=2020-01-01`


### `end_date` *(obligatoire)*  
- **Description** : Définit la date de fin pour filtrer les images (inclusif).  
- **Format attendu** : `YYYY-MM-DD` (par exemple, `2021-01-01`).  
- **Exemple** : `?end_date=2021-01-01`


## Exemple de requête  
```bash
GET api.staging.chouette.vision/api/jobs/get-images/?tag=vine&start_date=2020-01-01&end_date=2021-01-01
```

Exemple de réponse de l'API :
```
[
   {
      "timestamp":"2024-08-05 10:54:11.151 +0200",
      "url":"http://.../3942460.jpg"
   },
   {
      "timestamp":"2024-08-01 06:55:28.546 +0200",
      "url":"http://.../3912247.jpg"
   },
   {
      "timestamp":"2024-08-05 10:03:18.600 +0200",
      "url":"http://.../3933565.jpg"
   },
]
```



### Versions du réseau
Vous utiliserez des réseaux de type ResNet avec Keras et Tensorflow :
https://keras.io/api/applications/resnet

Ce réseau existe en 6 versions différentes :

`ResNet50`, 
`ResNet101`, 
`ResNet152`, 
`ResNet50V2`, 
`ResNet101V2`, 
`ResNet152V2`

Chacune de ces version devra pouvoir être utilisée selon le choix de l'utilisateur.

## Exercice 1
Ecrire un code en utilisant Python et Tensorflow pour récupérer un dataset et entraîner un réseau de neurones de classification sur ce dataset.

**Entrée** : Paramètres du dataset (date_min et date_max) et version du réseau de neurones

**Sortie** : Réseau de neurones entraîné

## Exercice 2
Ecrire un code en utilisant Python et la technologie de votre choix pour stocker et récupérer les poids d'un réseau de neurones dont l'entrainement vient de se terminer. Vous utiliserez une base de donnée avec la structure qui vous semble le plus approprié.

## Exercice 3
Ecrire un code complet permettant :
- d'entrainer des réseaux de neurones et de les stocker automatiquement (Exercice 1 et 2)
- d'évaluer ces réseaux (en récupérant leurs poids sur la base de donnée précédemment créée) sur des images test


## Livrables
### Un dépôt GitHub public contenant :

Votre code source et vos scripts.
Une documentation claire (README.md) décrivant :
Les étapes pour configurer et exécuter votre projet.
Les choix techniques (base de données, JSON, structure du code, etc.).
Une solution automatisée (script ou autre) permettant de tester votre travail.

## Liberté et démarche :
Vous êtes totalement libre sur la manière de répondre aux exercices. L’objectif est de comprendre votre démarche, vos choix techniques et votre capacité à documenter et automatiser un projet reproductible.
Si certains aspects restent incomplets ou nécessitent une discussion, cela peut être abordé lors de l’entretien.

## Sécurité :

Évitez tout dépôt d'informations sensibles (clés API, identifiants de base de données, etc.).
Fournir un exemple de fichier de configuration (par exemple : config.example.env) listant les variables d'environnement nécessaires pour exécuter le projet.




