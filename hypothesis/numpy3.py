import numpy as np
from hypothesis.extra.numpy import arrays

g = arrays(np.bool, (10, 10))

print(g.example())
