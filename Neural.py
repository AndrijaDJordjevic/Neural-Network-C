##
## EPITECH PROJECT, 2023
## NEURAL [WSL: Ubuntu]
## File description:
## Neural
##

import ReadWriteFile
import neuralClass as n
import numpy as np

# Constants
MAX_ITERATIONS = 10000

def preprocess_data(data):
    if len(data) == 0:
        print("Erreur: Aucune donnée valide.")
        return None
    max_values = np.amax(data, axis=0)
    non_zero_columns = max_values != 0
    data[:, non_zero_columns] = data[:, non_zero_columns] / max_values[non_zero_columns]
    return data

def train_neural_network(arg, X_train, y_train):
    if len(X_train) < 2:
        print("Erreur: Insuffisamment de données pour former le modèle.")
        return None

    if arg.load is not None:
        chess_nn = ReadWriteFile.load_network(arg.load[0])
    elif arg.new is not None:
        chess_nn = n.ChessStatusNeuralNetwork(arg.new[0], hidden_s=int(arg.new[1]), output_s=int(arg.new[2]))
    else:
        print("Erreur: Aucune option valide spécifiée pour la création du réseau neuronal.")
        return None

    chess_nn.train(X_train, y_train, iterations=MAX_ITERATIONS)
    return chess_nn


def make_predictions(chess_nn, fen_prediction):
    X_prediction = np.array([n.fen_to_matrix(fen_prediction)])
    X_prediction = preprocess_data(X_prediction)

    if X_prediction is not None:
        predictions = chess_nn.predict(X_prediction)

        for pred in predictions:
            print("Outcome prédit:", pred)
            if pred == 0:
                print("La partie est en cours.")
            elif pred == 1:
                print("Échec et mat.")
            elif pred == 2:
                print("Échec.")
            elif pred == 3:
                print("running")

def StartNeural(arg):

    if not arg.FILE:
        print("Erreur: Argument manquant.")
        return 1
    res, checkmate, fen_examples = ReadWriteFile.parse_dataset(arg.FILE[0])
    print(res)

    if arg.train is not False:
        print("trainning...")
        X_train = np.stack([n.fen_to_matrix(fen) for fen in fen_examples if n.fen_to_matrix(fen) is not None])
        X_train = preprocess_data(X_train)
        if isinstance(res, list):
            res = np.array(res)
        chess_nn = train_neural_network(arg, X_train, res)

    if arg.predict is not False and arg.load is not None:
        chess_nn = ReadWriteFile.load_network(arg.load[0])
        for fen_prediction in fen_examples:
            make_predictions(chess_nn, fen_prediction)

    if arg.save is not None:
        ReadWriteFile.save_network(chess_nn, arg.save[0])

    return 0
