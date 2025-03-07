# pin_cour
un script python qui permet d'épingler des dossier en fonction de l'heure, par exemple des cours 
## Fonctionement

Mettre ces cours dans le fichier `cours.py` sous la forme suivante :

```python
day = [
  Cour(
    week,
    cour,
    heure-debut,
    heure_fin
  )
]
```

### Parametre :

`day` : Jour. Valeurs possibless :
- `monday`
- `Mardi`
- `Mercredi`
- `Jeudi`
- `Vendredi`

`week` : `a`, `b` ou `a&b` (`a` pour semaine pair, `b` pour semaine impair, et `a&b` pour toute les semaines)
`cour` : Nom du dossier qu'il faudras épingler. Le chemin du dossier est dans la variable `Dossier_cour` du fichier `main.py`
`heure-debut` & `heure-fin` : respectivement l'heure de début et de fin au format `HH:MM:SS`
