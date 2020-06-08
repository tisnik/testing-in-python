from hypothesis.strategies import none, booleans, integers

g = none() | booleans() | integers(min_value=0, max_value=1000)

for _ in range(20):
    print(g.example())
