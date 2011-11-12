"""
Task #2 solver

We are using multiprocessing module for faster calculations
"""
from operator import add
from multiprocessing import Pool


def _nums_generator(start_end):
    """
    Usage:
    >>> list(_nums_generator((0, 10)))
    ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    """
    star_num, end_num = start_end
    for n in xrange(star_num, end_num):
        for i in str(n):
            yield i


def _nums_counter(start_end):
    """
    Returns number of zeros in start_end range

    Args:
    ``start_end``: (start_num, end_num) tuple

    Usage:
    >>> _nums_counter((0, 20))
    2
    """
    iterable = _nums_generator(start_end)
    result = 0
    for i in iterable:
        result += (1 if i == '0' else 0)
    return result


def _chunks(length, chunk_size):
    """
    Usage:
    >>> list(_chunks(10, 2))
    [(0, 2), (2, 4), (4, 6), (6, 8), (8, 10)]
    """
    chunk_size = min(length, chunk_size)
    for i in xrange(0, length, chunk_size):
        yield (i, i + chunk_size)


def number_of_zeros(dec_str):
    """
    >>> number_of_zeros("219")
    42
    >>> number_of_zeros("100")
    10
    """
    num = int(dec_str)
    pool = Pool()  # number of workers equals number of CPUs
    result = reduce(
        add,
        pool.map(_nums_counter, _chunks(num, 10000))
    )
    if result > 1410000016:
        return result % 1410000017
    return result


def main():
    print number_of_zeros("219")


if __name__ == '__main__':
    main()
