import numpy as np
import re

points = re.split('\D+', open("input").read())[:-1].reshape(-1,2)
print(points)

