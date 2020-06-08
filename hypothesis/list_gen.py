from hypothesis.strategies import lists, integers

g = lists(integers())

for _ in range(10):
    print(g.example())
