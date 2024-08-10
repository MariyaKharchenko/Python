__all__ = ['json_to_pickle']


import json
import pickle
from pathlib import Path


def json_to_pickle(file: Path) -> None:
    for file in file.iterdir():
        if file.is_file() and file.suffix == '.json':
            with open(file, 'r', encoding='utf-8') as f_read:
                data = json.load(f_read)
            with open(f'{file.stem}.pickle', 'wb') as f_writebyte:
                pickle.dump(data, f_writebyte)


if __name__ == '__main__':
    json_to_pickle(Path(r'C:\Users\mariy\PycharmProjects\pythonProject\seminar_8'))