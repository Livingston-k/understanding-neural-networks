inputs = [1.2,2.4,5.6,6.7]
weights = [7.2,3.0,4.1,0]
weights1 = [1.2,3.4,2.1,3]
weights2 = [3.2,8.4,1.1,5]

bias = 3
bias1 = 1
bias2 = 2
bias3 = 4

output = [
    inputs[0] * weights[0]+  inputs[1] * weights[1]+  inputs[2] * weights[2]+ inputs[3] * weights[3]+bias,
    inputs[0] * weights1[0]+  inputs[1] * weights1[1]+  inputs[2] * weights1[2]+ inputs[3] * weights1[3]+bias1,
    inputs[0] * weights2[0]+  inputs[1] * weights2[1]+  inputs[2] * weights2[2]+ inputs[3] * weights2[3]+bias2,
]
print(output)