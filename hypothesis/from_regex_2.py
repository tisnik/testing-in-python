from hypothesis.strategies import from_regex

g = from_regex(r"#[a-fA-F0-9]{6}", fullmatch=True)

for _ in range(20):
    print(g.example())
