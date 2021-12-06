from timeit import timeit


def get_int_lines(filename: str) -> list:
    lines = get_lines(filename)
    lines = list(map(int, lines))
    return lines


def get_lines(filename: str) -> list:
    with open(filename) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))
    return lines


def time_function(func, iterations=100) -> int:
    return timeit(func, number=iterations) / 100
