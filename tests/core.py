
from regenerator import Regenerator

def test():
    xlist = list(range(5))
    regenerator = Regenerator((x for x in xlist))
    for item in regenerator:
        print(item)  
    assert all(xlist, list(regenerator))
    
