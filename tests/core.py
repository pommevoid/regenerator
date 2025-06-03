
from regenerator import Regenerator

def test():
    a = list(range(5))
    regenerator = Regenerator((item for item in a))
    for item in regenerator:
        print(item)  
    b = list(regenerator)
    assert len(a) == len(b)
    for item1, item2 in zip(a, b):
        assert item1 == item2
    
