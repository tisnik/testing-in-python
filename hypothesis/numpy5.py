import numpy as np
from hypothesis.strategies import integers
from hypothesis.extra.numpy import arrays

g = arrays(np.int32, (2, 3, 4), elements=integers(0, 100), unique=True)

for _ in range(10):
    print(g.example())
    print()
