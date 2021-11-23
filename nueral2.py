inputs = [1.2,2.4,5.6,6.7]
weights = [
    [7.2,3.0,4.1,0],
    [1.2,3.4,2.1,3],
    [3.2,8.4,1.1,5]]
biases = [1,2,3]
layer_outputs = []
for neuron_weights,neuron_bias in zip(weights,biases):
	neuron_output = 0
	for n_input,weight in zip(inputs,neuron_weights):
		neuron_output += n_input*weight
	neuron_output += neuron_bias
	layer_outputs.append(neuron_output)
print (layer_outputs)