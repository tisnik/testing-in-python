from string import printable
from hypothesis.strategies import text

g = text(printable, min_size=5, max_size=10)

for _ in range(10):
    print(g.example())
