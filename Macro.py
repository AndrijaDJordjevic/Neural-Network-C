
MYTORCH_DESCRIPTION = """MyTorch is an innovative project that combines the power of neural networks with the strategic complexity of chess.
The goal of MyTorch is to create a neural network capable of analyzing chessboard positions and 
predicting the current state of the game, whether it's a checkmate, a check, a stalemate, or an ongoing game.
"""

NEW_DESCRIPTION = """--new       Creates a new neural network with random weights.
Each subsequent number represent the number of neurons on each layer, from left
to right. For example, ./my_torch –new 3 4 5 will create a neural network with
an input layer of 3 neurons, a hidden layer of 4 neurons and an output layer of 5
neurons."""

LOAD_DESCRIPTION = """--load      Loads an existing neural network from LOADFILE."""

TRAIN_DESCRIPTION = """--train     Launches the neural network in training mode. Each board in FILE
must contain inputs to send to the neural network, as well as the expected output."""

PREDICT_DESCRIPTION = """--predict Launches the neural network in predictin mode. Each board in FILE
must contain inputs to send to the neural network, and optionally an expected
output."""

SAVE_DESCRIPTION = """--save      Save neural network internal state into SAVEFILE."""

FILE = """FILE    FILE containing chessboards"""

EPILOG = "MADE by Martin petit, Andrija Djordjevic"