# Exercice 3 - Application multi-version avec optimisation

Objectif: gerer deux versions d'une API Python, optimiser l'image avec un multistage build et publier les versions sur Docker Hub.

## Contexte

Tu maintiens une API Flask de statistiques:
- Version `1.0.0`: endpoint `/api/stats`
- Version `2.0.0`: ajout de l'endpoint `/api/stats/median`

Tu dois publier plusieurs tags et faire en sorte que `latest` pointe vers la version la plus recente.

## Partie 1 - Version 1.0.0

### Travail a faire

1. Creer une premiere version de l'application avec l'endpoint `/api/stats`.
2. Utiliser un Dockerfile simple (sans multistage).
3. Construire et tester l'image `tonusername/stats-api:1.0.0`.
4. Publier cette version sur Docker Hub.

### Test attendu

Le calcul doit retourner au minimum:
- `count`
- `sum`
- `average`
- `min`
- `max`

## Partie 2 - Version 2.0.0 avec multistage

### Evolution fonctionnelle

Ajouter la route suivante dans `app.py`:

```python
@app.route('/api/stats/median', methods=['POST'])
def calculate_median():
    data = sorted(request.json.get('numbers', []))
    n = len(data)

    if n == 0:
        return jsonify({'error': 'No data provided'}), 400

    if n % 2 == 0:
        median = (data[n//2 - 1] + data[n//2]) / 2
    else:
        median = data[n//2]

    return jsonify({'median': median})
```

Mettre a jour `requirements.txt`:

```txt
flask==3.0.0
numpy==1.26.0
pytest==7.4.0
```

### Travail a faire

1. Modifier le Dockerfile pour un build multistage:
- Stage `builder`: base `python:3.12-slim`, installation des dependances de build/tests
- Stage `runtime`: base `python:3.12-alpine`, copie uniquement de ce qui est necessaire en execution

2. Construire et tester la version `2.0.0`.
3. Comparer la taille des images `1.0.0` et `2.0.0`.
4. Publier `1.0.0`, `2.0.0` et mettre `latest` sur `2.0.0`.

Les commandes doivent etre fournies dans un fichier separe `COMMANDS.md`.

## Questions de reflexion

- Quelle est la difference de taille entre `1.0.0` et `2.0.0` ? Il y a 8Mb de différence de taille
- Pourquoi `pytest` ne doit pas rester dans l'image de production ? Comme c'est pour les tests elle peut contenir des informations que les utilisateurs n'ont pas besoin
- Comment recuperer explicitement la version `1.0.0` depuis Docker Hub ? docker pull pseudo:1.0.0

## Criteres de validation

- Trois tags disponibles sur Docker Hub: `1.0.0`, `2.0.0`, `latest`
- L'image `2.0.0` est plus legere que `1.0.0`
- Les endpoints `/api/stats` et `/api/stats/median` fonctionnent
- Le tag `latest` pointe bien vers `2.0.0`
