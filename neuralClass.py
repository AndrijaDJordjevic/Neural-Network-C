##
## EPITECH PROJECT, 2023
## neural
## File description:
## neural
##

import numpy as np

class ChessStatusNeuralNetwork:
    def __init__(self, input_s, hidden_s, output_s):
        self.input_size = 64
        self.output_size = 4
        self.hidden_size = 32
        self.weights_input_hidden = np.random.randn(self.input_size, self.hidden_size) * np.sqrt(2. / self.input_size)
        self.weights_hidden_output = np.random.randn(self.hidden_size, self.output_size) * np.sqrt(2. / self.hidden_size)

    def forward_propagation(self, X):
        self.hidden_layer_input = np.dot(X, self.weights_input_hidden)
        self.hidden_layer_output = self.sigmoid(self.hidden_layer_input)
        self.output_layer_input = np.dot(self.hidden_layer_output, self.weights_hidden_output)
        self.output = self.softmax(self.output_layer_input)
        return self.output

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def softmax(self, x):
        exp_values = np.exp(x - np.max(x, axis=1, keepdims=True))
        return exp_values / np.sum(exp_values, axis=1, keepdims=True)

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def backward_propagation(self, X, y, output):
        m = X.shape[0]
        self.output_error = output - y[:, np.newaxis]
        self.output_delta = self.output_error / m
        self.hidden_error = self.output_delta.dot(self.weights_hidden_output.T)
        self.hidden_delta = self.hidden_error * self.sigmoid_derivative(self.hidden_layer_output)
        self.weights_input_hidden -= X.T.dot(self.hidden_delta)
        self.weights_hidden_output -= self.hidden_layer_output.T.dot(self.output_delta)

    def train(self, X, y, iterations):
        for i in range(iterations):
            output = self.forward_propagation(X)
            self.backward_propagation(X, y, output)

    def predict(self, X_prediction):
        output = self.forward_propagation(X_prediction)
        return np.argmax(output, axis=1)


def fen_to_matrix(fen):
    piece_mapping = {
        'p': -1, 'r': -2, 'n': -3, 'b': -4, 'q': -5, 'k': -6,
        'P': 1, 'R': 2, 'N': 3, 'B': 4, 'Q': 5, 'K': 6
    }

    chess_matrix = np.zeros((8, 8), dtype=int)

    position, turn, castling, en_passant, halfmove, fullmove = fen.split()

    row = 0
    col = 0
    for char in position:
        if char == '/':
            row += 1
            col = 0
        elif char.isdigit():
            col += int(char)
        else:
            chess_matrix[row, col] = piece_mapping[char]
            col += 1

    # Flatten the 8x8 matrix into a 1D array
    flattened_matrix = chess_matrix.flatten()

    return flattened_matrix



