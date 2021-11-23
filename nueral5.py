import numpy as np

inputs = [[1.4,0.3,5.6,-9.0],
          [9.4,-1.3,5.6,2.0],
          [-7.4,3.3,1.6,-3.0],
          ]

weights = [[1.4,0.3,5.6,-9.0],
           [9.4,-1.3,5.6,2.0],
           [-7.4,3.3,1.6,-3.0],
           ]
bias = [2,4,7.9]
# ANOTHER LAYER
weights2 = [[3.4,1.3,3.6,-5.0],
           [10.4,-4.3,4.6,2.0],
           [-7.4,3.3,1.6,-1.0],
           ]
bias2 = [2,4,7.9,3]


outputs = np.dot(inputs,np.array(weights).T)+bias
outputs2= np.dot(outputs,weights2)+bias2
print(outputs2) 