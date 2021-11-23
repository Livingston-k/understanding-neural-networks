import numpy as np

inputs = [2,5,6,1]
weights = [1.4,0.3,5.6,9.0]
bias = 2

outputs = np.dot(weights,inputs)+bias
print(outputs)