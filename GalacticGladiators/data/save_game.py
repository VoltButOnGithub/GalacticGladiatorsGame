import os
import pickle

from GalacticGladiators.settings import SAVES_DIRECTORY


def save_game(game: 'Game') -> None:
    filename = f"{game.players[0].name}--{game.start_datetime.strftime('%d-%m-%Y-%H-%M-%S-%f')}.pk1"
    filepath = os.path.join(SAVES_DIRECTORY, filename)
    os.makedirs(SAVES_DIRECTORY, exist_ok=True)
    with open(filepath, 'wb') as file:
        pickle.dump(game, file)


def load_game(filepath: str, app: 'Application') -> 'Game':
    with open(filepath, 'rb') as game:
        unpickled_game = pickle.load(game)
        unpickled_game.app = app
        return unpickled_game


def delete_game_file(filepath: str) -> None:
    os.remove(filepath)


def delete_game(game: 'Game') -> None:
    filename = f"{game.players[0].name}--{game.start_datetime.strftime('%d-%m-%Y-%H-%M-%S-%f')}.pk1"
    filepath = os.path.join(SAVES_DIRECTORY, filename)
    delete_game_file(filepath)
