from sys import argv
from task_2 import *


if __name__ == '__main__':
    params = argv[1:]
    print(guess(*(int(param) for param in params)))