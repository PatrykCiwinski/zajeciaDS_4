import numpy as np
from numpy import floor

marks = []
for num in range(5):
    num = 0.5*floor(2*np.random.uniform(0, 20))
    marks.append(num)

marks.sort()
print(marks)
marks.pop()
marks.pop(0)
print(marks)

