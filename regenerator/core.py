
from itertools import chain

class Regenerator:
    def __init__(self, generator):
        self.generator = generator

    def __iter__(self):
        return self.copy()

    def __list__(self):
        return list(self.copy())

    def copy(self):
        generator1 = empty_generator()
        generator2 = empty_generator()
        for item in self.generator:
            generator1 = chain(generator1, [item])
            generator2 = chain(generator2, [item])
        self.generator = generator1
        return generator2
 


def empty_generator():
    return
    yield


