from hypothesis.strategies import lists, integers

g = lists(integers().filter(lambda x: x > 0 and x % 2 == 0))

for _ in range(10):
    print(g.example())
