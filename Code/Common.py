from timeit import timeit


def get_int_lines(filename: str) -> list:
    lines = get_lines(filename)
    lines = list(map(int, lines))
    return lines


def get_lines(filename: str) -> list:
    f = open(filename)
    lines = list(map(lambda line: line.rstrip(), f.readlines()))
    f.close()
    return lines


def time_function(func) -> int:
    return timeit(func, number=100) / 100
