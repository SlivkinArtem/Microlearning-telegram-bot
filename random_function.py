import random

import all_parsers


def get_random_parser():
    return getattr(all_parsers, random.choice([func.__name__ for func in all_parsers.__all__]))


if __name__ == '__main__':
    get_random_parser()
