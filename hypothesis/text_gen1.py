from hypothesis.strategies import text

g = text(min_size=5, max_size=10)

for _ in range(10):
    print(g.example())
