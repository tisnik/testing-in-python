import numpy as np
from hypothesis.extra.numpy import arrays

g = arrays(np.float, (4,3), elements=None)

for _ in range(10):
    print(g.example())
