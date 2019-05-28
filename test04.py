from collections.abc import Iterable, Iterator


def g():
    yield 1
    yield 2
    yield 3


print('Iterable?[1,2,3]:', isinstance([1, 2, 3], Iterable))

print('Iterator?[1,2,3]:', isinstance([1, 2, 3], Iterator))
