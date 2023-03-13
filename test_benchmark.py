from ismain import is_main

import timeit


def test_benchmark():
    elapsed_time = timeit.timeit(lambda: "-".join(map(str, range(100))), number=10000)
    print()
    print(f"{elapsed_time=}")


if is_main():
    test_benchmark()
