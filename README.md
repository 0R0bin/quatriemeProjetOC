# quatriemeProjetOC
Pour installer ce projet, placez vous dans le dossier et entrez la commande suivante
```
python -m venv env
```
Une fois l'environnement crée, activez le avec cette commande
```
env\scripts\activate.bat
```
Enfin installez les librairies requises
```
pip install -r requirements.txt
```

Pour générer un rapport flake8-html :
```
flake8 --format=html --htmldir=flake-report --max-line-length=119 --ignore=E128 controllers models views
```

Pour quitter et sauvegarder l'état du programme appuyez sur "Ctrl + C"