import numpy as np

inputs = [2,5,6,1]
weights = [[1.4,0.3,5.6,-9.0],
           [9.4,-1.3,5.6,2.0],
           [-7.4,3.3,1.6,-3.0],
           [7.1,2.3,9.6,-3.0]]
bias = [2,4,7.9,12]

outputs = np.dot(weights,inputs)+bias
print(outputs)