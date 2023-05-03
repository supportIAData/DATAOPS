import numpy as np

analys = np.array([1., 9., -90., 18., -76., 98., 100., 77., -5., 1020.])

print(analys.dtype)

print(analys)

mask = analys > 0

print(mask)

print(analys[mask])

analys[mask] = analys[mask]*1.1

print(analys)