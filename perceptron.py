Wayscript
Sign
Up
1
x_input = [0.1, 0.5, 0.2]
2
w_weights = [0.4, 0.3, 0.6]
3
threshold = 0.5
4
​
5


def step(weighted_sum):
    6


if weighted_sum > threshold:
    7
return 1
8
else:
9
return 0
10

11


def perceptron():
    12


weighted_sum = 0
13
for x, w in zip(x_input, w_weights):
    14
weighted_sum += x * w
15
print(weighted_sum)
16
return step(weighted_sum)
17
​
18
output = perceptron()
19
print("output: " + str(output))
