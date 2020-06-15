import numpy as np
from hypothesis.extra.numpy import arrays

g = arrays(np.int8, 10, elements=None)

for _ in range(10):
    print(g.example())
