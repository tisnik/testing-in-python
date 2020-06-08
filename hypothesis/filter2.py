from hypothesis.strategies import lists, integers

g = lists(integers().filter(lambda x: x > 0 and x % 2 == 0)).filter(lambda x: len(x) > 2 and len(x) < 6)

for _ in range(10):
    print(g.example())
