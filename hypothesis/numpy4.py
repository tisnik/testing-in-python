import numpy as np
from hypothesis.extra.numpy import arrays

g = arrays(np.half, (2, 3, 4), elements=None, unique=True)

for _ in range(10):
    print(g.example())
    print()
