# ETL

Extract Transform Load 

(extracted) cleaned, wrangled (transformed), and placed into a user-friendly data structure like a data frame (loaded).

## TP &Eacute;cart de salaires

Vous allez maintenant étudier l'écart des salaires des habitants de la ville de Boston par département sur l'année 2018. Récupérez le fichier json à l'adresse suivante :
[Analyse Boston](https://data.boston.gov/api/3/action/datastore_search?resource_id=31358fd1-849a-48e0-8285-e813f6efbdf1)

Vous utiliserez les dépendances suivantes

```python
import json
import numpy as np 
import pandas as pd 
import urllib.request
```

### Préparation des données

Approche ETL

1. Vous devez extraire les données à l'aide d'une fonction extract, utilisez la fonction read_csv

```python
def extract_boston_salary(url):
    pass
```

Pour extraire les données de l'API des salaires de Boston, à l'aide de votre fonction extract_boston_salary, vous utiliserez le code suivant, accédez à la clé **records** dans le fichier JSON pour récupérer les données.

```python
url = 'https://data.boston.gov/api/3/action/datastore_search?resource_id=31358fd1-849a-48e0-8285-e813f6efbdf1'  
fileobj = urllib.request.urlopen(url)
response_dict = json.loads(fileobj.read())

# La clé se trouve dans result => records dans le dictionnaire
```

2. Formatez les données de la colonne **TOTAL EARNINGS** pour les rendre compatibles avec un type numérique. Vous utilisez la méthode astype, voyez exemple ci-dessous :

Indications : vous devez éliminer les lignes qui posent problèmes voici quelques pistes,

- Créez un mask pour rechercher dans le DataFrame les lignes suivantes

```python
mask = data['TOTAL EARNINGS'] != 'TOTAL EARNINGS'
```

- Normalisez les formats de vos données et **modifiez** le DataFrame en conséquence.

```python
data['TOTAL EARNINGS'].str.replace(',', '')
```

- Forcez le type de vos champs à l'aide de la méthode suivante

```python
data['TOTAL EARNINGS'].astype(float)
```

Créez la fonction suivante qui va synthétiser votre approche d'analyse de données.

```python
def transform(data):
    pass
```

3. Enregistrez les données dans un nouveau fichier. Avec Pandas, voyez dans la documentation de la librairie, vous pouvez créez un fichier, implémentez cette dernière fonction.

```python
def load(data):
    pass
```

4. Facultatif

Vous pouvez également agréger les données à l'aide de la fonction groupby. Voyez la documentation de cette fonction et étudiez l'écart des salaires dans le département **Boston Police Department**.