
from time import time
import tracemalloc

from regenerator import Regenerator


n = 100000000#0

# Generator by itself
tracemalloc.start()
start = time()
a = (item for item in range(n))
end = time()
current, peak = tracemalloc.get_traced_memory()
print(f"Generator = {end - start}, {current}, {peak}")
tracemalloc.stop()

# List by itself
tracemalloc.start()
start = time()
a = list(range(n))
end = time()
current, peak = tracemalloc.get_traced_memory()
print(f"List = {end - start}, {current}, {peak}")
tracemalloc.stop()

# Copy list
tracemalloc.start()
start = time()
a = list(range(n))
b = a.copy()
end = time()
current, peak = tracemalloc.get_traced_memory()
print(f"List copy = {end - start}, {current}, {peak}")
tracemalloc.stop()

# Regenerator
tracemalloc.start()
start = time()
a = (item for item in range(n))
b = Regenerator(a).copy()
end = time()
current, peak = tracemalloc.get_traced_memory()
print(f"Regenerator = {end - start}, {current}, {peak}")
tracemalloc.stop()
