import numpy as np

X = [[1,2,3,2.5],
    [2.0,5.0,-1.0,2.0],
    [-1.5,2.7,3.3,-0.8]]

class LayerDanse:
    def __init__(self,n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1,n_neurons))
    def forward(self,inputs):
        self.outputs = np.dot(inputs,self.weights)+self.biases
layer1 = LayerDanse(4,5)
layer2 = LayerDanse(5,2)

layer1.forward(X)
layer2.forward(layer1.outputs)
print(layer2.outputs)