from hypothesis.strategies import from_regex

g = from_regex(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$", fullmatch=True)

for _ in range(20):
    print(g.example())
