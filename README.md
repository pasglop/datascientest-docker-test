# Evaluation DataScientest - Data engineer - MAI 2023

## Introduction
On va mettre en place un docker compose pour pouvoir tester une application fastapi.

Les différents tests à effectuer sont les suivants :
- Test de l'authentification
- Test des autorisations
- Test de contenu renvoyé par l'API


## Prérequis
- Python 3.10
- pipenv
- pytest
- requests
- python-dotenv
- python-on-whales

## Installation
### Installation des dépendances
```bash
pipenv install
python -m pip install --upgrade pip
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### Lancement des tests
```bash
source env/bin/activate
python setup.py
```

## Résultats
Dans le répertoire test_results, vous trouverez les résultats des tests effectués:
- Un fichier JSON par test, avec les informations de la requête, la réponse, et les informations de la requête.
- un fichier HTML par test avec le résultat du test.
- un fichier XML par test avec le résultat du test utilisable sur Jenkins.
- un fichier log.txt avec les logs de l'exécution du test.