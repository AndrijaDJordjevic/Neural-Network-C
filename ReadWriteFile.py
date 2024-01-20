##
## EPITECH PROJECT, 2023
## NEURAL [WSL: Ubuntu]
## File description:
## OpenFile
##

import re
import pickle

def save_network(network, file_name):
    with open(file_name, 'wb') as f:
        pickle.dump(network, f)

def load_network(file_name):
    with open(file_name, 'rb') as f:
        return pickle.load(f)
        
def parse_result(result):
    result_map = {
        '0-1': 1,   # Échec et mat
        '1-0': 2,   # Échec
        '1/2-1/2': 3,  # Égalité
        '0-0': 0,
    }
    return result_map.get(result, 0)
        
def parse_dataset(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    res_matches = re.findall(r'RES: (.+)', content)
    checkmate_matches = re.findall(r'CHECKMATE: (.+)', content)
    fen_matches = re.findall(r'FEN: (.+)', content)

    res = [parse_result(match.strip()) for match in res_matches]
    checkmate = [match.lower() == 'true' for match in checkmate_matches]
    fen = [match for match in fen_matches]

    return res, checkmate, fen