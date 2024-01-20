# MyTorch B-CNA-500 Project README

## Introduction

Ce README fournit les instructions nécessaires pour lancer le projet MyTorch dans le cadre du cours B-CNA-500. Le projet implique la création d'un réseau de neurones pour analyser des parties d'échecs.

## Prérequis

- Un environnement de développement prenant en charge la compilation via Makefile.
- Les dépendances nécessaires pour exécuter le code (Python3).
- Dataset pour les echecs respectant la norme FEN

## Compilation

Pour compiler le projet, utilisez les commandes suivantes dans le répertoire racine :

\```bash
make
\```

Pour recompiler le projet :

\```bash
make re
\```

## Utilisation

\```bash
./my_torch [--new IN_LAYER [HIDDEN_LAYERS...] OUT_LAYER | --load LOADFILE] [--train | --predict] [--save SAVEFILE] FILE
\```

### Flags

\```bash
--train
\```
Lance le réseau neuronal en mode entraînement.

\```bash
--predict
\```
Prédit l'état actuel d'une partie d'échecs : échec, échec et mat, partie en cours, égalité.

\```bash
--New X Y Z
\```
Crée un nouveau réseau neuronal avec X = couche d'entrée, Y = couches cachées, Z = couche de sortie.

\```bash
--Load path
\```
Charge un réseau neuronal depuis un fichier spécifié.

\```bash
--save File
\```
Sauvegarde l'état actuel du réseau neuronal dans le fichier spécifié.

# Prédicteur d'État d'Échecs avec Réseau de Neurones

Ce script Python implémente un réseau de neurones simple pour prédire l'état d'une partie d'échecs en fonction de la représentation FEN (Forsyth-Edwards Notation) du plateau. Le réseau de neurones a une couche cachée et utilise la fonction d'activation sigmoïde pour la couche cachée et la fonction d'activation softmax pour la couche de sortie.

## Utilisation

1. **Initialisation**: Le réseau de neurones est initialisé avec la classe `ChessStatusNeuralNetwork`, qui prend la taille de l'entrée, la taille de la couche cachée et la taille de la sortie en tant que paramètres.

```python
neural_network = ChessStatusNeuralNetwork(taille_entree, taille_cachee, taille_sortie)
```

2. **Propagation avant (Forward Propagation)**: La méthode `forward_propagation` calcule la sortie du réseau de neurones étant donné la matrice d'entrée `X`.

```python
sortie = neural_network.forward_propagation(X)
```

3. **Entraînement**: La méthode `train` entraîne le réseau de neurones à l'aide de la rétropropagation. Elle prend la matrice d'entrée `X`, les étiquettes correspondantes `y` et le nombre d'itérations en tant que paramètres.

```python
neural_network.train(X, y, iterations)
```

4. **Prédiction**: La méthode `predict` prédit l'état de la partie d'échecs en fonction de la matrice d'entrée `X_prediction`.

```python
prediction = neural_network.predict(X_prediction)
```

5. **Conversion de FEN en Matrice**: La fonction `fen_to_matrix` convertit une chaîne FEN en un tableau 1D représentant le plateau d'échecs.

```python
fen = "votre_chaine_fen_ici"
matrice_aplatie = fen_to_matrix(fen)
```

## Architecture du Réseau de Neurones

- Taille de la couche d'entrée : 64 (correspondant à un plateau d'échecs 8x8)
- Taille de la couche cachée : 32
- Taille de la couche de sortie : 4 (en supposant une tâche de classification avec 4 classes)

Le réseau de neurones utilise la fonction d'activation sigmoïde pour la couche cachée et la fonction d'activation softmax pour la couche de sortie. L'initialisation des poids est réalisée en utilisant la méthode d'initialisation de He.

## Dépendances

- NumPy est utilisé pour les opérations numériques.

## Utilité des Fonctions d'Activation

1. **Sigmoïde pour la Couche Cachée (`sigmoid`)**:

   - **Utilité** : La fonction sigmoïde est couramment utilisée dans la couche cachée pour introduire une non-linéarité dans le modèle. Elle transforme les valeurs d'entrée en une plage de 0 à 1, facilitant l'apprentissage de motifs complexes par le réseau de neurones.
   - **Raison** : Les transformations linéaires successives sans fonction d'activation rendraient le réseau équivalent à une simple combinaison linéaire de ses entrées, perdant ainsi sa capacité à apprendre des relations non linéaires.

2. **Softmax pour la Couche de Sortie (`softmax`)**:

   - **Utilité** : La fonction softmax est utilisée pour obtenir des probabilités normalisées sur les classes de sortie. Elle convertit les scores bruts en probabilités, permettant de choisir la classe prédite avec la plus haute probabilité.
   - **Raison** : Dans les tâches de classification, softmax est souvent préféré car il fournit une distribution de probabilité sur les classes, rendant plus clair et interprétable le choix de la classe prédite.

3. **Dérivée de Sigmoïde (`sigmoid_derivative`)**:
   - **Utilité** : La dérivée de la sigmoïde est utilisée dans le processus de rétropropagation du gradient lors de l'entraînement du réseau. Elle est utilisée pour ajuster les poids du réseau et minimiser l'erreur.
   - **Raison** : La rétropropagation du gradient utilise la dérivée pour déterminer comment les poids doivent être ajustés pour minimiser l'erreur du réseau.

## Choix de la Taille du Réseau de Neurones

- **Couche d'Entrée (Input Layer) : 64 neurones (correspondant à un plateau d'échecs 8x8)**.

  - Raison : Chaque neurone représente une case du plateau.

- **Couche Cachée (Hidden Layer) : 32 neurones**.

  - Raison : Une taille de couche cachée plus petite est choisie pour éviter la surcomplexité et le surapprentissage. Elle est capable de capturer des caractéristiques plus abstraites du plateau d'échecs.

- **Couche de Sortie (Output Layer) : 4 neurones (supposant une classification avec 4 classes)**.
  - Raison : Chaque neurone représente une classe possible (état d'une partie d'échecs), avec la fonction softmax utilisée pour obtenir des probabilités normalisées.

## Conclusion

Le choix des fonctions d'activation et de la taille du réseau de neurones est crucial pour la performance et l'apprentissage efficace. Les fonctions d'activation introduisent la non-linéarité nécessaire pour modéliser des relations complexes, tandis que la taille du réseau est ajustée pour éviter le surapprentissage tout en conservant la capacité d'apprendre des modèles significatifs dans les données.
